"""Template-based auto-reply generator for low-rated delivery app reviews.
한국어 배달 리뷰 CSV와 호환됩니다.
CSV 컬럼: 리뷰ID, 별점, 리뷰내용, 답글여부 (또는 rating/review/content 영문)
"""

from __future__ import annotations

import csv
from pathlib import Path
from typing import Any


def load_low_rating_reviews(
    csv_path: str | Path,
    rating_column: str = "별점",       # 한국어 CSV 기본값으로 수정
    max_rating: float = 2.0,
) -> list[dict[str, Any]]:
    """Load CSV and keep only reviews with 1-2 star ratings.
    
    한국어(별점) 및 영어(rating) 컬럼 모두 자동 감지.
    """
    low_reviews: list[dict[str, Any]] = []
    path = Path(csv_path)

    with path.open("r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames or []

        # 컬럼명 자동 감지: 별점 → rating 순서로 시도
        if rating_column not in fieldnames:
            for candidate in ("rating", "별점", "score", "점수"):
                if candidate in fieldnames:
                    rating_column = candidate
                    break

        for row in reader:
            raw = (row.get(rating_column) or "").strip()
            if not raw:
                continue
            try:
                rating = float(raw)
            except ValueError:
                continue
            if 1.0 <= rating <= max_rating:
                row["_rating"] = rating
                low_reviews.append(row)

    return low_reviews


def generate_reply(review_text: str, rating: float) -> str:
    """Generate a template-based reply without any LLM/API call.
    
    한국어 키워드 감지 + 영어 키워드 감지 모두 지원.
    """
    text = review_text  # 한국어는 lower() 불필요

    # 한국어 키워드 → 문제 분류
    if any(word in text for word in ("식", "차갑", "미지근", "cold", "temperature", "lukewarm")):
        issue_ko = "음식이 식어서 도착한 점"
        issue_en = "food temperature did not meet expectations"
    elif any(word in text for word in ("늦", "지연", "오래", "late", "delay", "slow")):
        issue_ko = "배달이 늦어진 점"
        issue_en = "delivery was delayed"
    elif any(word in text for word in ("빠진", "없", "누락", "틀린", "wrong", "missing", "different")):
        issue_ko = "주문 내용이 정확하지 않았던 점"
        issue_en = "the order was inaccurate"
    elif any(word in text for word in ("맛", "짠", "싱거운", "질긴", "눅눅", "taste", "salty", "bland")):
        issue_ko = "음식 맛과 품질이 기대에 미치지 못한 점"
        issue_en = "taste and quality were unsatisfactory"
    elif any(word in text for word in ("새", "포장", "용기", "쏟")):
        issue_ko = "포장 상태가 불량했던 점"
        issue_en = "packaging was inadequate"
    else:
        issue_ko = "불편함을 드린 점"
        issue_en = "your experience did not meet our standards"

    # 한국어인지 영어인지 감지 (한글 유니코드 범위)
    is_korean = any('\uAC00' <= c <= '\uD7A3' for c in text)

    if is_korean:
        return (
            f"고객님, {issue_ko} 진심으로 사과드립니다. "
            "소중한 의견을 전 직원과 공유하고 즉시 개선하겠습니다. "
            "더 나은 서비스로 다시 찾아주실 수 있도록 최선을 다하겠습니다. 감사합니다."
        )
    else:
        return (
            f"Thank you for your feedback. We are sorry that {issue_en}. "
            "We shared your review with our team and will improve immediately. "
            "Please give us another chance to provide a better meal next time."
        )


def _print_replies(csv_path: str | Path, max_rating: float = 2.0) -> None:
    reviews = load_low_rating_reviews(csv_path=csv_path, max_rating=max_rating)
    print(f"저평점 리뷰 발견: {len(reviews)}건 (최대 {max_rating}점)")
    print("----- 자동 답글 생성 결과 -----")
    for idx, row in enumerate(reviews, start=1):
        # 한국어/영어 컬럼명 모두 대응
        review_text = (
            row.get("리뷰내용") or row.get("review") or row.get("content") or ""
        ).strip()
        rating = float(row.get("_rating", 0))
        reply = generate_reply(review_text=review_text, rating=rating)
        print(f"[{idx}] ⭐{rating:.0f}점")
        print(f"리뷰  : {review_text}")
        print(f"답글  : {reply}")
        print()


if __name__ == "__main__":
    import sys

    csv_file = sys.argv[1] if len(sys.argv) >= 2 else "shared/delivery_reviews_sample.csv"
    _print_replies(csv_file)

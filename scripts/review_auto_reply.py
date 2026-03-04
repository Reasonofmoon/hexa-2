"""Template-based auto-reply generator for low-rated delivery app reviews."""

from __future__ import annotations

import csv
from pathlib import Path
from typing import Any


def load_low_rating_reviews(
    csv_path: str | Path,
    rating_column: str = "rating",
) -> list[dict[str, Any]]:
    """Load CSV and keep only reviews with 1-2 star ratings."""
    low_reviews: list[dict[str, Any]] = []
    path = Path(csv_path)

    with path.open("r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            raw = (row.get(rating_column) or "").strip()
            if not raw:
                continue
            try:
                rating = float(raw)
            except ValueError:
                continue
            if 1.0 <= rating <= 2.0:
                row["_rating"] = rating
                low_reviews.append(row)

    return low_reviews


def generate_reply(review_text: str, rating: float) -> str:
    """Generate a template-based reply without any LLM/API call."""
    text = review_text.lower()

    if any(word in text for word in ("cold", "temperature", "lukewarm")):
        issue = "food temperature did not meet expectations"
    elif any(word in text for word in ("late", "delay", "slow")):
        issue = "delivery was delayed"
    elif any(word in text for word in ("wrong", "missing", "different")):
        issue = "the order was inaccurate"
    elif any(word in text for word in ("taste", "salty", "bland")):
        issue = "taste and quality were unsatisfactory"
    else:
        issue = "your experience did not meet our standards"

    return (
        f"Thank you for your feedback. We are sorry that {issue}. "
        "We shared your review with our team and will improve immediately. "
        "Please give us another chance to provide a better meal next time."
    )


def _print_replies(csv_path: str | Path) -> None:
    reviews = load_low_rating_reviews(csv_path=csv_path)
    print(f"Low-rated reviews found: {len(reviews)}")
    print("----- Auto Replies -----")
    for idx, row in enumerate(reviews, start=1):
        review_text = (row.get("review") or row.get("content") or "").strip()
        rating = float(row.get("_rating", 0))
        reply = generate_reply(review_text=review_text, rating=rating)
        print(f"[{idx}] rating={rating:.1f}")
        print(f"Review: {review_text}")
        print(f"Reply : {reply}")
        print()


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        raise SystemExit("Usage: python review_auto_reply.py <reviews.csv>")
    _print_replies(sys.argv[1])

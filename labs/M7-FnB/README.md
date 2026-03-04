# M7-FnB 실습 가이드: 리뷰 분석 & 자동 응답

## 오늘 실습 목표
1. 고객 리뷰 데이터를 분석하여 긍정/부정 패턴을 파악한다
2. `review_auto_reply.py`를 Colab에서 직접 실행한다
3. 리뷰 자동 응답 시스템을 구축하고 테스트한다

---

## 🟢 Starter: 프롬프트만으로 (코딩 없음)

아래를 ChatGPT/뤼튼에 그대로 붙여넣고, `[]` 부분만 바꾸세요:

```
당신은 식음료(F&B) AI 컨설턴트입니다.
우리 매장(업종: [카페], 상품: [아메리카노])의 리뷰를 분석해주세요.
- 긍정 리뷰: "맛이 좋아요", "친절해요", "청결해요"
- 부정 리뷰: "느려요", "비싸요", "시끄러워요"
이 기준으로 자동 응답 메시지를 5개씩 만들어주세요.
긍정 리뷰에는 감사 표시, 부정 리뷰에는 개선 약속을 포함해주세요.
```

---

## 🔵 Professional: Colab 실행 (5단계)

**1단계**: Colab 뱃지 클릭 → 노트북 오픈  
**2단계**: `STORE_INFO` 셀에서 매장명·상품·API 키 수정  
**3단계**: 런타임 → 모두 실행  
**4단계**: 리뷰 분석 차트 자동 생성 확인  
**5단계**: `auto_reply_samples.md`·`review_analysis.png` 자동 다운로드 ✅

---

## 🔥 확장 과제 2개

**과제 1 — 별점 3점 필터링**
```python
# 별점 3점 이하 리뷰만 필터링하여 우선 응답
import pandas as pd
df = pd.read_csv('reviews.csv')
low_reviews = df[df['rating'] <= 3]
print(f"우선 응답 필요 리뷰: {len(low_reviews)}건")
```

**과제 2 — Gemini API 연동**
```python
# Google Gemini API로 리뷰 요약 및 응답 생성
import google.generativeai as genai
genai.configure(api_key="YOUR_GEMINI_KEY")
model = genai.GenerativeModel('gemini-pro')
response = model.generate_content(f"리뷰 요약: {review_text}")
```
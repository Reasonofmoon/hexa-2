# 🍽️ hexa-2: 외식/F&B AX 마스터클래스

> "배달 1점 리뷰가 자동으로 정중하게 답변된다" — 외식업 중소기업을 위한 AI 자동화 실습 과정

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Reasonofmoon/hexa-2/blob/main/notebooks/M7_FnB_review_lab.ipynb)

---

## 🎯 이 과정은?

**대상**: 음식점, 카페, 프랜차이즈, 배달앱 입점 사업자  
**목표**: 배달 리뷰 자동 답글·메뉴 분석·식자재 예측 3가지 핵심 자동화  
**시간**: 6시간 (강의 3h + 실습 3h)

---

## 🎯 수준별 활용 가이드

### 🟢 Starter — "5분 안에 배달 리뷰 답글 초안"
1. `labs/M7-FnB/README.md` 열기
2. 프롬프트 복사 → ChatGPT에 붙여넣기
3. 가게명·메뉴명만 수정 후 Enter ✅

### 🔵 Professional — Colab 자동화
1. Colab 뱃지 클릭
2. `RESTAURANT_INFO` 셀 수정
3. 런타임 → 모두 실행
4. 전체 저평점 리뷰 자동 답글 CSV 다운로드

### 🟣 Enterprise — 멀티 에이전트 파이프라인
- OMC로 리뷰 분석 → 답글 → SNS 포스팅 자동화
- `AGENTS.md` 기반 브랜드 보이스 내재화

---

## ⚙️ 3모듈 커리큘럼

| 모듈 | 제목 | Colab |
|---|---|---|
| M1 | AX 진단 & F&B 벤치마킹 | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](notebooks/M1_AX_diagnosis.ipynb) |
| M7-F&B | 배달 리뷰 자동 분석 & 답글 | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](notebooks/M7_FnB_review_lab.ipynb) |
| M9 | SNS 연동 & 마케팅 자동화 | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](notebooks/M9_marketing_auto.ipynb) |

---

## 📂 프로젝트 구조

```
hexa-2/
├── notebooks/
│   ├── M1_AX_diagnosis.ipynb
│   ├── M7_FnB_review_lab.ipynb   ← 배달 리뷰 자동화 ★
│   └── M9_marketing_auto.ipynb
├── labs/
│   ├── M1-diagnosis/README.md
│   └── M7-FnB/README.md          ← 실습 가이드 & 프롬프트
├── scripts/
│   ├── review_auto_reply.py       ← 리뷰 자동 답글
│   └── agents_config_validator.py
└── shared/
    └── delivery_reviews_sample.csv ← 샘플 배달 리뷰 데이터 (20행)
```

---

## 🌐 hexa 시리즈
- [hexa-1](https://github.com/Reasonofmoon/hexa-1): 🏭 제조업
- **hexa-2** (현재): 🍽️ 외식/F&B
- [hexa-3](https://github.com/Reasonofmoon/hexa-3): 🛒 소매/유통
- [hexa-4](https://github.com/Reasonofmoon/hexa-4): 📚 교육/에드테크
- [hexa-5](https://github.com/Reasonofmoon/hexa-5): 🏗️ 건설/부동산
- [hexa-6](https://github.com/Reasonofmoon/hexa-6): 💼 전문서비스/IT

<div align="center">

# 🍽️ hexa-2: F&B AX 마스터클래스

### *AI로 외식 비즈니스를 혁신하는 12주 실전 과정*

**메뉴카피부터 리뷰 감성분석까지 — 고객 데이터로 직접 검증하는 AX 커리큘럼**

[![Version](https://img.shields.io/badge/version-1.0.0-6366f1?style=for-the-badge)](https://github.com/Reasonofmoon/hexa-2)
[![Colab](https://img.shields.io/badge/Google_Colab-12개_노트북-F9AB00?style=for-the-badge&logo=googlecolab&logoColor=white)](https://github.com/Reasonofmoon/hexa-2/tree/main/notebooks)
[![Sector](https://img.shields.io/badge/Sector-F%26B-2563eb?style=for-the-badge&logo=restaurant&logoColor=white)](https://github.com/Reasonofmoon/hexa-2)
[![License](https://img.shields.io/badge/License-MIT-a78bfa?style=for-the-badge)](LICENSE)
[![Scripts](https://img.shields.io/badge/CLI_Scripts-8개-22d3ee?style=for-the-badge&logo=python)](scripts/)

> **"외식업 현장에서 AI 도구를 사용할 수 있는 인력은 전체의 5% 미만이다."**  
> hexa-2는 코딩 경험이 없는 점주·매니저도 Colab 노트북으로  
> 바로 실전 결과를 내도록 설계된 **12주 실무 중심 AX 커리큘럼**입니다.

[📗 커리큘럼 시작](notebooks/) · [🔧 스크립트 도구](scripts/) · [📂 실습 데이터](shared/) · [🐛 이슈](../../issues)

</div>

---

## 🧠 Philosophy — "왜 F&B AX인가"

기존 외식업 AI 교육의 문제: **가게 데이터가 없이 이론만 있다**.

| 기준 | 기존 AI 교육 | hexa-2 AX 커리큘럼 |
|------|-------------|-------------------|
| 데이터 | 가상의 식당 데이터 | **실제 리뷰 CSV** (배달, 방문, SNS) |
| 결과물 | 모델 정확도 숫자 | **자동 답글 + 재고예측 + SNS 콘텐츠** |
| 난이도 | Python 필수 | **Colab 실행만으로 완성** |
| 기간 | 3개월+ 이론 | **Week 1부터 실전 결과** |
| 연결성 | 개별 실습 | **W1→W12 파이프라인으로 연결** |

```mermaid
graph LR
    A[📋 W1-2 진단&메뉴] --> B[📝 W3-4 리뷰분석]
    B --> C[📊 W5-6 감성분석]
    C --> D[📨 W7-8 SNS자동화]
    D --> E[🔮 W9-10 재고예측]
    E --> F[🎛️ W11-12 통합대시보드]
    
    style A fill:#6366f1,color:#fff
    style F fill:#22d3ee,color:#fff
```

---

## ⚙️ 시스템 레이어

### Layer 1 · Foundation (W1~W4) — AI 기초 도구화
> **Wow**: 100개 배달 리뷰를 AI가 **5초 안에** 자동 감성 분류

| 주차 | 노트북 | 핵심 도구 |
|------|--------|-----------|
| W1 | M1_AX_diagnosis.ipynb | Gemini API, 자가진단 |
| W2 | W02_menu_copy.ipynb | 메뉴 카피, 가격 자동 설정 |
| W3 | W03_review_analysis.ipynb | 리뷰 감성 분석, 키워드 추출 |
| W4 | W04_reply_automation.ipynb | 자동 답글, 브랜드 보이스 |

### Layer 2 · Analytics (W5~W8) — 데이터 기반 의사결정
> **Wow**: 리뷰 감성·인기 메뉴·방문 시간을 **클릭 한 번**에 경영진 차트로 변환

| 주차 | 노트북 | 핵심 도구 |
|------|--------|-----------|
| W5 | W05_sales_analysis.ipynb | pandas, matplotlib, 상위 메뉴 |
| W6 | W06_review_sentiment.ipynb | 감성 트렌드, 부정 원인 분석 |
| W7 | W07_kakao_alert.ipynb | 카카오톡 알림, 실시간 알림 |
| W8 | W08_sns_content.ipynb | SNS 콘텐츠 자동 생성 |

### Layer 3 · Intelligence (W9~W12) — 자동화 운영 시스템
> **Wow**: 재고 부족 시 **자동 발주 → SNS 홍보 → 고객 알림** 파이프라인

| 주차 | 노트북 | 핵심 도구 |
|------|--------|-----------|
| W9 | W09_inventory_forecast.ipynb | 재고 예측, 3σ 이상감지 |
| W10 | W10_customer_segmentation.ipynb | 고객 세분화, 타겟 마케팅 |
| W11 | W11_fnb_dashboard.ipynb | 종합 F&B 대시보드 |
| W12 | W12_integrated_operation.ipynb | 통합 운영 시스템 발표 |

---

## 🎯 수준별 활용 가이드

### 🟢 Starter — "5분 안에 첫 결과"
1. [W3 노트북](https://colab.research.google.com/github.com/Reasonofmoon/hexa-2/blob/main/notebooks/W03_review_analysis.ipynb) 클릭 → Colab에서 열기
2. `RESTAURANT_INFO`에 가게명·메뉴명만 입력 (`✏️` 표시 찾기)
3. `Shift+Enter`로 위에서 아래로 실행
4. 리뷰 감성 분석 차트 + 결과 CSV 자동 다운로드

> ⚠️ API 키 발급: [Google AI Studio](https://aistudio.google.com/apikey) → GEMINI_API_KEY

### 🔵 Professional — "내 가게 데이터로 실전 분석"
1. `shared/delivery_reviews_sample.csv` 구조 확인
2. 내 가게 리뷰 데이터를 같은 형식으로 준비
3. W5~W6 노트북에서 CSV 업로드 → 감성·인기 메뉴 자동 분석
4. W7 노트북에서 카카오톡 API 연결 → 일일 리뷰 자동 발송

```bash
# CLI 스크립트 직접 사용
python scripts/review_auto_reply.py --input shared/delivery_reviews_sample.csv
python scripts/menu_copy_generator.py --input data.csv --webhook [WEBHOOK_URL]
python scripts/sentiment_analyzer.py --input data.csv --output results.csv
```

### 🟣 Enterprise — "팀 표준화 & 파이프라인"
1. `scripts/M9_demo_runner.py` 실행 → 전체 파이프라인 원클릭 시연
2. GitHub Actions로 매일 자동 리뷰 집계 스케줄링
3. W11~W12를 내부 대시보드로 배포 (Flask/Streamlit)
4. hexa-1, cedu-1과 연계해서 업종 간 벤치마킹

---

## 📂 디렉토리 구조

```
hexa-2/
├── notebooks/          ← 12주 Colab 노트북 (W01~W12)
│   ├── W02_menu_copy.ipynb              # 메뉴 카피 생성기
│   ├── W03_review_analysis.ipynb        # 리뷰 감성 분석
│   ├── W04_reply_automation.ipynb       # 자동 답글 시스템
│   ├── W05_sales_analysis.ipynb        # 매출 분석
│   ├── W06_review_sentiment.ipynb       # 감성 트렌드
│   ├── W07_kakao_alert.ipynb           # 카카오 알림
│   ├── W08_sns_content.ipynb          # SNS 콘텐츠 생성
│   └── W09_inventory_forecast.ipynb    # 재고 예측 이상감지
├── scripts/            ← CLI 실행 가능 Python 스크립트
│   ├── review_auto_reply.py            # 리뷰 자동 답글
│   ├── menu_copy_generator.py          # 메뉴 카피 생성기
│   ├── sentiment_analyzer.py           # 감성 분석기
│   ├── kakao_alert_sender.py          # 카카오 발송
│   ├── sns_content_generator.py       # SNS 콘텐츠 생성
│   ├── inventory_forecaster.py        # 재고 예측
│   ├── customer_segmenter.py          # 고객 세분화
│   └── M9_demo_runner.py              # 원클릭 데모 런처
├── shared/             ← 실습 데이터
│   ├── delivery_reviews_sample.csv     # 배달 리뷰 샘플
│   └── menu_items_sample.csv          # 메뉴 데이터 샘플
└── labs/               ← 실습 가이드 (M2~M7)
    ├── M2-menu/README.md
    ├── M3-review/README.md
    ├── M4-reply/README.md
    └── M7-FnB/README.md
```

---

## 🔧 확장 가이드

| 우선순위 | 커스터마이징 | 난이도 | 영향 범위 |
|----------|--------------|--------|-----------|
| **1st** | `RESTAURANT_INFO` 딕셔너리 수정 | ⭐ | 가게명·메뉴·날짜 |
| **2nd** | 샘플 CSV를 실제 데이터로 교체 | ⭐⭐ | 분석 결과 전체 |
| **3rd** | 카카오톡 API 연결 | ⭐⭐ | 실시간 알림 |
| **4th** | SNS API 인증 설정 | ⭐⭐⭐ | 마케팅 자동화 |
| **5th** | W11~W12 대시보드 서버 배포 | ⭐⭐⭐ | 팀 공유 시스템 |

---

## 🚀 빠른 시작

```bash
# 1. 레포 클론
git clone https://github.com/Reasonofmoon/hexa-2.git
cd hexa-2

# 2. 환경 설정 (로컬 실행 시)
pip install google-generativeai pandas matplotlib gspread requests

# 3. 데모 실행
python scripts/M9_demo_runner.py

# 4. 리뷰 분석 바로 실행
python scripts/sentiment_analyzer.py --input shared/delivery_reviews_sample.csv
```

또는 **Colab에서 바로 실행** (설치 불필요):  
[![W3 열기](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github.com/Reasonofmoon/hexa-2/blob/main/notebooks/W03_review_analysis.ipynb)
[![W6 열기](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github.com/Reasonofmoon/hexa-2/blob/main/notebooks/W06_review_sentiment.ipynb)
[![W9 열기](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github.com/Reasonofmoon/hexa-2/blob/main/notebooks/W09_inventory_forecast.ipynb)

---

## 🔗 전체 AX 시리즈

| 레포 | 섹터 | 핵심 모듈 |
|------|------|-----------|
| [hexa-1](https://github.com/Reasonofmoon/hexa-1) | 🏭 제조업 | OEE, 불량분류, 예지보전 |
| **hexa-2** (현재) | 🍽️ F&B | 리뷰분석, 메뉴카피, 재고예측 |
| [hexa-3](https://github.com/Reasonofmoon/hexa-3) | 🛒 소매/유통 | 상품카피, CRM, SEO |
| [hexa-4](https://github.com/Reasonofmoon/hexa-4) | 📚 교육 | 교안자동화, 성적분석, 챗봇 |
| [hexa-5](https://github.com/Reasonofmoon/hexa-5) | 🏗️ 건설 | 계약서분석, 공정관리 |
| [hexa-6](https://github.com/Reasonofmoon/hexa-6) | 💼 IT/서비스 | 제안서, 코드리뷰, KPI |

---

## 🌐 다국어 지원

| 항목 | 현황 |
|------|------|
| 노트북 UI | 한국어 |
| 스크립트 출력 | 한국어 (컬럼 자동감지: 한/영) |
| 샘플 데이터 | 한국어 컬럼명 |
| README | 한국어 / English (예정) |

---

*AX Consulting Curriculum © 2026 | Powered by Google Gemini*
# 기여 가이드 (Contributing Guide)

hexa-2 F&B AX 마스터클래스에 기여해 주셔서 감사합니다.

## 📋 Colab 노트북 기여 가이드

### 노트북 작성 규칙

1. **실행 가능한 상태 유지**: 모든 노트북은 오류 없이 실행 가능한 상태로 제출해야 합니다.
2. **한국어 주석 사용**: 코드 설명과 주석은 한국어로 작성합니다.
3. **Gemini API 사용**: AI 기능은 `gemini-2.0-flash` 모델을 기본으로 사용합니다.

### 노트북 구조

```python
# ✏️ 사용자 입력 섹션 (필수)
RESTAURANT_INFO = {
    "name": "가게명을 입력하세요",
    "menu": "메뉴명을 입력하세요",
    "date": "YYYY-MM-DD"
}

# 🔑 API 키 설정 (필수)
from google.colab import userdata
GEMINI_API_KEY = userdata.get('GEMINI_API_KEY')

# 📦 라이브러리 import
import google.generativeai as genai
import pandas as pd

# 🔧 메인 로직
# ...
```

## 🎨 코딩 컨벤션

| 항목 | 규칙 |
|------|------|
| 언어 | 한국어 주석, 변수명은 영어 |
| API | Google Gemini (`gemini-2.0-flash`) |
| 데이터 | `shared/` 폴더의 샘플 CSV 활용 |
| 출력 | 실행 결과가 명확하게 표시되도록 작성 |

## 🔀 Pull Request 규칙

### PR 제출 전 체크리스트

- [ ] 노트북이 Colab에서 오류 없이 실행됨을 확인
- [ ] 모든 셀이 순서대로 실행 가능함을 확인
- [ ] 한국어 주석이 충분히 작성됨
- [ ] 샘플 데이터로 테스트 완료

### PR 제목 형식

```
[노트북] W03 리뷰 감성 분석 개선
[스크립트] 메뉴 카피 생성기 추가
[문서] README 오타 수정
```

### PR 설명 템플릿

```markdown
## 변경 사항
- 변경 내용 요약

## 테스트 방법
1. Colab에서 노트북 열기
2. `Runtime > Run all` 실행
3. 결과 확인

## 관련 이슈
- #이슈번호 (있는 경우)
```

## 🚫 기여하지 말아야 할 것

- 실행 오류가 있는 노트북
- 한국어 주석이 없는 코드
- 다른 AI 모델을 하드코딩한 코드
- 샘플 데이터 없이 실제 데이터만 사용하는 코드

---

문의사항은 [Issues](../../issues)에 등록해 주세요.

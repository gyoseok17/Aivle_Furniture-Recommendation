## 나방(NABANG) — AI 기반 인테리어 추천·리모델링 웹앱

### 개요
- 방 사진 한 장으로 스타일·색상 분석과 가구 추천, 그리고 선택한 무드로 리모델링 이미지를 생성하는 웹 서비스입니다.
- 사진 기반 맥락 이해(Google Vision) + 생성형 AI(OpenAI) 결합으로, 사용자에게 즉각적인 인테리어 인사이트를 제공합니다.

### 설명
- **아키텍처 설계**: Django 기반 웹 구조/세션 흐름/템플릿 설계, 정적·미디어 자산 구성
- **AI 파이프라인 구현**: Google Vision 객체 감지 → 영역별 스타일 분류(SVM) → 색상 라벨링(KMeans) → GPT-4-Vision 가구 추천
- **생성형 리모델링**: OpenAI Image API로 스타일 변환 이미지 생성 및 저장/표시
- **인증/계정**: allauth + 카카오/구글/네이버 소셜 로그인 연동
- **DB/조회**: 추천 결과를 기반으로 `furniture` 테이블에서 연관 아이템 조회(랜덤 샘플링)

### 핵심 기술 스택
- **Backend**: Django
- **AI/ML**: Google Cloud Vision API, OpenAI GPT-4-Vision & Image, scikit-learn(SVM/KMeans)
- **DB**: MySQL
- **Frontend**: Django Templates, Vanilla JS/CSS

### 아키텍처 요약
- **분석 파이프라인**: Google Vision(객체 감지) → 영역 크기 가중치 → SVM 스타일 분류(`SVM2.joblib`) → LabelEncoder 복원 → KMeans 색상 군집 + 라벨링
- **추천/생성**: GPT-4-Vision 가구 카테고리 1종 추천 → OpenAI Image API로 선택 스타일의 방 이미지 생성
- **웹 흐름**: 업로드(비동기) → 세션 저장 → 결과 페이지에서 DB `furniture` 조회(랜덤 4개) 후 표시

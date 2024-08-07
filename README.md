## 2024년 8월 7일
- 보고서 종합의견 Gpt 사용성
- 네이버 API 

## 2024년 8월 5일
- df text 외국어 비중 검사 구현 완료
- 반의어 리스트
    100여개 반의어 리스트 생성 완료(Lark 전체 메신저)

## 2024년 8월 2일
영희가 필요없는 파일들 삭제함 (aaa, ade와 같은 고양이 이미지)

## 2024년 7월 30일
- **부정표현 리스트** `negative-word`로 업로드 완료
- **반의어 데이터 자료** 리스트、 텍스트형 데이터는 아직 찾지 못함、（형태분석、 유사문、 감정분석 자료는 많지만 반의어는 찾을 수 없었음）
－ 국립국어원 ＡＰＩ사용¿¿¿¿¿¿¿
- **BERT_문장(동사)_의미분석** 윤아꺼 보는중
  
## 2024년 7월 29일
- **국립국어원 언어정보나눔터 "일상 대화 요약 말뭉치 2023"** 다운 완료 ｊｓｏｎ파일임
- 자료명: 국립국어원 일상 대화 요약 말뭉치 2023
  공개일 (버전 1.0) 2024. 6. 28.
  자료 유형: 텍스트
  내용 ： 국립국어원 일상 대화 말뭉치 2020, 2021에서 추출한 대화 2,000건에 대해 담화 분석을 실시하고 주제별로 대화를 분할하여 화자별, 주제별 요약문을 도출하고 이를 토대로 대표 요약문을 작성한 말뭉치    
  담화 분석: 문장 세트 분류(type), 각 문장 세트에 대한 화행(dialog_act)과 관계(target) 주석, 중심 문장 간 관계(relational_triple) 분석    
  요약문 작성: 문장 세트를 주제별로 묶어(utterance_group) 중심어(keyword) 선별, 주제별 대화 요약문(conversation_summary) 및 화자별 요약문(speaker_summary) 작성, 결정 사항(decisions) 추출. 이를 토대로 대표 요약문(main_summary) 작성    
  분량 ： 문서 2,000건(원시 말뭉치 기준 약 300만 어절)    
  파일 형식: JSON(UTF-8 인코딩)     
  파일 수 및 크기: 텍스트 파일 2,000개, 총 26MB(ZIP파일기준)    

## 2024년 7월 25일
### 데이터
- **부정표현 리스트**
  - **부정표현 단어 수**: 9826
  - **출처**: 표준국어대사전, 신조어, 이모티콘, SentiWordNet_3.0.0_20130122, SenticNet-5.0, 감정단어사전0603 / 김은영, “국어 감정동사 연구”, 2004.02, 학위논문(박사) - 전남대학교 국어국문학과 대학원
  - **문제점**: 사전형 단어임. 일상생활에 쓰는 형태가 아니라 변환 필요 (현 데이터 예시: 격노하다, 격분, 격분하다, 격하게)

- **일반단어**
  - **국립국어원 언어정보나눔터 "일상 대화 요약 말뭉치 2023"** 신청 완료 상태 (공공데이터처럼 국어원에서 제공하는 데이터처럼 보임)

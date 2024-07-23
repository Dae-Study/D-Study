# 검색창 구현 + 검색어 추천 기능 구현 서비스입니다. (👨‍👩‍👧‍👦 9팀)

> pre-onboarding-7th-3-1-9

| <img src="https://avatars.githubusercontent.com/u/58911113?v=4" width="120" height="120" /> | <img src="https://avatars.githubusercontent.com/u/74575497?v=4" width="120" height="120" /> | <img src="https://avatars.githubusercontent.com/u/72599761?v=4" width="120" height="120"/> |
| :-----------------------------------------------------------------------------------------: | :-----------------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------: |
|                                           👑 권준                                           |                                           김경훈                                            |                                           김수정                                           |
|                            [@jun-05](https://github.com/jun-05)                             |                          [@tirhande](https://github.com/tirhande)                           |                        [@crystal993](https://github.com/crystal993)                        |

| <img src="https://avatars.githubusercontent.com/u/104307213?v=4" width="120" height="120"/> | <img src="https://avatars.githubusercontent.com/u/94212747?v=4" width="120" height="120" /> | <img src="https://avatars.githubusercontent.com/u/77476348?v=4"  width="120" height="120" /> | <img src="https://avatars.githubusercontent.com/u/76990149?v=4" width="120" height="120"/> |
| :-----------------------------------------------------------------------------------------: | :-----------------------------------------------------------------------------------------: | :------------------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------: |
|                                           송슬기                                            |                                           오나래                                            |                                            이창훈                                            |                                           전이진                                           |
|                          [@songseul](https://github.com/songseul)                           |                            [@NR0617](https://github.com/NR0617)                             |                 [@anotheranotherhoon](https://github.com/anotheranotherhoon)                 |                          [@pongdang](https://github.com/pongdang)                          |

#

## **✨ 배포 링크**

## [배포 바로가기](https://pre-onboarding-7th-3-1-9-tau.vercel.app/main)

#

## ‼️ 주요 기능 구현

### 0️⃣ json-server 배포

- localhost가 아닌 vercel에 json-server를 배포하여 사용
- ex) https://json-server-beryl.vercel.app/api/sick?sickNm_like=간
- ex) https://json-server-beryl.vercel.app/api/sick?q=콜레라

### [3️⃣ API 호출 캐싱 링크](#3️⃣-assignment)

### [4️⃣ API 호출 횟수 줄이기 링크](#4️⃣-assignment)

### [6️⃣ 키보드만으로 추천 검색어 이동 링크](#6️⃣-assignment)

#

## 📝 목차

- [📰 프로젝트 설명](#-프로젝트-설명)
- [🛠️ Dev Tools](#-dev-tools)
- [🖥 프로젝트 실행 방법](#-프로젝트-실행-방법)

#

## **📰 프로젝트 설명**

- 검색창 구현 + 검색어 추천 기능 구현 서비스입니다.

#

## **🛠 Dev Tools**

![badge](https://img.shields.io/badge/React-61dafb?logo=React&logoColor=white&style=flat-square) ![badge](https://img.shields.io/badge/Typescript-3178C6?style=flat-square&logo=Typescript&logoColor=white) ![badge](https://img.shields.io/badge/npm-CB3837?logo=npm&logoColor=white&style=flat-square) ![badge](https://img.shields.io/badge/redux_toolkit-764ABC?style=flat-square&logo=redux&logoColor=black) ![badge](https://img.shields.io/badge/styled%20components-DB7093?style=flat-square&logo=styled%20components&logoColor=white) ![badge](https://img.shields.io/badge/Visual%20Studio%20Code-007ACC?style=flat-square&logo=Visual%20Studio%20Code&logoColor=white)

#

## **🖥 프로젝트 실행 방법**

```sh
### Installation
# Repositorie Clone
git clone https://github.com/Wanted-07-team-9/pre-onboarding-7th-3-1-9.git

# npm으로 설치 진행
pre-onboarding-7th-3-1-9 %  % npm install

### Usage
# Local Dev Server 실행
pre-onboarding-7th-3-1-9 % npm start

# Build
pre-onboarding-7th-3-1-9 % npm build
```

#

## **✏ 토의 내용 및 선정**

[🖍 1차 토의결과](https://github.com/Wanted-07-team-9/pre-onboarding-7th-3-1-9/discussions/1)

[🖍 2차 토의결과](https://github.com/Wanted-07-team-9/pre-onboarding-7th-3-1-9/discussions/2)

[🖍 3차 토의결과](https://github.com/Wanted-07-team-9/pre-onboarding-7th-3-1-9/discussions/7)

[🥇 선정 결과](https://github.com/Wanted-07-team-9/pre-onboarding-7th-3-1-9/discussions/20)

#

## **📝 디렉토리 구조**

```sh
📂 pre-onboarding-7th-3-1-9
┣ 📂 public
┣ 📂 src
┃   ┣ 📂 @types           # type 정의 모음
┃   ┣ 📂 apis             # axios 호출 관련
┃   ┣ 📂 components       # component 모음
┃   ┣   ┣ 📂 blocks       # page보단 작고 button 같은 component보단 큰 애들
┃   ┣   ┗ 📂 common       # button, input, select box와 같은 component
┃   ┣ 📂 assets           # 파일들 (이미지 파일 등)
┃   ┣ 📂 hooks            # custom hook
┃   ┣ 📂 pages            # 페이지 단위로 구분
┃   ┣   ┣ 📂 Main         # 메인 페이지
┃   ┣   ┗ 📂 NotFound     # 404 NotFound 페이지
┃   ┣ 📂 redux            # redux/toolkit, store 디렉토리
┃   ┣   ┗ 📂 reducer      # reducer/slice 디렉토리
┃   ┣ 📂 router           # page Router 관리 페이지
┃   ┗ 📂 styles           # global style
┗ 📄 README.md            # README 파일
```

#

## **💡 Assignment 목차**

- [1️⃣ Assignment](#1️⃣-assignment)
- [2️⃣ Assignment](#2️⃣-assignment)
- [3️⃣ Assignment](#3️⃣-assignment)
- [4️⃣ Assignment](#4️⃣-assignment)
- [5️⃣ Assignment](#5️⃣-assignment)
- [6️⃣ Assignment](#6️⃣-assignment)
- [7️⃣ Assignment](#7️⃣-assignment)

#

### **1️⃣ Assignment**

- 질환명 검색시 API 호출 통해서 검색어 추천 기능 구현
  - 사용자가 입력한 텍스트와 일치하는 부분 볼드처리

⭐️⭐️⭐️⭐️⭐️

### 검색된 결과 문자열에서 "검색한 단어"를 기준으로 split을 하고,

### array를 map으로 반복하면서 split된 부분마다 "검색한 단어"를 삽입하여 bold 처리 하였습니다.

⭐️⭐️⭐️⭐️⭐️

<p align="center">
<img width="537" alt="search" src="https://user-images.githubusercontent.com/74575497/200851310-d8d964fc-5e51-4b17-aca4-211d7f09c8cc.png">
</p>

https://github.com/Wanted-07-team-9/pre-onboarding-7th-3-1-9/blob/bbf1724458dd765687641bed9246447632d70bc6/src/components/blocks/AutoCompleteItem.tsx#L4-L28

#

### **2️⃣ Assignment**

- - 검색어가 없을 시 “검색어 없음” 표출

⭐️⭐️⭐️⭐️⭐️

### 검색된 문자열이 없을경우 검색어 없음 표출하였습니다.

⭐️⭐️⭐️⭐️⭐️

<p align="center">
<img width="528" alt="empty" src="https://user-images.githubusercontent.com/74575497/200851832-41b84cc0-e62e-4d6d-b2ea-9515c94069bc.png">
</p>

https://github.com/Wanted-07-team-9/pre-onboarding-7th-3-1-9/blob/bbf1724458dd765687641bed9246447632d70bc6/src/components/blocks/EmptyResult.tsx#L3-L9
https://github.com/Wanted-07-team-9/pre-onboarding-7th-3-1-9/blob/bbf1724458dd765687641bed9246447632d70bc6/src/pages/Main/AutoComplete/AutoComplete.tsx#L35

#

### **3️⃣ Assignment**

- API 호출 최적화
  - API 호출별로 로컬 캐싱 구현
    - 캐싱 기능을 제공하는 라이브러리 사용 금지(React-Query 등)
    - 캐싱을 어떻게 기술했는지에 대한 내용 README에 기술

⭐️⭐️⭐️⭐️⭐️

### Cache Storage를 사용하여 캐싱 기능을 제공하였습니다.

### Cache Storage에는 queryString을 키값(name)으로 데이터와 etag를 저장합니다.

### API 호출시 Cache Storage에 queryString 값이 존재하면 etag를 header에 포함하여 호출 진행하며,

### response status === 200 이면 받은 response.data를 표출하고, etag와 data 값을 Cache Storage에 저장합니다.

### response status === 304 이면 Cache Storage에서 data 값을 가져와서 표출합니다.

⭐️⭐️⭐️⭐️⭐️

<p align="center">
<img width="420" alt="cache" src="https://user-images.githubusercontent.com/74575497/200842174-e1b72327-5569-4b5e-b7d7-594ec5499587.png">
</p>

https://github.com/Wanted-07-team-9/pre-onboarding-7th-3-1-9/blob/8c6d325032818d697dc2f31b9540ebb32f2c3f1e/src/apis/axiosInstance.ts#L9-L35

#

### **4️⃣ Assignment**

- - 입력마다 API 호출하지 않도록 API 호출 횟수를 줄이는 전략 수립 및 실행
    - README에 전략에 대한 설명 기술

⭐️⭐️⭐️⭐️⭐️

### API 요청에 300ms의 debounce를 적용하였고,

### 사용자의 입력마다 API 호출 하는것이 아닌 사용자의 입력이 해당 시간동안 없을때만 호출하게 하여 횟수를 줄였습니다.

⭐️⭐️⭐️⭐️⭐️

https://github.com/Wanted-07-team-9/pre-onboarding-7th-3-1-9/blob/bbf1724458dd765687641bed9246447632d70bc6/src/hooks/useGetSickItem.ts#L16-L29

#

### **5️⃣ Assignment**

- - API를 호출할 때 마다 `console.info("calling api")` 출력을 통해 콘솔창에서 API 호출 횟수 확인이 가능하도록 설정

⭐️⭐️⭐️⭐️⭐️

### axios instance의 인터셉터에서 request 전에 console.info('calling api'); 를 추가했습니다.

⭐️⭐️⭐️⭐️⭐️

<p align="center">
<img width="384" alt="console" src="https://user-images.githubusercontent.com/74575497/200847063-91f2c08f-9871-4c3c-bac6-6a2dd94a48ba.png">
</p>

https://github.com/Wanted-07-team-9/pre-onboarding-7th-3-1-9/blob/bbf1724458dd765687641bed9246447632d70bc6/src/apis/axiosInstance.ts#L8-L16

#

### **6️⃣ Assignment**

- 키보드만으로 추천 검색어들로 이동 가능하도록 구현
  - 사용법 README에 기술

⭐️⭐️⭐️⭐️⭐️

### 검색창의 input box의 onKeyDown 이벤트에 ArrowDown, ArrowUp 이벤트가 발생했을때 selectIndex값을 변경하였고,

### selectIndex값과 아이템의 index 값이 같으면 over className을 추가하였습니다.

⭐️⭐️⭐️⭐️⭐️

https://github.com/Wanted-07-team-9/pre-onboarding-7th-3-1-9/blob/bbf1724458dd765687641bed9246447632d70bc6/src/pages/Main/SearchBar/index.tsx#L14-L23
https://github.com/Wanted-07-team-9/pre-onboarding-7th-3-1-9/blob/bbf1724458dd765687641bed9246447632d70bc6/src/components/blocks/AutoCompleteItem.tsx#L16-L26

#

### **7️⃣ Assignment**

> (추가 기능)

- isLoading 대신 Suspense 구현

https://github.com/Wanted-07-team-9/pre-onboarding-7th-3-1-9/blob/7b4fb302901a98f2222b5b1f38117d2102005542/src/pages/Main/AutoComplete/index.tsx#L12-L14

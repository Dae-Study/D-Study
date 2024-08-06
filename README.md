# D-Study 작업 현황
## 일자 : 2024년 8월 6일 (화)
<작업중>
kiwi 외 띄어쓰기 라이브러리 적용 가능한 항목 검토 & 우분투 환경이라서 그런지 계속 충돌남 (ㅠㅠ) 
웹페이지 DB connect

## 일자 : 2024년 8월 3일 (토)
### 1. 파일 설명 :

__Labeling__ : Labeling 필요 코드(.py) pakage화 

__1) MongDBconnection__: 

     def DBconnection(DB_name, Col_name, type):__ 몽고DB 데이터베이스의 collection 가져옴

     def MongoDB_Update(df, collection):__ 몽고DB 데이터베이스의 collection 등록함

__2) BadWordFiltering__ : DataFrame에 있는 문장을 검사하여 욕설이 있는 경우 label_1 값을 0, 아니면 1로 표현함

                          1. 문장 비속어 검사 : 구현 완료 

                          2. 형태소 검사 후 공백 제거는  Morpheme classification.py에 구현, 함수로 가져온 결과값을 비속어 검사하도록 수정할 예정 

                          3. 영문, 일본어 제거 : 구현 완료 but 비중 검사의 경우 이수현과 협업 

__3) badWords__ : 나쁜말 모음집 (.txt)  

__4) main__ : 모든 파일 실행 파일

__5) init__ : import문

__5) Morpheme classification__ : 형태소 분류 및 Other(형태소 분류 없음)이 연속된 경우를 비속어로 보고 공백을 제거함



## 8월 4일 작업 예정 :
 1차 라벨링 완료 및 비속어 리스트를 늘리는 것이 중요하다고 생각함, 이부분은 수현이의 자료를 검토할 예정! 웬만하면 1차 라벨링때 다 걸러지면 좋겠다고 생각해 

## 일자 : 2024년 8월 2일 (금)
### 1. 파일 설명 :

__Labeling__ : Labeling 필요 코드(.py) pakage화 

__1) MongDBconnection__: 

     def DBconnection(DB_name, Col_name, type):__ 몽고DB 데이터베이스의 collection 가져옴

     def MongoDB_Update(df, collection):__ 몽고DB 데이터베이스의 collection 등록함

__2) BadWordFiltering__ : DataFrame에 있는 문장을 검사하여 욕설이 있는 경우 label_1 값을 0, 아니면 1로 표현함

                          1. 문장 비속어 검사 : 구현 완료 

                          2. 형태소 검사 후 공백 제거 비속어 검사 (작업중) 

                          3. 영문, 일본어 제거 : 구현 완료 but 비중 검사를 한번 더 적용해야할 것 같음 

__3) badWords__ : 나쁜말 모음집 (.txt)  

__4) main__ : 모든 파일 실행 파일

__5) init__ : import문

__5) 형태소 분류 초안__ : 문제의 작업파일

### 2. 작업 설명 :
형태소 분류하고 공백 제거만하면 1차 라벨링 다 될 것 같은데~~ 
ㅋ1ㅂ는 오픈 소스 적용할 예정
이번 주말까지 완료하는게 목표 


## 일자 : 2024년 7월 31일 (수)
### 1. 파일 설명 : 7월 28일과 동일함 (수정된 것은 추후 업로드)

알파벳의 경우 1차 라벨링 코드 000처리

A,B,C,...,Z 영문의 경우 그 수가 적어서 list 변수로 관리할 예정 (파일이나 DB는 데이터량이 많을때 사용하는 것이 유리)

lsit와 대조하여 영문 발견시 000으로 1차 라벨링 되며 추후 모든 과정에서 제거됨 !!


오늘은 코드 리뷰 위주로 작업! 

### 2. 작업 설명 :   

## 일자 : 2024년 7월 28일 (일)

### 1. 파일 설명 :

__Labeling__ : Labeling 필요 코드(.py) pakage화 

__1) MongDBconnection__: 

     def DBconnection(DB_name, Col_name, type):__ 몽고DB 데이터베이스의 collection 가져옴

     def MongoDB_Update(df, collection):__ 몽고DB 데이터베이스의 collection 등록함

__2) BadWordFiltering__ : DataFrame에 있는 문장을 검사하여 욕설이 있는 경우 label_1 값을 0, 아니면 1로 표현하
                          1. 문장 비속어 검사 2. 공백 제거 비속어 검사

__3) badWords__ : 나쁜말 모음집 (.txt)  

__4) main__ : 모든 파일 실행 파일

__5) init__ : import문


__예외 파일__
__MongoDrop__ :  MongoDB에 있는 Database 삭제 코드  


### 2. 작업 설명 :   

DB 등록, 업데이트 함수 제거

<비속어 검사 절차>
1. 문장 내 비속어 검사후 1차 라벨링 
2. 1번에서 걸러지지 않은 문장 내 공백 제거 후 비속어 검사 후 1차 라벨링 < 수정 필요
3. 2번에서 걸러지지 않은 비1속어 < 1 제거후 비속어 검사 후 1차 라벨링 < 진행중

---


## 일자 : 2024년 7월 25일 (목)

### 1. 파일 설명 :

__1) MongDBconnection__: MongoDB에서 collection을 읽어와 DataFrame으로 변환하는 코드  

__2) BadWordFiltering__ : DataFrame에 있는 문장을 검사하여 욕설이 있는 경우 label_1 값을 0, 아니면 1로 표현하는 코드  

__3) badWords__ : 나쁜말 모음집 (.txt)  

__4) MongoDrop__ :  MongoDB에 있는 Database 삭제 코드  


### 2. 작업 설명 :   

https://github.com/VaneProject/bad-word-filtering?tab=readme-ov-file : 비속어 필터링 깃허브 링크  

해당 링크는 'java'로 기술되엉 있기 때문에 'python'으로 수정하여 욕설이 있는 경우 라벨링하는 코드를 제작


우선 test DataFrame을 만들어 적용했을때 결과는 성공!!  

몽고DB에 있는 df 처리는, 눈깔이 너무 아파서 (인공눈물 4번 넣었는데도) 다음 작업으로 미루겠습니다 미안하다  


---

## 일자 : 2024년 7월 23일 (화)

### 작업 설명 : 
몽고 DB에서 DataFrame으로 파일을 가져온 다음,  

가져온 파일은 라벨링 검사 함수를 통해 <---작업중!!  

DataFrame(df) 끝에 열 label_1을 추가하고 내용의 경우, 속어는 0 비속어는 1로 추가함



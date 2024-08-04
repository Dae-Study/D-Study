# D-Study 작업현황 [윤아]

## Date 8/4
### 1. 파일 설명
#### Seperate_name:
__1) hangul_components: 초성, 중성, 종성 리스트__

__2) Korean_consonants: 각 자음 및 모음마다 자신과 비슷한 발음 또는 사람들이 자주 오타를 내거나 일부러 바꿔쓰는 빈도가 높은 자음 또는 모음으로 리스트 구성__

__3) Test: 이름 변형 감지 알고리즘 코드이고, 아직 구현 중!!__

### 2. 작업 설명:
#### 이전 작업에서 수정된 것:
'김윤아' 이름을 입력받으면 [['ㄱ','ㅣ','ㅁ'],['ㅇ','ㅠ','ㄴ'],['ㅇ','ㅏ','']]로 분리하게 됨

#### 지금 구현 중인 것:
'유우운아' 같은 변형된 이름을 검출하는 알고리즘 테스팅 중이고, Korean_consonents를 사용하는 기능 추가 예정

Korean_consonents를 추가하지 않아서 아직은 유윤아 이런식으로만 추출 가능

## Date 8/2
### 작업 설명:
__이름 변형 알고리즘 구상 및 구현 중__
'김윤아'이름을 입력받으면 [ㄱ,ㅣ,ㅁ,ㅇ,ㅠ,ㄴ,ㅇ,ㅏ]로 출력하도록 함

### 추후 작업 설명:
#### 이름 변형
__1) '김윤아'이면, 김=['ㄱ','ㅣ','ㅁ'], 윤=['ㅇ','ㅠ','ㄴ'], 아=['ㅇ','ㅏ','']로 한 글자씩 나눠서 리스트로 나누기__

__2) lark에 올린 것처럼 이름 변형 유형을 검출할 수 있는 알고리즘 작성__

__3) 윤아 -> 아윤 , 김윤아 -> 윤아김 등 위치가 바뀐 이름에도 적용되도록 알고리즘 작성__

#### 라벨링2_부정+긍정
__1) Kiwi로 형태소 분류 후, 종결형 어미, 관사형 어미로 끝나는 (특히 ~겠냐, ~냐, ~겠다 + ?) 단어를 추출하는 알고리즘 작성 (부정 tag 달아주기)__

__2) (긍정+긍정), (긍정+부정), (부정+긍정)을 긍정 또는 부정 tag로 분류하기__

## Date 7/28
### 1. 파일 설명:

__Section_1~3: 두 단어 비교를 위한 기능을 섹션별로 구상__
1. Section 1: 예시 단어 "뽑다"의 반의어 데이터프레임을 만듬
2. Section 2: 사용자의 이름을 입력하게 한 뒤 이를 고유명사로 처리, 문장에서 Kiwi를 활용해 동사를 추출한 뒤 종결형 어미로 끝나도록 "~다"의 형태로 만듬
3. Sectino 3: 추출된 동사들 중 반의어 리스트에 해당하면 "BAD"로 처리되도록 함 (-> 동사에서 용언(동사 및 형용사)로 수정)

### 2. 작업설명:

#### 현재 진행 중인 작업
부정 + 긍정인 경우 부정적 의미를 담은 문장으로 분류하는 기능 구현

#### 두 단어 비교 기능
#### 수정사항:
1. 이전에 KoBERT로 동사의 관계를 구분하는 것에서 반의어 리스트를 통해 처리하는 방식으로 변경
#### 1. 요구 사항 정리

1. **사용자의 이름을 입력받아 문장 분석 시 고유명사로 처리**
   - 사용자로부터 이름을 입력받고, 형태소 분석 시 해당 이름을 고유명사로 처리하여 분석에 포함.
  
2. **주어진 문장의 형태소를 분석하여 동사 추출**
   - 주어진 문장을 형태소로 분리하고, 동사에 해당하는 형태소를 추출하여 종결형 어미 형태로 변환.
   
3. **동사의 반의어 데이터프레임 생성 및 반의어 체크**
   - 주어진 동사의 반의어를 포함하는 데이터프레임을 생성.
   - 추출된 동사들 중 데이터프레임에서 반의어에 해당하는 단어가 있으면 "BAD"를, 없으면 "GOOD"을 출력.

#### 2. 구현 방법 정리

1. **데이터프레임 생성**
   - 반의어 리스트를 포함하는 데이터프레임을 생성.
   - 예를 들어, '뽑다'라는 단어에 대한 반의어 리스트를 생성하고 이를 데이터프레임으로 저장.

2. **문장 분석 및 동사 추출**
   - `kiwipiepy` 라이브러리를 사용하여 형태소 분석을 수행.
   - 사용자 이름을 입력받아 문장에서 해당 이름을 고유명사로 처리.
   - 문장을 형태소로 분리한 후, 동사에 해당하는 형태소를 추출하여 원형을 종결형 어미 형태로 변환.
   - 동사의 원형이 이미 "다"로 끝나는지 확인하여 중복되지 않도록 처리.

3. **반의어 체크**
   - 추출된 동사들 중 데이터프레임에서 반의어에 해당하는 단어가 있는지 확인.
   - 추출된 동사가 반의어 리스트에 포함된 경우 "BAD", 포함되지 않은 경우 "GOOD"을 출력.

### 예시
- 예시 문장: "정준하는 저때 나갔어야 함. 다른 사람 뽑았으면 더 잘됐을 듯."
- 사용자 이름: "정준하"
- 형태소 분석 결과에서 추출된 동사: '나가다', '뽑다', '되다'
- 반의어 데이터프레임에서 '뽑다'의 반의어로 '나가다'가 포함되어 있으므로 결과는 "BAD" 출력.

### 결론
- 위의 요구 사항을 충족하기 위해, 사용자의 이름을 형태소 분석 시 고유명사로 처리하고, 주어진 문장에서 동사를 추출하여 종결형 어미 형태로 변환. 또한, 생성된 반의어 데이터프레임을 활용하여 추출된 동사들 중 반의어에 해당하는 단어가 있는지 확인하고, 이에 따라 "GOOD" 또는 "BAD"를 출력하는 기능을 구현함. 
- 모든 동사 단어에 해당하는 데이터 프레임을 만들고, 추출된 단어들을 for문으로 자신의 데이터 프레임을 확인하도록 하는 기능을 추가하고자 함.
- 동사에서 ~하다, ~되다 처럼 동사를 보조하는 역할인 "보조동사"는 제외하는 기능을 추가할 예정.

## Date 7/27
### 1.파일 설명:

__1) "BERT문장(동사)의미분석": KoBERT의 문장의 의미 관계성을 분석하는 기능을 이용해 "두 단어의 반대의미 분석"을 구현하고자 함.__

__2) "문장분리기_Kiwi": Kiwipiepy 라이브러리가 띄어쓰기 없는 문장, 오타가 있는 문장 등 대부분의 문장을 잘 분리하고, 형태소까지 분석해줌.__

__3) "두 단어 뜻 비교 구상_초본": KoBERT와 Kiwi를 이용해서 구상__

### 2. 작업설명:

__Kiwi로 형태소를 분석해서 거기에 동사에 해당하는 단어만 선택한 다음(이름과 같은 고유명사는 제외) 이 동사들끼리 반대되는 의미인지 KoBERT를 이용해 분석하려고 했는데, KoBERT가 은근 잘 안돼서 수정 중 ㅜㅜ__

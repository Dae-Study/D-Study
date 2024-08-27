from kiwipiepy import Kiwi
import pandas as pd

# Kiwi 인스턴스 생성
kiwi = Kiwi()

# 예시 문장
texts = ["정준하는 저때 나갔어야 함. 다른 사람 뽑았으면 더 잘됐을 듯.",
         "아니? 이거 아닌데.",
         "너가 해라", 
         "내일 놀러가지롱~~"]

# 모든 문장의 형태소 분석 결과를 저장할 리스트
sentences_all = []

for text in texts:
    sentences = kiwi.split_into_sents(text, return_tokens=True)
    sentences_all.append(sentences)

# 사용자 이름 입력
user_name = input("사용자의 이름을 입력하세요: ")

# 형태소 추출 및 동사 원형 리스트 생성
sentence_vars = {}
verbs = []

# 용언을 추출해서 condjugated_verbs에 저장하는 코드
for i, sentences in enumerate(sentences_all, start=1):
    sentence_vars[f"Sentence{i}"] = [sent.text for sent in sentences]
    print(f"\nSentence{i}:")
    for sent in sentences:
        print(f"  Sentence text: {sent.text}")
        for token in sent.tokens:
            # token.form = 형태소
            if token.form == user_name:
                continue  # 사용자의 이름을 제외
            print(f"    {token.form} ({token.tag})")
            # token(형태소)의 품사가 용언(동사 , 형용사)일 경우 verbs 리스트에 저장
            if token.tag.startswith("VV") or token.tag.startswith("VA"):
                verbs.append(token.lemma)  # 동사의 원형을 사용

# 동사의 원형을 종결형 어미 형태로 변경
conjugated_verbs = [verb if verb.endswith("다") else verb + "다" for verb in verbs]

print("\nExtracted and conjugated verbs:", conjugated_verbs)

# 1. DataFrame 
print("1. DataFrame")
data = {
    '단어': ['뽑다'],
    '반의어': [['나가다', '퇴출하다', '들어가다']]
}
df = pd.DataFrame(data)
print(df)

# 3. 반의어 체크
print("\n3. 반의어 체크")
result = "GOOD"
for verb in conjugated_verbs:
    for antonyms in df['반의어']:
        # 동사 중 반의어 목록에 있으면 BAD를 반환
        if verb in antonyms:
            result = "BAD"
            break
    # 만약 반대되는 단어 쌍이 하나라도 존재한다면 코드 종료
    if result == "BAD":
        break

print("Result:", result)

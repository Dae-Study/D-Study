import pandas as pd
from kiwipiepy import Kiwi

# Kiwi 인스턴스 생성
kiwi = Kiwi()

# 사용자 이름 입력
user_name = input("사용자의 이름을 입력하세요: ")

# 예시 문장
text = "정준하는 저때 나갔어야 함. 다른 사람 뽑았으면 더 잘됐을 듯."

# 문장을 형태소로 분리
sentences = kiwi.split_into_sents(text, return_tokens=True)

# 1. DataFrame
print("1. DataFrame")
data = {
    '단어': ['뽑다'],
    '반의어': [['나가다', '퇴출하다', '들어가다']]
}
df = pd.DataFrame(data)
print(df)

# 2. 단어 추출
print(f"\n2. 단어 추출 (문장 분석 결과, 이름 '{user_name}' 포함):")

# 형태소 추출 및 동사 원형 리스트 생성
sentence_vars = {}
verbs = []
for i, sentence in enumerate(sentences, start=1):
    sentence_vars[f"Sentence{i}"] = sentence.text
    print(f"\nSentence{i}: {sentence.text}")
    for token in sentence.tokens:
        if token.form == user_name:
            continue  # 사용자의 이름을 제외
        print(f"  {token.form} ({token.tag})")
        if token.tag.startswith("VV") or token.tag.startswith("VA"):
            verbs.append(token.lemma)  # 동사의 원형을 사용

# 동사의 원형을 종결형 어미 형태로 변경
conjugated_verbs = [verb if verb.endswith("다") else verb + "다" for verb in verbs]

print("\nExtracted and conjugated verbs:", conjugated_verbs)

# 3. 반의어 체크
print("\n3. 반의어 체크")
result = "GOOD"
for verb in conjugated_verbs:
    for antonyms in df['반의어']:
        if verb in antonyms:
            result = "BAD"
            break
    if result == "BAD":
        break

print("Result:", result)

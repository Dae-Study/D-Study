from kiwipiepy import Kiwi
import pandas as pd

# 1. 사용자에게 이름을 입력받기
user_name = input("이름을 입력하세요: ")

# 2. Kiwi 인스턴스 생성 및 사용자 이름을 고유명사로 추가
kiwi = Kiwi()
kiwi.add_user_word(user_name, "NNP")  # 사용자 이름을 고유명사로 추가
kiwi = Kiwi(typos='basic_with_continual')

# 3. 문장 준비 및 사용자 이름 제외
text = "기린은목이길다정준하가뽑다가좋다정준하가나가다가싫다"
text_without_name = text.replace(user_name, "")  # 사용자 이름 제거

# 4. 문장 분리와 형태소 분석 수행
sentences = kiwi.split_into_sents(text_without_name, return_tokens=True)

# 5. 형태소 분석 결과 출력
print(f"문장 분석 결과 (이름 '{user_name}' 포함):")
for i, sentence in enumerate(sentences, start=1):
    print(f"\nSentence{i}: {sentence.text}")
    for token in sentence.tokens:
        print(f"  {token.form} ({token.tag})")

# 6. 문장 변수에 배분 및 동사 추출
sentence_vars = {}
verbs = []
for i, sentence in enumerate(sentences, start=1):
    sentence_vars[f"Sentence{i}"] = sentence.text
    for token in sentence.tokens:
        if token.tag.startswith("VV") or token.tag.startswith("VA"):
            verbs.append(token.lemma)  # 동사의 원형을 사용

print("\nExtracted verbs:", verbs)

# 7. DataFrame 생성 및 동사에 대한 정보 추가
data = {
    '동사': ['뽑', '나가'],
    '반대': ['GOOD', 'BAD']  # 반대에 대한 예시 데이터
}
df = pd.DataFrame(data)

# 동사들에 대한 반대 정보 확인
print("\nVerb analysis:")
for verb in verbs:
    if verb in df['동사'].values:
        status = df[df['동사'] == verb]['반대'].values[0]
        print(f"Verb: {verb}, Status: {status}")
    else:
        print(f"Verb: {verb}, Status: UNKNOWN")

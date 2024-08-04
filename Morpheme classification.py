import pandas as pd
from kiwipiepy import Kiwi

# Kiwi 초기화
kiwi = Kiwi()

# 형태소 분석 및 품사 태깅 함수
def analyze_text(text):
    tokens = kiwi.tokenize(text)
    labeled_morphemes = []

    for token in tokens:
        morpheme_str = token.form
        morpheme_tag = token.tag

        if morpheme_tag.startswith('N'):
            label = 'Noun'
        elif morpheme_tag.startswith('V'):
            label = 'Verb'
        elif morpheme_tag.startswith('J'):
            label = 'Adjective'
        elif morpheme_tag.startswith('E'):
            label = 'Ending'
        elif morpheme_tag.startswith('P'):
            label = 'Particle'
        else:
            label = 'Other'

        labeled_morphemes.append((morpheme_str, label))

    return labeled_morphemes

# 데이터프레임을 이용한 형태소 분석 작업
def process_dataframe(df, text_column):
    processed_data = []
    no_space_text_data = []

    for text in df[text_column]:
        labeled_morphemes = analyze_text(text)
        processed_data.append(labeled_morphemes)

        # 형태소를 문자열로 변환하고 공백 제거
        no_space_text = ''
        i = 0
        while i < len(labeled_morphemes):
            morpheme, label = labeled_morphemes[i]
            
            if label == 'Other':
                start = i
                # 병합 가능한 연속 'Other' 찾기
                while i < len(labeled_morphemes) and labeled_morphemes[i][1] == 'Other':
                    i += 1
                end = i
                
                # 연속 'Other' 형태소를 병합
                no_space_text += ''.join(morpheme for morpheme, _ in labeled_morphemes[start:end])
                if i < len(labeled_morphemes):
                    no_space_text += ' '  # 다음 형태소와 구분
            else:
                no_space_text += morpheme + ' '
                i += 1
        
        no_space_text_data.append(no_space_text.strip())

    df['processed_text'] = processed_data
    df['Remove_spaces_data'] = no_space_text_data
    return df

# 예제 데이터프레임 생성
data = {'text': ["어떻게 이래", "게 이야"]}
df = pd.DataFrame(data)

# 데이터프레임 처리
processed_df = process_dataframe(df, 'text')
print(processed_df[['text', 'processed_text', 'Remove_spaces_data']])

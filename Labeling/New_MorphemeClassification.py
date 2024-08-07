import pandas as pd
from kiwipiepy import Kiwi
import re

# Kiwi 초기화
kiwi = Kiwi()


import pandas as pd

def analyze_text(text):
    tokens = kiwi.tokenize(text)  # 입력 텍스트를 토큰화합니다
    labeled_morphemes = []  # 형태소와 레이블을 저장할 리스트를 초기화합니다
    idx = 0  # 현재 텍스트의 위치를 나타내는 변수입니다

    while idx < len(text):
        found = False
        
        # 의문사 형태소를 먼저 검사합니다
        for interrogative in ['이래', '이러냐', '이런', '저래']:
            if text.startswith(interrogative, idx):
                labeled_morphemes.append((interrogative, 'Interrogative'))
                idx += len(interrogative)
                found = True
                break
        
        # 주격 조사 형태소를 먼저 검사합니다
        if not found:
            for particle in ['은', '는', '이', '가']:
                if text.startswith(particle, idx):
                    labeled_morphemes.append((particle, 'Particle'))
                    idx += len(particle)
                    found = True
                    break
        
        # 형태소 분석을 수행합니다
        if not found:
            for token in tokens:
                morpheme_str = token.form  # 형태소 문자열을 가져옵니다
                morpheme_tag = token.tag  # 형태소의 태그를 가져옵니다
                
                # 형태소 문자열이 현재 위치에서 찾을 수 있는지 확인합니다
                if text.startswith(morpheme_str, idx):
                    # 형태소 태그에 따라 적절한 레이블을 부여합니다
                    if morpheme_str == '.':
                        label = 'Ending'
                    elif morpheme_str == ',':
                        label = 'Comma'
                    elif morpheme_tag.startswith('N'):
                        label = 'Noun'
                    elif morpheme_tag.startswith('V'):
                        label = 'Verb'
                    elif morpheme_tag.startswith('J'):
                        label = 'Adjective'
                    elif morpheme_tag.startswith('E'):
                        label = 'Ending'
                    elif morpheme_tag.startswith('P'):
                        label = 'Particle'
                    elif morpheme_tag.startswith('M'):
                        label = 'Adverb'
                    else:
                        label = 'Other'
                    
                    # 형태소 문자열이 공백이 아닌 경우
                    if morpheme_str.isspace():
                        labeled_morphemes.append((morpheme_str, 'Space'))
                    else:
                        labeled_morphemes.append((morpheme_str, label))
                    
                    idx += len(morpheme_str)
                    found = True
                    break
        
        if not found:
            # 현재 위치의 문자가 공백이 아니면 'Other'로 태깅합니다
            if not text[idx].isspace():
                labeled_morphemes.append((text[idx], 'Other'))
            else:
                labeled_morphemes.append((text[idx], 'Space'))
            idx += 1

    # 형태소와 레이블을 조합하여 최종 결과를 생성합니다
    final_morphemes = []
    i = 0
    while i < len(labeled_morphemes):
        if i < len(labeled_morphemes) - 1:
            current_morpheme, current_label = labeled_morphemes[i]
            next_morpheme, next_label = labeled_morphemes[i + 1]

            # 명사 + 님 처리
            if current_label == 'Noun' and next_morpheme == '님':
                final_morphemes.append((current_morpheme, 'Noun'))
                final_morphemes.append((next_morpheme, 'Honorific'))
                i += 2
                continue

            # Adverb + Other 결합 처리
            if current_label == 'Adverb' and next_label == 'Other':
                # "안녕하세요"와 같은 경우는 결합하지 않도록 처리
                if len(current_morpheme) + len(next_morpheme) > 2:  # 예를 들어, 길이가 2보다 크면 결합하지 않음
                    final_morphemes.append((current_morpheme, current_label))
                else:
                    combined_str = current_morpheme + next_morpheme
                    final_morphemes.append((combined_str, 'Other'))
                i += 2
                continue
            
            # Noun + Ending 결합 처리
            if current_label == 'Noun' and next_label == 'Ending':
                combined_str = current_morpheme + next_morpheme
                final_morphemes.append((combined_str, 'Noun'))
                i += 2
                continue
            
            # Verb + 야 결합 처리
            if current_label == 'Verb' and next_morpheme == '야':
                combined_str = current_morpheme + next_morpheme
                final_morphemes.append((combined_str, 'VerbOther'))
                i += 2
                continue
        
        final_morphemes.append(labeled_morphemes[i])
        i += 1

    return final_morphemes


def process_morphemes(processed_text):
    i = 0
    final_result = []

    while i < len(processed_text):
        # 현재 형태소와 레이블
        label = processed_text[i][1]
        current_str = processed_text[i][0]
        
        if i < len(processed_text) - 2:
            next_label = processed_text[i + 1][1]
            second_label = processed_text[i + 2][1]
            next_str = processed_text[i + 1][0]
            second_str = processed_text[i + 2][0]

            # 'Other' 형태소가 연속된 경우
            if label == 'Other' and second_label == 'Other' and next_label in ['Space', 'Other']:
                if next_label == 'Space' and next_str == ' ':
                    # 공백이 있는 경우 형태소 통합
                    final_result.append((current_str + second_str, 'Other'))
                    i += 3
                elif next_label == 'Other' and re.fullmatch(r'[1!@]+', next_str):
                    # 특수문자가 연속된 경우 형태소 통합
                    final_result.append((current_str + second_str, 'Other'))
                    i += 3
                else:
                    final_result.append((current_str, label))
                    i += 1
            elif label == 'Other' and next_label == 'Noun':
                # 'Other'가 'Noun'과 연속된 경우
                final_result.append((current_str, label))
                final_result.append(processed_text[i + 1])
                i += 2
            else:
                final_result.append((current_str, label))
                i += 1
        else:
            final_result.append((current_str, label))
            i += 1

    return final_result


def process_dataframe(df):
    # 'text' 열에 대해 analyze_text와 process_morphemes를 호출하여 'final_processed_text' 생성
    df['processed_text'] = df['text'].apply(analyze_text)
    df['final_processed_text'] = df['processed_text'].apply(process_morphemes)
    return df

def concatenate_morphemes(df):
    # 'final_processed_text' 열을 기반으로 형태소를 결합하여 'Remove_text' 생성
    def combine_morphemes(morphemes):
        combined_str = ''.join(morpheme for morpheme, label in morphemes)
        return combined_str
    
    df['Remove_text'] = df['final_processed_text'].apply(combine_morphemes)
    return df


data = {'text': ['어떻게 이래', 'ㅅ1111ㅂ새꺄', 'ㅅ ㅂ', '할 때 A+주세요.']}
df = pd.DataFrame(data)

# 데이터프레임 처리
df = process_dataframe(df)
df = concatenate_morphemes(df)

print(df)
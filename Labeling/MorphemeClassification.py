import pandas as pd
from kiwipiepy import Kiwi
import re

# Kiwi 초기화
kiwi = Kiwi()

# 형태소 분석 및 품사 태깅 함수
def analyze_text(text):
    tokens = kiwi.tokenize(text)
    labeled_morphemes = []
    
    idx = 0  # 현재 텍스트의 위치
    
    for token in tokens:
        morpheme_str = token.form
        morpheme_tag = token.tag
        
        if morpheme_str.isspace():
            # 공백은 형태소로 포함하지 않음
            continue
        
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
        
        # 형태소와 일치하는 원문 텍스트를 찾는다
        if idx < len(text):
            match_index = text.find(morpheme_str, idx)
            
            if match_index != -1:
                # 일치하는 부분이 발견되면 해당 부분을 라벨링
                while idx < match_index:
                    if not text[idx].isspace():
                        labeled_morphemes.append((text[idx], 'Other'))
                    idx += 1
                
                labeled_morphemes.append((text[match_index:match_index+len(morpheme_str)], label))
                idx = match_index + len(morpheme_str)
            else:
                # 형태소가 원문 텍스트에서 발견되지 않으면 'Other'로 처리
                if idx < len(text):
                    if not text[idx].isspace():
                        labeled_morphemes.append((text[idx], 'Other'))
                    idx += 1
    
    # 원문 텍스트에서 남은 부분을 'Other'로 태깅
    while idx < len(text):
        if not text[idx].isspace():
            labeled_morphemes.append((text[idx], 'Other'))
        idx += 1

    return labeled_morphemes

def process_dataframe(df, text_column):
    processed_data = []
    no_space_text_data = []

    for text in df[text_column]:
        labeled_morphemes = analyze_text(text)

        # 기호 제거 및 형태소 병합
        cleaned_morphemes = []
        i = 0
        while i < len(labeled_morphemes):
            morpheme, label = labeled_morphemes[i]

            if label == 'Other':
                # 기호 제거
                cleaned_morpheme = re.sub(r'[1@!]', '', morpheme)
                if cleaned_morpheme:  # 비어있지 않은 경우에만 추가
                    cleaned_morphemes.append((cleaned_morpheme, label))
            else:
                cleaned_morphemes.append((morpheme, label))
                
            i += 1

        # 연속된 'Other' 형태소 병합 (공백 없이)
        no_space_text = ''
        processed_text = ''
        i = 0
        while i < len(cleaned_morphemes):
            morpheme, label = cleaned_morphemes[i]
            
            if label == 'Other':
                start = i
                # 병합 가능한 연속 'Other' 찾기
                while i < len(cleaned_morphemes) and cleaned_morphemes[i][1] == 'Other':
                    i += 1
                end = i
                
                # 연속 'Other' 형태소를 병합 (공백 없이)
                combined_other = ''.join(morpheme for morpheme, _ in cleaned_morphemes[start:end])
                no_space_text += combined_other
                processed_text += f'({combined_other}, Other) '
            else:
                no_space_text += morpheme
                processed_text += f'({morpheme}, {label}) '
                i += 1

        no_space_text_data.append(no_space_text.strip())
        processed_data.append(processed_text.strip())

    df['processed_text'] = processed_data
    df['Remove_spaces_data'] = no_space_text_data
    return df



''' 이전 코드 
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
'''
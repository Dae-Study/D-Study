# process_dataframe.py
import pandas as pd
from analyze_text import analyze_text
from korean_ratio import calculate_korean_ratio

def process_dataframe(df, text_column):
    processed_data = []
    no_space_text_data = []
    korean_ratios = []

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

        # 한국어 비율 계산
        korean_ratio = calculate_korean_ratio(labeled_morphemes)
        korean_ratios.append(korean_ratio)

    df['processed_text'] = processed_data
    df['Remove_spaces_data'] = no_space_text_data
    df['korean_ratio'] = korean_ratios

    # korean_ratio를 소수점 둘째 자리까지 반올림
    df['korean_ratio'] = df['korean_ratio'].round(2)
    return df

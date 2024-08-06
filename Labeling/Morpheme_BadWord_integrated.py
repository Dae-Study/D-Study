from MorphemeClassification import process_dataframe
from BadWordFiltering import BadWordFiltering
import pandas as pd
import re

def contains_foreign_language(text):
    """
    텍스트에 외국어(영어, 일본어)가 포함되어 있는지 확인합니다.

    :param text: 확인할 텍스트.
    :return: 영어 또는 일본어가 포함되어 있으면 True, 그렇지 않으면 False.
    """
    english_regex = re.compile(r'[A-Za-z]')
    japanese_regex = re.compile(r'[\u3040-\u30ff\u31f0-\u31ff\u4e00-\u9faf]')

    if english_regex.search(text):
        return True
    if japanese_regex.search(text):
        return True

    try:
        lang = detect(text)
        if lang in ['en', 'ja']:
            return True
    except:
        return False
    return False

# BadWordFiltering 인스턴스 생성, 비속어 목록 파일 경로를 제공
bad_word_filter = BadWordFiltering(file_path='C:/Users/oben0/Desktop/Git_Local/D-Study/Labeling/badwords.txt')

def check_both(text, bad_word_filter):
    """
    텍스트에 대해 check와 partial_check를 모두 수행하여 비속어를 확인합니다.

    :param text: 비속어를 확인할 텍스트.
    :param bad_word_filter: 비속어 필터링 클래스 인스턴스.
    :return: 비속어가 포함되어 있으면 True, 그렇지 않으면 False.
    """
    return bad_word_filter.check(text) or bad_word_filter.partial_check(text, process_dataframe)

def Labeling_1(df):
    df = process_dataframe(df, 'text')  # 형태소 분석 및 공백 제거 작업을 수행
    df['label_1'] = df.apply(
        lambda row: '000' if contains_foreign_language(row['text']) else
        (0 if check_both(row['text'], bad_word_filter) else 1),
        axis=1
    )
    return df

# 예제 데이터프레임 생성
data = {'text': ["어떻게 이래", "게 이야", "ABC"]}
df = pd.DataFrame(data)

# 데이터프레임 처리 및 라벨링
processed_df = Labeling_1(df)
print(processed_df[['text', 'label_1']])

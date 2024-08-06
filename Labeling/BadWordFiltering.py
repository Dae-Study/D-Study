# BadWordFiltering.py
from __init__ import *
import re
import pandas as pd
from langdetect import detect, DetectorFactory
from MorphemeClassification import process_dataframe


# 언어 감지기의 랜덤성을 제거하여 동일한 결과를 얻도록 설정
DetectorFactory.seed = 0

class BadWordFiltering(set):
    """
    비속어 필터링을 위한 클래스
    """
    def __init__(self, file_path=None):
        """
        클래스 초기화. 비속어 목록을 파일에서 읽어옵니다.

        :param file_path: 비속어 목록이 저장된 파일 경로. 기본값은 None입니다.
        """
        super().__init__()
        if file_path:
            self.load_bad_words(file_path)
        else:
            # 기본 비속어 목록을 직접 추가할 수 있습니다.
            self.update(["badword1", "badword2", "koreaWord1"])

    def load_bad_words(self, file_path):
        """
        파일에서 비속어 목록을 읽어옵니다. 비속어 목록이 ','로 구분되어 있다고 가정합니다.

        :param file_path: 비속어 목록이 저장된 파일 경로.
        """
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                # 파일의 내용을 읽고 ','로 구분하여 비속어 목록을 업데이트합니다.
                content = file.read()
                bad_words = [word.strip() for word in content.split(',') if word.strip()]
                self.update(bad_words)
        except FileNotFoundError:
            print(f"파일을 찾을 수 없습니다: {file_path}")
        except Exception as e:
            print(f"파일을 읽는 중 오류가 발생했습니다: {e}")

    def check(self, text):
        """
        텍스트에 비속어가 포함되어 있는지 확인합니다.

        :param text: 비속어를 확인할 텍스트.
        :return: 텍스트에 비속어가 포함되어 있으면 True, 그렇지 않으면 False.
        """
        text = text.lower()  # 대소문자 구분 없이 비교
        for word in self:
            # 비속어가 부분 문자열로 존재하는지 확인
            if re.search(re.escape(word), text):  # 단순 문자열 매칭
                return True
        return False

    def partial_check(self, text, process_func):
        """
        텍스트에 비속어의 첫 문자가 포함된 경우 형태소 분석 후 공백을 제거한 텍스트에서 비속어가 포함되어 있는지 확인합니다.

        :param text: 비속어를 확인할 텍스트.
        :param process_func: 형태소 분석 및 공백 제거 함수.
        :return: 텍스트에 비속어가 포함되어 있으면 True, 그렇지 않으면 False.
        """
        df = process_func(pd.DataFrame({'text': [text]}), 'text')
        no_space_text = df['Remove_spaces_data'].iloc[0]
        return self.check(no_space_text)


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
    """
    주어진 데이터프레임의 'text' 열에 대해 전처리를 수행하고, 
    비속어 여부와 외국어 포함 여부에 따라 'label_1' 열을 추가합니다.

    :param df: 텍스트 데이터를 포함한 데이터프레임.
    :return: 'label_1' 열이 추가된 데이터프레임.
    """
    df = process_dataframe(df, 'text')  # 형태소 분석 및 공백 제거 작업을 수행
    
    df['label_1'] = df.apply(
        lambda row: '000' if contains_foreign_language(row['text']) else
        (0 if check_both(row['text'], bad_word_filter) else 1),
        axis=1
    )
    return df
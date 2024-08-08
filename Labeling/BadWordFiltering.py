# BadWordFiltering.py
from __init__ import *
import re
import pandas as pd
from langdetect import detect, DetectorFactory
#from New_MorphemeClassification import process_dataframe


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

# BadWordFiltering 인스턴스 생성, 비속어 목록 파일 경로를 제공
bad_word_filter = BadWordFiltering(file_path='C:/Users/oben0/Desktop/Git_Local/D-Study/Labeling/badwords.txt')

def Labeling_1(df):
    """
    df의 '1st_filtering_text' 컬럼을 바탕으로 영어, 일본어, 비속어 여부를 검사하여
    'Label_1' 컬럼에 값을 기록합니다.
    
    :param df: 데이터프레임
    :return: 수정된 데이터프레임
    """
    # 'Label_1' 컬럼을 초기화
    df['Label_1'] = None

    for i, row in df.iterrows():
        text = row['1st_filtering_text']
        ratio = row['ja_en__ratio']

        # 외국어(영어, 일본어)가 60% 이상인 경우
        if ratio >= 0.6:
            df.at[i, 'Label_1'] = '000'
        # 비속어가 포함된 경우
        elif bad_word_filter.check(text):
            df.at[i, 'Label_1'] = '0'
        # 아무 문제 없는 경우
        else:
            df.at[i, 'Label_1'] = '1'

    return df
import pandas as pd
import re

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
           # print(f"비속어 목록: {self}")  # 비속어 목록 출력 (디버깅용)
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
                print(f"비속어 발견: {word} in {text}")  # 디버깅용
                return True
        return False

    def blank_check(self, text):
        """
        공백을 제거한 후 텍스트에 비속어가 포함되어 있는지 확인합니다.

        :param text: 비속어를 확인할 텍스트.
        :return: 공백을 제거한 텍스트에 비속어가 포함되어 있으면 True, 그렇지 않으면 False.
        """
        return self.check(text.replace(" ", ""))


# 샘플 DataFrame 생성
data = {
    'text': [
        'ㅅㅂ 쌔끼야.',
        '치킨 먹고싶다.',
        '개새끼야.',
        '교수님 좋은 말로 할 때 A+주세요.'
    ]
}

df = pd.DataFrame(data)

# BadWordFiltering 인스턴스 생성, 비속어 목록 파일 경로를 제공
bad_word_filter = BadWordFiltering(file_path=r'C:\Users\oben0\Desktop\Git_Test\D-Study\badwords.txt')

# 비속어가 포함된 텍스트를 확인하기 위해 디버깅
def debug_check(text):
    result = bad_word_filter.check(text)
    print(f"텍스트: '{text}'")
    print(f"비속어 포함 여부: {result}")
    return 0 if result else 1

# 각 행을 검사하고 비속어가 포함된 경우 label_1을 0으로 설정
df['label_1'] = df['text'].apply(debug_check)

print(df)


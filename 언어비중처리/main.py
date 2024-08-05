# main.py
import pandas as pd
from process_dataframe import process_dataframe

# 분석할 텍스트 예시
df = pd.DataFrame({'text': ['게 이가', 'Hello World', 'Hello 안녕하세요 반가워요', 'こん 내 이름은 북극곰', 'こんにちは 世界']})

# 데이터프레임 처리
df = process_dataframe(df, 'text')

# 결과 출력
print(df)

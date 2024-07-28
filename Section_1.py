import pandas as pd

# 딕셔너리를 사용한 데이터 프레임 생성
data = {
    '단어': ['뽑다'],
    '반의어': [['나가다', '퇴출하다', '들어가다']]
}

df = pd.DataFrame(data)

print(df)

import pandas as pd

def add_ja_en_combined_ratio(df, label_column='final_processed_text'):
    """
    DataFrame에 일본어(Ja)와 영어(En)의 결합 비율을 계산하여 새로운 열에 저장합니다.
    
    Parameters:
        df (pd.DataFrame): 라벨이 포함된 데이터프레임.
        label_column (str): 라벨이 포함된 열의 이름.
        
    Returns:
        pd.DataFrame: 결합 비율이 추가된 데이터프레임.
    """
    def calculate_combined_ratio(labels):
        # 라벨 리스트에서 Ja와 En 개수 계산
        ja_en_count = sum(1 for _, label in labels if label in ['Ja', 'En'])
        total_labels = len(labels)
        # 비율 계산
        return round(ja_en_count / total_labels, 2) if total_labels > 0 else 0.00
    
    # 각 행에 대해 비율 계산
    df['ja_en__ratio'] = df[label_column].apply(calculate_combined_ratio)
    
    return df

'''
# 예시 데이터프레임 생성
data = {
    'final_processed_text': [
        [('어떻게', 'Adverb'), ('eee', 'En'), ('이래', 'Interrogative')],
        [('ㅅㅂ', 'Other'), ('새꺄', 'Noun')],
        [('ㅅㅂ', 'Other')],
        [('eee', 'En')],
        [('これはテストです', 'Ja')],
        [('게이야', 'Other')]
    ]
}
df = pd.DataFrame(data)

# 함수 호출
df = add_ja_en_combined_ratio(df)

# 결과 출력
print(df)
'''
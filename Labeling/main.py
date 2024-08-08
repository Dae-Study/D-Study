from __init__ import *
import pandas as pd
#from MongDBconnection import *
from BadWordFiltering import Labeling_1
from New_MorphemeClassification import concatenate_morphemes
from New_MorphemeClassification import process_dataframe
from language_weight_test import add_ja_en_combined_ratio


#연결 오류 Why
"""
df, collection = DBconnection('Gang','Min_B',1)
df = pd.DataFrame(df)

#1차 형태소 분리 :  df ['processed_text'] (1차 필터링 전 형태소 ),  df['final_processed_text'] = (1차 필터링 후 형태소)
df = process_dataframe(df)

#1차 필터링된 텍스트 (1차 필터링 후 형태소의 병합 텍스트)
df = concatenate_morphemes(df)

# 영어, 일본어 비중 검사 
df = add_ja_en_combined_ratio(df)

#Labeling 1차 진행 
Labelinng_df = Labeling_1(df)
print(Labelinng_df[['1st_filtering_text','Label_1']])

#업데이트 
MongoDB_Update(Labelinng_df, collection)
"""



#test
df2 = {
    'text': [
        'ㅅㅂ',
        'ㅅ ㅂ',
        'ㅅ1ㅂ',
        'ㅅ1111ㅂ새꺄',
        'ABC',
        '어떻게 이래',
        '게 이야',
        "これはテストです",
        'A+주세요.'
    ]

}
 
df2 = pd.DataFrame(df2)


#1차 형태소 분리 :  df ['processed_text'] (1차 필터링 전 형태소 ),  df['final_processed_text'] = (1차 필터링 후 형태소)
df2 = process_dataframe(df2)

#1차 필터링된 텍스트 (1차 필터링 후 형태소의 병합 텍스트)
df2 = concatenate_morphemes(df2)

# 영어, 일본어 비중 검사 
df2 = add_ja_en_combined_ratio(df2)

#Labeling 1차 진행 
Labelinng_df = Labeling_1(df2)
print(Labelinng_df[['1st_filtering_text','Label_1']])



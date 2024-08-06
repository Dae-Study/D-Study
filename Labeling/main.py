from __init__ import *
import pandas as pd
from BadWordFiltering import Labeling_1
from MongDBconnection import *


#연결
#df, collection = DBconnection('Gang','Min_B',1)

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
        '교수님 좋은 말로 할 때 A+주세요.'
    ]

}
 
df2 = pd.DataFrame(df2)

#Labeling 1차 진행 
Labelinng_df = Labeling_1(df2)
print(Labelinng_df)

#업데이트 
#MongoDB_Update(Labelinng_df, collection)








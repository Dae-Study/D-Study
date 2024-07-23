from pymongo import MongoClient
import pandas as pd  # pandas 라이브러리 임포트
from bson.objectid import ObjectId

# 몽고DB에 연결하는 함수
mongo_uri = 'mongodb+srv://gimyuna:dtw01060@DL-Dragons.gqslqxe.mongodb.net/?retryWrites=true&w=majority'
client = MongoClient(mongo_uri)
db = client.get_database('Gang')  
collection = db['New_A']  

# 데이터 가져오기
data = list(collection.find())
df = pd.DataFrame(data)
print(df.head)

# 라벨링 작업 *작업중*
def label_text(text):
    if "욕설" in text:
        return 1
    else:
        return 0

# text 컬럼에 대해 라벨링 작업 수행
#df['label'] = df['text'].apply(label_text)

# 라벨링 결과 확인
#print(df[['text', 'label']].head())

# MongoDB에 업데이트
#for idx, row in df.iterrows():
 #   collection.update_one(
   #     {"_id": ObjectId(row["_id"])}, 
    #    {"$set": {"label": row["label"]}}
  #  )
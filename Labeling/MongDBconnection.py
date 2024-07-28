from __init__ import *
from pymongo import MongoClient
from bson import ObjectId
import pandas as pd


# 몽고DB에 연결하는 함수
def DBconnection(DB_name, Col_name, type):
    mongo_uri = 'mongodb+srv://gimyuna:dtw01060@DL-Dragons.gqslqxe.mongodb.net/?retryWrites=true&w=majority'
    client = MongoClient(mongo_uri)
    db = client.get_database(DB_name)  
    collection = db[Col_name]
    
    # 데이터 가져오기
    data = list(collection.find())
    df = pd.DataFrame(data)
    #print(df.head())

    if type==1:
        return df, collection
    if type==2:
        return df

# 몽고DB에 업로드하는 함수 
def MongoDB_Update(df, collection):
# MongoDB에 업데이트
    for idx, row in df.iterrows():
        # _id가 ObjectId 객체인지 확인하고 변환
        object_id = row["_id"] if isinstance(row["_id"], ObjectId) else ObjectId(row["_id"])
        collection.update_one(
         {"_id": object_id}, 
            {"$set": {"label_1": row["label_1"]}}
        )


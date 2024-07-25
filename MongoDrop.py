from pymongo import MongoClient
import pandas as pd  # pandas 라이브러리 임포트
from bson.objectid import ObjectId

# 몽고DB에 연결하는 함수
mongo_uri = 'mongodb+srv://gimyuna:dtw01060@DL-Dragons.gqslqxe.mongodb.net/?retryWrites=true&w=majority'
client = MongoClient(mongo_uri)
db = client["TEST"]
client.drop_database("TEST")
print("데이터베이스가 삭제되었습니다.")
from __init__ import *
from pymongo import MongoClient
from bson import ObjectId
import pandas as pd


def DBconnection(DB_name, Col_name, type):
    mongo_uri = "mongodb+srv://gimyuna:dtw01060@dl-dragons.gqslqxe.mongodb.net/?retryWrites=true&w=majority&appName=DL-Dragons"
    try:
        client = MongoClient(mongo_uri)
        db = client.get_database(DB_name)  
        collection = db[Col_name]
        
        # 데이터 가져오기
        data = list(collection.find())
        df = pd.DataFrame(data)
        
        if type == 1:
            return df, collection
        if type == 2:
            return df
    except Exception as e:
        print(f"An error occurred while connecting to the database: {e}")


try:
    df, collection = DBconnection('Gang', 'Min_A', 1)
except Exception as e:
    print(f"An error occurred: {e}")

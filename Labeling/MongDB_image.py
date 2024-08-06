from pymongo import MongoClient
from gridfs import GridFS

# 몽고DB에 연결하는 함수
def DBconnection(DB_name, Col_name):
    mongo_uri = 'mongodb+srv://gimyuna:dtw01060@DL-Dragons.gqslqxe.mongodb.net/?retryWrites=true&w=majority'
    client = MongoClient(mongo_uri)
    db = client.get_database(DB_name)
    collection = db[Col_name]
    return collection

# 이미지 업로드 함수
def upload_image_to_mongodb(image_path, db_name, collection_name):
    # MongoDB에 연결
    collection = DBconnection(db_name, collection_name)
    fs = GridFS(collection)
    
    # 이미지 파일을 읽어서 GridFS에 업로드
    with open(image_path, 'rb') as image_file:
        file_id = fs.put(image_file, filename=image_path)
        
    print(f"Uploaded image with file ID: {file_id}")
    return file_id
from pymongo import MongoClient
from pymongo.errors import ServerSelectionTimeoutError

# MongoDB 클러스터 URI
uri = 'mongodb+srv://gimyuna:dtw01060@DL-Dragons.gqslqxe.mongodb.net/?retryWrites=true&w=majority'

try:
    # MongoDB 클라이언트 생성
    client = MongoClient(uri, serverSelectionTimeoutMS=5000)  # 5초 동안 서버 선택 시도
    # 데이터베이스에 연결 시도
    db = client.DJ_girl  # 'test'는 사용할 데이터베이스 이름입니다.
    
    # 데이터베이스에 실제로 접근할 수 있는지 확인
    client.admin.command('ping')
    print("MongoDB에 연결되었습니다.")
except ServerSelectionTimeoutError as e:
    print(f"MongoDB 연결 실패: {e}")

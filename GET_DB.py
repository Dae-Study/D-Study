from pymongo import MongoClient
from kiwipiepy import Kiwi

# MongoDB에 연결하는 함수
def connect_to_MongoDB(mongo_uri):
    try:
        # MongoClient에 ssl 매개변수 전달
        client = MongoClient(mongo_uri, tls=True, tlsAllowInvalidCertificates=True)
        print("연결 성공")
    except Exception as e:
        print(f"오류 발생: {e}")
        client = None
    return client

# MongoDB에 있는 DB 및 collections를 가져오는 함수
def get_db_collections(mongo_uri):
    client = connect_to_MongoDB(mongo_uri)
    if client is None:
        return None

    # DB 목록 딕셔너리
    DB_collections = {}
    database_names = client.list_database_names()

    for db_name in database_names:
        db = client[db_name]
        collection_names = db.list_collection_names()
        DB_collections[db_name] = collection_names

    client.close()  # 사용 후 클라이언트 연결 종료
    return DB_collections

# 각 collections 에서 댓글을 가져오는 함수
def get_comments(mongo_uri):
    client = connect_to_MongoDB(mongo_uri)
    if client is None:
        return []

    # 불러온 댓글 저장 딕셔너리
    comments = []

    # DB와 collection을 불러온다
    DB_collections = get_db_collections(mongo_uri)

    if DB_collections is None:
        client.close()
        return []

    for db_name, collection_names in DB_collections.items():
        db = client[db_name]
        for collection_name in collection_names:
            collection = db[collection_name]
            for comment in collection.find():
                comments.append(comment)
    for i in comments:
        print(i)

    client.close()  # 사용 후 클라이언트 연결 종료
    return comments

# 각 컬렉션에서 데이터(댓글)를 가져오는 함수
def analyze_comments(mongo_uri):
    client = connect_to_MongoDB(mongo_uri)
    if client is None:
        return {}

    # Kiwi 인스턴스 생성
    kiwi = Kiwi()

    # 동사와 형용사 추출 및 카운트 저장 딕셔너리
    V_counter = {}

    # 댓글을 불러온다
    comments = get_comments(mongo_uri)

    for comment in comments:
        text = comment.get('text')
        # 만약 text가 없다면 건너뛰기
        if not text:
            continue
                
        sentences = kiwi.split_into_sents(text, return_tokens=True)  # 형태소 분석
        for sentence in sentences:
            for token in sentence.tokens:
                # 동사와 형용사 검출
                if token.tag.startswith("VV") or token.tag.startswith("VA"):
                    if token.form in V_counter:  # 이미 딕셔너리에 있는 단어인지 확인
                        V_counter[token.form] += 1  # 카운트 증가
                    else:
                        V_counter[token.form] = 1  # 새로운 단어이면 추가하고 카운트를 1로 설정

    return V_counter

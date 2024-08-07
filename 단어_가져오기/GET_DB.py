from pymongo import MongoClient
import ssl
from kiwipiepy import Kiwi

def get_db_collections(mongo_uri):

    try:
        # MongoClient에 ssl 매개변수 전달
        client = MongoClient(mongo_uri, tls=True, tlsAllowInvalidCertificates=True)
        print("get_db_collections 연결성공")
    except Exception as e:
        print(f"오류 발생: {e}")

    DB_collections = {}
    database_names = client.list_database_names()

    for db_name in database_names:
        db = client[db_name]
        collection_names = db.list_collection_names()
        DB_collections[db_name] = collection_names

    return DB_collections

def get_comments(mongo_uri):
    try:
        # MongoClient에 ssl 매개변수 전달
        client = MongoClient(mongo_uri, tls=True, tlsAllowInvalidCertificates=True)
        print("get_comments 연결성공")
    except Exception as e:
        print(f"오류 발생: {e}")

    # Kiwi 인스턴스 생성
    kiwi = Kiwi()

    # 동사와 형용사 추출 및 카운트 저장 딕셔너리
    V_counter = {}

    DB_collection = get_db_collections(mongo_uri)

    for db_name, collection_names in DB_collection.items():
        db = client[db_name]
        for collection_name in collection_names:
            collection = db[collection_name]
            comments = collection.find()
            #print("컬렉션 연결")

            # 각 댓글에 대해 동사와 형용사 추출
            for comment in comments:
                text = comment.get('text')
                if not text:
                    continue

                # print(text)
                
                sentences = kiwi.split_into_sents(text, return_tokens=True) # 형태소 분석
                for i, sentence in enumerate(sentences, start=1):
                    for token in sentence.tokens:
                        # 동사와 형용사 검출
                        if token.tag.startswith("VV") or token.tag.startswith("VA"):
                            if token.form in V_counter: # 이미 딕셔너리에 있는 단어인지 확인
                                V_counter[token.form] += 1 # 카운트 증가
                            else:
                                V_counter[token.form] = 1 # 새로운 단어이면 추가하고 카운트를 1로 설정
    
    return V_counter
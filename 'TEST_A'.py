from youtube_comment_downloader import YoutubeCommentDownloader
from pymongo import MongoClient

def get_youtube_comments(video_id):
    comments = []
    downloader = YoutubeCommentDownloader()
    
    for comment in downloader.get_comments(video_id):
        comments.append(comment)
    
    return comments

# 몽고DB에 연결하는 함수
def connect_to_mongo(uri):
    client = MongoClient(uri)
    db = client.get_database()  # 기본 데이터베이스 선택
    collection = db['youtube_comments']  # 사용할 컬렉션 선택
    return collection

# MongoDB에 댓글 저장하는 함수
def save_comments_to_mongo(comments, collection):
    # Insert comments into the MongoDB collection
    collection.insert_many(comments)

# 댓글을 가져올 유튜브 비디오 ID를 지정합니다.
video_id = '-DmixSHLIn0'  # 예시 비디오 ID
comments = get_youtube_comments(video_id)

# MongoDB Atlas 클러스터의 연결 문자열 (URI)
mongo_uri = 'mongodb+srv://gimyuna:TckKBp&QsADUHr6@dl-dragons.gqslqxe.mongodb.net/?retryWrites=true&w=majority'

# MongoDB에 연결하여 컬렉션을 가져옵니다.
collection = connect_to_mongo(mongo_uri)

# 가져온 댓글을 MongoDB 컬렉션에 저장합니다.
save_comments_to_mongo(comments, collection)

print(f"Comments have been saved to MongoDB collection '{collection.name}'")
from 단어_추출 import get_comments  # 함수가 정의된 모듈을 임포트

mongo_uri = "mongodb+srv://gimyuna:dtw01060D@dl-dragons.gqslqxe.mongodb.net/?retryWrites=true&w=majority"

# get_comments 함수를 호출하여 V_counter를 얻음
V_counter = get_comments(mongo_uri)

# V_counter의 예시 항목 몇 개를 출력
for word, count in V_counter.items():  # 상위 10개의 항목만 출력
    print(f"{word}: {count}")
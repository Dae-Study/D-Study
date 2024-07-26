const { MongoClient } = require('mongodb');

// MongoDB Atlas 접속 문자열 (본인의 접속 문자열로 바꿔주세요)
const uri = 'mongodb+srv://gimyuna:dtw01060@DL-Dragons.gqslqxe.mongodb.net/?retryWrites=true&w=majority';

// MongoDB 클라이언트 생성
const client = new MongoClient(uri);

async function run() {
    try {
        // MongoDB 클라이언트 연결
        console.log('MongoDB 클라이언트 연결 시도 중...');
        await client.connect();
        console.log('MongoDB 클라우드에 연결되었습니다.');

        // 데이터베이스 및 컬렉션 선택
        const database = client.db('Gang');
        const collection = database.collection('New_A');

        // 모든 문서 조회 예시
        const cursor = collection.find({});
        const results = await cursor.toArray();

        // 조회된 문서 출력
        console.log('조회된 문서들:');
        results.forEach((doc, idx) => {
            console.log(`${idx + 1}:`, doc);
        });

    } 
    catch (err) {
        console.error('오류 발생:', err);
    }
    finally {
        // MongoDB 클라이언트 연결 닫기
        await client.close();
        console.log('MongoDB 클라이언트 연결이 닫혔습니다.');
    }
    
}

// 연결 함수 실행
run().catch(console.error);

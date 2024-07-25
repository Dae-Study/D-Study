const { MongoClient } = require('mongodb');

// MongoDB Atlas 접속 문자열 (본인의 접속 문자열로 바꿔주세요)
const uri = 'mongodb+srv://gimyuna:dtw01060@DL-Dragons.gqslqxe.mongodb.net/?retryWrites=true&w=majority';

// MongoDB 클라이언트 생성
const client = new MongoClient(uri, { useNewUrlParser: true, useUnifiedTopology: true });

async function run() {
    try {
        // MongoDB 클라이언트 연결
        await client.connect();
        console.log('MongoDB 클라우드에 연결되었습니다.');

        // 데이터베이스 및 컬렉션 선택
        const database = client.db('Gang');
        const collection = database.collection('New_A');

        // 새로운 문서 삽입 예시
        //const insertResult = await collection.insertOne({ name: 'John Doe', age: 30 });
        //console.log('새로운 문서가 삽입되었습니다:', insertResult.insertedId);

        // 문서 조회 예시
        //const findResult = await collection.findOne({ name: 'John Doe' });
        //console.log('조회된 문서:', findResult);

    } finally {
        // MongoDB 클라이언트 연결 닫기
        await client.close();
    }
}

// 연결 함수 실행
run().catch(console.error);

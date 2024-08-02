const express = require('express');
const { MongoClient } = require('mongodb');
const path = require('path');
const app = express();
const port = 3002; // 포트 번호

// MongoDB 연결 문자열
const uri = 'mongodb+srv://gimyuna:dtw01060@DL-Dragons.gqslqxe.mongodb.net/?retryWrites=true&w=majority';

const client = new MongoClient(uri, {
    tlsAllowInvalidCertificates: true,
    tlsAllowInvalidHostnames: true
});

// 정적 파일 제공
app.use(express.static(path.join(__dirname, '..'))); // 루트 경로를 정적 파일의 기본 경로로 설정

app.get('/data', async (req, res) => {
    try {
        await client.connect();
        const database = client.db('Gang');
        const collection = database.collection('New_A');
        const results = await collection.find({}).toArray();
        res.json(results);
    } catch (err) {
        res.status(500).send('데이터를 가져오는 데 오류가 발생했습니다.');
    } finally {
        await client.close();
    }
});

app.listen(port, () => {
    console.log(`서버가 http://localhost:${port}에서 실행 중입니다.`);
});

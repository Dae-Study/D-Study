import webbrowser
from flask import Flask, render_template
import threading
import time
import os

app = Flask(__name__, template_folder='templates')

@app.route('/')
def home():
    return render_template('user.html')

@app.route('/search')
def search():
    return render_template('search.html')

@app.route('/sidebar')
def iframe_page():
    return render_template('sidebar.html')

@app.route('/filtering')
def filtering():
    return render_template('filtering.html')

@app.route('/compare')
def compare():
    return render_template('compare.html')

@app.route('/report')
def report():
    return render_template('report.html')

def open_browser():
    # 환경 변수를 사용하여 브라우저 열기 로직이 이미 실행되었는지 확인
    if os.getenv('BROWSER_OPENED') != 'true':
        time.sleep(5)  # 서버가 완전히 시작되도록 대기
        webbrowser.open('http://127.0.0.1:5001/')
        os.environ['BROWSER_OPENED'] = 'true'

if __name__ == '__main__':
    # 브라우저 열기 로직을 한 번만 실행하도록 보장
    threading.Thread(target=open_browser).start()
    app.run(port=5001, debug=False)  # 디버그 모드 비활성화

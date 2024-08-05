# analyze_text.py
def analyze_text(text):
    # 이 함수는 실제로는 형태소 분석을 해야 하지만, 예시로 각 단어를 'Other'로 라벨링
    return [(morpheme, 'Other') for morpheme in text.split()]

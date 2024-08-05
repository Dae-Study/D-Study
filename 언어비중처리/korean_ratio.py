# korean_ratio.py
from language_detection import detect_language

def calculate_korean_ratio(processed_text):
    """
    Calculate the percentage of Korean morphemes in the given processed text.
    
    Parameters:
    - processed_text (list of tuples): Each tuple contains (morpheme, label).
    
    Returns:
    - float: Percentage of Korean morphemes among 'Other' labeled morphemes.
    """
    # 'Other'로 레이블된 형태소만 필터링
    other_morphemes = [morpheme for morpheme, label in processed_text if label == 'Other']
    
    # 'Other' 형태소가 없는 경우 비율을 0으로 반환
    if not other_morphemes:
        return 0.0
    
    # 총 'Other' 형태소의 개수
    total_count = len(other_morphemes)
    
    # 한국어 형태소의 가중치 합계 계산
    korean_weight = sum(detect_language(morpheme) for morpheme in other_morphemes)
    
    # 한국어 비율 계산 및 소수점 둘째 자리까지 반올림
    korean_ratio = round((korean_weight / total_count) * 100, 2)  # 퍼센트 형식으로 변환
    
    return korean_ratio

import re

def detect_language(text):
    """
    Detect the language of the given text and assign weight based on language.
    
    Parameters:
    - text (str): The text to be analyzed.
    
    Returns:
    - float: Weight of the text (1.0 for Korean, 0.0 otherwise).
    """
    if re.search(r'[ㄱ-ㅎㅏ-ㅣ가-힣]', text):
        return 1.0  # 한국어일 경우 가중치 1.0
    return 0.0  # 한국어가 아닌 경우 가중치 0.0

from kiwipiepy import Kiwi

# Kiwi 객체 생성
kiwi = Kiwi()

def analyze_text(text):
    # 형태소 분석 및 품사 태깅
    print(kiwi.tag(text))
    tags = kiwi.tag(text)
    
    labeled_morphemes = []
    
    for morpheme, tag in tags:
        # 형태소와 태그 추출
        morpheme_str = morpheme
        morpheme_tag = tag
        
        # 형태소 라벨링
        if morpheme_tag.startswith('N'):
            label = 'Noun'  # 명사
        elif morpheme_tag.startswith('V'):
            label = 'Verb'  # 동사
        elif morpheme_tag.startswith('J'):
            label = 'Adjective'  # 형용사
        elif morpheme_tag.startswith('E'):
            label = 'Ending'  # 어미
        elif morpheme_tag.startswith('P'):
            label = 'Particle'  # 조사
        else:
            label = 'Other'  # 기타
        
        labeled_morphemes.append((morpheme_str, label))
    
    return labeled_morphemes

# 테스트 문장
text1 = "어떻게 이래"
text2 = "게 이야"

print("어떻게 이래 형태소 분석 결과:")
morphemes = analyze_text(text1)
for morpheme, label in morphemes:
    print(f"{morpheme}: {label}")

print("\n게 이야 형태소 분석 결과:")
morphemes = analyze_text(text2)
for morpheme, label in morphemes:
    print(f"{morpheme}: {label}")

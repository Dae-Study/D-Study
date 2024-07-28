from kiwipiepy import Kiwi

# Kiwi 인스턴스 생성
kiwi = Kiwi()

# 분석할 텍스트
text = "전 애초에 한숨봇 플로우를 별로 안좋아함 자신의 전문 분야에서 비전문가를 깔보고 무시하는 등 여기는 트위터리안 감성의 절정 이과한숨봇까지는 모두가 아는 상식정도를 올렸으니까 그렇다 쳐 예체능도 좀 갈수록 산으로 가는듯 얘들아 친구 좀 사겨봐"

# 문장 분리
sentences = kiwi.split_into_sents(text)

# 분리된 문장 출력
for sentence in sentences:
    print(sentence.text)
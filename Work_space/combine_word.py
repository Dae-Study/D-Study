from kiwipiepy import Kiwi
from hangul_components import JAUM, MOUM

kiwi = Kiwi(typos='continual')

text = "안ㄴㅕㅇ하ㅏㅏ셍요 ㅅ111ㅂ 개ㅅㄲ야 안돼 저리가야해 '이런' 저런,, ~! ㅅ@ㅂ"
sentences = kiwi.split_into_sents(text, return_tokens=True)

split_text = []

word_split = text.split()

# 텍스트를 형태소 단위로 나누어 리스트로 저장
for sentence in sentences:
    for tokens in sentence.tokens:
        form = tokens.form
        tag = tokens.tag

        # 특수문자는 한 글자씩 분리해서 추가
        if tag.startswith('S'):
            for i in form:
                split_text.append((i, tag))
            continue
        
        split_text.append((form, tag))

print(split_text)

text_length = len(split_text)

def get_next(now_text, index, text_length):
    next_form, next_tag = None, None

    next = (next_form, next_tag)

    # 문장의 마지막 요소가 아닐 경우
    if index < text_length - 1:
        if text[index+1] != None:
            next_form, next_tag = split_text[index+1]
            next = (next_form, next_tag)

    return next

# 결합된 문장을 저장할 리스트
combined_text = []
right_point = 0
JAUM_list = []
complete_text = []

# 자음과 모음을 결합하여 문장을 재구성하는 함수
def combine_word(now, next, index):
    global right_point, JAUM_list

    now_form = now[0]
    next_form = next[0]

    if now_form in JAUM:
        print("now is 자음")
        right_point = index
        if (next[1] == None) or (not next[1].startswith('S')):
            return
        elif next_form in JAUM:
            JAUM_list = now_form + next_form
            i = get_next(next, index+1, text_length)
            i_form = i[1]
            while i_form in JAUM:
                JAUM_list+=i_form
                i = get_next(next, index+1, next_form)
                i_form = i[1]
            combined_text.append(JAUM_list)
        else:
            if next_form in JAUM:
                print("next is 자음")
            elif next_form in MOUM:
                print("next is 모음")
                right_point+=1
                n_next = get_next(next, index+1, text_length)
                n_next_form = n_next[0]
                if (next[1] == None) or (not next[1].startswith('S')):
                    print("now + next (자음 + 모음)까지 저장")
                    combined_text.append(now_form + next_form)
                else:
                    if n_next_form in MOUM:
                        right_point+=1
                        print("n_next is 모음")
                        print("now + next (자음 + 모음)까지 저장")
                        combined_text.append(now_form + next_form)
                    elif n_next_form in JAUM:
                        print("n_next is 자음")
                        nn_next = get_next(n_next, index+2, text_length)
                        nn_next_form = nn_next[0]
                        if (nn_next[1] == None) or (not nn_next[1].startswith('S')):
                            right_point+=1
                            print("now + next + n_next (자음 + 모음 + 자음)까지 저장")
                            combined_text.append(now_form + next_form + n_next_form)
                        else:
                            if nn_next_form in MOUM:
                                print("now + next (자음 + 모음)까지 저장")
                                combined_text.append(now_form + next_form)
                            elif nn_next_form in JAUM:
                                right_point+=1
                                print("nn_next is 자음")
                                print("now + next + n_next (자음 + 모음 + 자음)까지 저장")
                                combined_text.append(now_form + next_form + n_next_form)
                            else:
                                return
                    else:
                        return
            else:
                return
    else:
        return

    
for index, word in enumerate(split_text):
    if index < right_point:
        continue
    next = get_next(word, index, text_length)
    #print(word)
    if not word[1].startswith('S'):
        # print("OOH") 작동확인
        combined_text.append(word[0])
        continue
    combine_word(word, next, index)

# 결과 출력
print(''.join(combined_text))
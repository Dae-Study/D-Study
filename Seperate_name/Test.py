import unicodedata
from hangul_components import CHOSUNG_LIST, JUNGSUNG_LIST, JONGSUNG_LIST

BASE_CODE, CHOSUNG, JUNJONG = 44032, 588, 28

name_list = []
syntax_list = []
save = 0
count_s, count_n = 0, 0

text = "유유윤아는 천재"

user_name = input("이름을 입력하세요: ")
print(f"입력된 이름 {user_name}")

def Seperate_name(char):
    if '가' <= char <= '힣':  # 한글 음절인지 확인
        code = ord(char) - BASE_CODE
        chosung = code // CHOSUNG
        jungsung = (code % CHOSUNG) // JUNJONG
        jongsung = code % JUNJONG
        return CHOSUNG_LIST[chosung], JUNGSUNG_LIST[jungsung], JONGSUNG_LIST[jongsung]
    else:
        return '', '', ''

for char in user_name:
    name_list.append(Seperate_name(char))

print(name_list)

for char in text:
    result = Seperate_name(char)
    if result != ('', '', ''):
        syntax_list.append(result)

print(syntax_list)

for index_n in name_list:
    count_n = 0
    for symbol_n in index_n:
        count_n += 1
        for index_s_idx, index_s in enumerate(syntax_list):
            count_s = 0
            for symbol_s_idx, symbol_s in enumerate(index_s):
                count_s += 1
                if count_n != 3:
                    if count_n == count_s:
                        if symbol_n == symbol_s:
                            save = 1
                            break  # 가장 가까운 루프(여기서는 symbol_s 루프)를 탈출
                        else:
                            continue  # 다음 루프로 진행
                else:
                    if count_s == 1:
                        if symbol_s != 'ㅇ':
                            save = 0
                            break  # 가장 가까운 루프(여기서는 symbol_s 루프)를 탈출
                        else:
                            save = 1
                    elif count_s == 2:
                        S = index_n[1]
                        if symbol_s != S:
                            save = 0
                            break  # 가장 가까운 루프(여기서는 symbol_s 루프)를 탈출
                        else:
                            save = 1
                    else:
                        if symbol_n == symbol_s:
                            save = 1
                        else:
                            save = 0
                        break  # 가장 가까운 루프(여기서는 symbol_s 루프)를 탈출
            if save == 1:
                break  # symbol_s 루프 탈출 후 index_s 루프도 탈출
print(save)
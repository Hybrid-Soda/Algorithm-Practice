# 2607 비슷한 단어 / 구현, 문자열

n = int(input())
init_word = input()
ans = 0

for _ in range(n-1):
    dupl_word = init_word
    word = input()
    cnt = 0

    for w in word:
        # 문자가 단어에 있으면 그 문자를 제거
        if w in dupl_word:
            dupl_word = dupl_word.replace(w, '', 1)
        # 문자가 단어에 없으면 카운트
        else:
            cnt += 1
    
    if cnt <= 1 and len(dupl_word) <= 1:
        ans += 1

print(ans)

# 문제의 조건에 맞는 최소한의 자료구조 사용
# 문자 비교가 필요한 경우라면 딕셔너리보다는 문자열 메서드나 리스트가 더 간결함
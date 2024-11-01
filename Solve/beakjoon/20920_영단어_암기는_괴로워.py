# 20920 영단어 암기는 괴로워 / 자료 구조, 문자열, 정렬, 해시를 사용한 집합과 맵, 트리를 사용한 집합과 맵

N, M = map(int, input().split())
words = {}

for _ in range(N):
    word = input()
    if len(word) >= M:
        words[word] = words.setdefault(word, 0) + 1

sorted_words = sorted(words.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))

for word, _ in sorted_words:
    print(word)

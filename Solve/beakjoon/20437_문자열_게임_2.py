# 20437 문자열 게임 2

for _ in range(int(input())):
    w = input()
    k = int(input())

    char_dict = {}

    for i, char in enumerate(w):
        char_dict[char] = char_dict.get(char, []) + [i]

    min_char = 100000
    max_char = -1

    for idx_list in char_dict.values():
        len_idx_list = len(idx_list)

        if len_idx_list < k:
            continue

        for i in range(len_idx_list - k + 1):
            len_of_char = idx_list[i + k - 1] - idx_list[i] + 1
            min_char = min(min_char, len_of_char)
            max_char = max(max_char, len_of_char)

    if max_char != -1:
        print(min_char, max_char)
    else:
        print(-1)

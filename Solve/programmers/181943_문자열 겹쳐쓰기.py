def solution(my_string, overwrite_string, s):
    answer = list(my_string)
    for i in range(len(overwrite_string)):
        answer[s + i] = overwrite_string[i]
    return ''.join(answer)
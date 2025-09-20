def solution(array, commands):
    answer = []

    for i, j, k in commands:
        part = array[i-1: j]
        answer.append(sorted(part)[k-1])
    
    return answer
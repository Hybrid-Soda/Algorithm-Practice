def solution(n, lost, reserve):
    answer = n - len(lost)
    stud = [0] * (n+2)

    for l in lost:
        stud[l] -= 1
    
    for r in reserve:
        stud[r] += 1
        if stud[r] == 0:
            answer += 1

    for i in range(1, n+1):
        if stud[i] == -1:
            if stud[i-1] == 1:
                stud[i-1] -= 1
                answer += 1
            elif stud[i+1] == 1:
                stud[i+1] -= 1
                answer += 1

    return answer
def solution(n, times):
    answer = n * min(times)
    l, r = 1, n * min(times)

    while l <= r:
        m = (l + r) // 2
        total = sum(m // t for t in times)

        if total < n:
            l = m+1
        else:
            answer = min(answer, m)
            r = m-1

    return answer

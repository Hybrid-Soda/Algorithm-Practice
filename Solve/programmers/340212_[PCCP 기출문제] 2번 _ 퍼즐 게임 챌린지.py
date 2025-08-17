def solution(diffs, times, limit):
    answer = float('inf')
    l, r = 1, max(diffs)
    
    # 이분탐색
    while l <= r:
        level = (l + r) // 2
        time = get_time([0]+diffs, [0]+times, level)

        if time > limit:
            l = level + 1
        else:
            r = level - 1
            answer = min(answer, level)
    
    return answer

def get_time(diffs, times, level):
    total_time = 0

    for i in range(1, len(diffs)):
        term = max(0, diffs[i] - level)
        total_time += (times[i] + times[i-1]) * term + times[i]
    
    return total_time
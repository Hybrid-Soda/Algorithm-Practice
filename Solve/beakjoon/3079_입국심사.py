# 3079 입국심사 / 이분 탐색, 매개 변수 탐색

def binary_search(m: int, times: list[int]):
    min_time, max_time = times[0], m * times[-1]
    answer = float('inf')

    while min_time <= max_time:
        mid_time = (min_time + max_time) // 2
        cnt_temp = 0
        
        # 중간 시간 동안 처리할 수 있는 인원 수 계산
        for time in times:
            cnt_temp += mid_time // time

        # 처리할 수 있는 인원 수가 m 이상이면 시간을 줄인다
        if cnt_temp >= m:
            max_time = mid_time - 1
            answer = min(answer, mid_time)
        # 처리할 수 있는 인원 수가 m 미만이면 시간을 늘린다
        else:
            min_time = mid_time + 1

    return answer

n, m = map(int, input().split())
times = sorted(int(input()) for _ in range(n))
print(binary_search(m, times))

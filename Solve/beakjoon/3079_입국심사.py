# 3079 입국심사

import sys
input = sys.stdin.readline


def confirm(m: int, times: list[int], cutline: int):
    for time in times:
        if time <= cutline:
            m -= cutline // time
        else:
            break
    print('m:', m)
    return m


def binary_search(m: int, times: list[int]):
    min_time, max_time = 1, m * max(times)

    while min_time <= max_time:
        mid_time = (min_time + max_time) // 2
        print(mid_time)
        res = confirm(m, times, mid_time)

        if res > 0:
            max_time = mid_time - 1
        elif res < 0:
            min_time = mid_time + 1
        else:
            return mid_time

    return max_time

n, m = map(int, input().split())
times = sorted(int(input()) for _ in range(n))
print(binary_search(m, times))

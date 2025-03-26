# 1731 추론 / 수학, 사칙연산

series = [int(input()) for _ in range(int(input()))]

if 2 * series[1] == series[0] + series[2]:
    print(series[-1] + series[1] - series[0])
else:
    print(series[-1] * (series[1] // series[0]))

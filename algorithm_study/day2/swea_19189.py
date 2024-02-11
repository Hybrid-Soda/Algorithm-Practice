# 19189 순열의 아름다움
# 순열 : 1 ~ N의 숫자로 구성 / 중복 x 길이 N의 수열 pN

# < 아름다운 쌍 >
# max⁡(pl, …, pr) - min(pl, …, pr) = r - l 과 1 ≤ l ≤ r ≤ N 을 만족하는 (l,r)

# < 구해야 하는 것 >
# 길이 N의 모든 순열에 대해 sum(count(아름다운 쌍)) % (소수 P) = ?

# < 예시 >
# | N | r-l: (l,r) (1 ≤ l ≤ r ≤ N)    | pN: N!      | max(pl~pr) - min(pl~pr)   |
# |-----------------------------------------------------------------------------|
# | 1 | 0: (1,1)                      | p1: 1! = 1  | pair = 1 / permu = 1 * 1! |
# |-----------------------------------------------------------------------------|
# | 2 | 0: (1,1), (2,2)               | p1: 1! = 1  | pair = 2 / permu = 2 * 1! |
# |   | 1: (1,2)                      | p2: 2! = 2  | pair = 1 / permu = 1 * 2! |
# |-----------------------------------------------------------------------------|
# | 3 | 0: (1,1), (2,2), (3,3)        | p1: 1! = 1  | pair = 3 / permu = 3 * 1! |
# |   | 1: (1,2), (2,3)               | p2: 2! = 2  | pair = 2 / permu = 2 * 2! |
# |   | 2: (1,3)                      | p3: 3! = 6  | pair = 1 / permu = 1 * 3! |
# |-----------------------------------------------------------------------------|
# | 4 | 0: (1,1), (2,2), (3,3), (4,4) | p1: 1! = 1  | pair = 4 / permu = 4 * 1! |
# |   | 1: (1,2), (2,3), (3,4)        | p2: 2! = 2  | pair = 3 / permu = 3 * 2! |
# |   | 2: (1,3), (2,4)               | p3: 3! = 6  | pair = 2 / permu = 2 * 3! |
# |   | 3: (1,4)                      | p4: 4! = 24 | pair = 1 / permu = 1 * 4! |

'''
< 일반화 DP 배열 >
| N \ r-l |     0     |     1     |     2     |     3     |
|---------------------------------------------------------|
|    1    |  1!*1*1!  |           |           |           |
|---------------------------------------------------------|
|    2    |  2!*2*1!  |  1!*1*2!  |           |           |
|---------------------------------------------------------|
|    3    |  3!*3*1!  |  2!*2*2!  |  1!*1*3!  |           |
|---------------------------------------------------------|
|    4    |  4!*4*1!  |  3!*3*2!  |  2!*2*3!  |  1!*1*4!  |

DP[N][k] = (N-k)! * (N-k) * (k+1)!
ans = sum(DP[N][:N])
'''

import sys
sys.stdin = open("input.txt")

for tc in range(int(input())):
    # N : 순열의 길이 / P : 소수
    N, P = map(int, input().split())
    happy = 0
    facto = [1] * (N+1)

    # 팩토리얼 배열 입력 (기하급수적으로 수가 커지므로 P로 계속 나누어 준다)
    for i in range(2, N+1):
        facto[i] = (facto[i-1] * i) % P

    # 팩토리얼 배열을 이용하여 답안 도출
    for k in range(N):
        happy += ((facto[N-k] * (N-k)) % P * facto[k+1]) % P
        happy %= P

    print(f'#{tc+1} {happy}')
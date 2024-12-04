# 22251 빌런 호석 / 구현, 브루트포스 알고리즘

num_led = [
    "1111110",  # 0
    "0110000",  # 1
    "1101101",  # 2
    "1111001",  # 3
    "0110011",  # 4
    "1011011",  # 5
    "1011111",  # 6
    "1110000",  # 7
    "1111111",  # 8
    "1111011",  # 9
]


# num_1과 num_2의 LED 차이를 계산
def compare_led(num_1: int, num_2: int):
    result = 0

    for i in range(7):
        if num_led[num_1][i] != num_led[num_2][i]:
            result += 1

    return result


def calculate_case(left_cnt: int, now_floor: str, digit: int):
    global ans
    if digit == k:
        # 모든 자릿수 확인 후 유효한 경우를 기록
        if 1 <= int(now_floor) <= n:
            ans += 1
        return

    for i in range(10):
        # 자릿수 교체 시 필요한 LED 반전 횟수 계산
        cnt = compare_led(i, int(now_floor[digit]))

        if left_cnt >= cnt:
            # 새로운 층수로 갱신하여 재귀 호출
            new_floor = now_floor[:digit] + str(i) + now_floor[digit + 1 :]
            calculate_case(left_cnt - cnt, new_floor, digit + 1)


n, k, p, x = map(int, input().split())
x = str(x).zfill(k)
ans = 0
calculate_case(p, x, 0)
print(ans - 1)

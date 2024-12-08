# 2138 전구와 스위치 / 그리디 알고리즘


def toggle(lights: list[bool], idx: int, n: int):
    lights[idx] = not lights[idx]
    if idx > 0:
        lights[idx - 1] = not lights[idx - 1]
    if idx < n - 1:
        lights[idx + 1] = not lights[idx + 1]


def get_count(n: int, lights: list[bool], target: list[bool], press_first: bool):
    copy = lights[:]
    cnt = 0

    if press_first:
        toggle(copy, 0, n)
        cnt += 1

    for i in range(1, n):
        if copy[i - 1] != target[i - 1]:
            toggle(copy, i, n)
            cnt += 1

    return cnt if copy == target else float("inf")


def main():
    n = int(input())
    lights = list(map(lambda c: c == "1", input().strip()))
    target = list(map(lambda c: c == "1", input().strip()))

    cnt = get_count(n, lights, target, False)
    if cnt != float("inf"):
        return cnt

    cnt = get_count(n, lights, target, True)
    if cnt != float("inf"):
        return cnt

    return -1


if __name__ == "__main__":
    print(main())

# 1. 현재 전구 상태 강제 수정: 원하는 상태가 아니라면 현재 전구를 기준으로 스위치를 눌러야 함
# 2. 국소적 영향: 스위치를 누르면 자신과 양옆만 바뀌어 국소적 변화만 발생
# 3. 탐색 공간 축소: 첫 번째 전구 선택 후 선형 탐색으로 최소 스위치 횟수를 결정 가능

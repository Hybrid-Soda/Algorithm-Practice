# 2110 공유기 설치 / 이분 탐색, 매개 변수 탐색


# 공유기 설치 시뮬레이션
def setup_router(n: int, mid: int, coord: list[int]) -> int:
    cnt = 1
    now = coord[0]

    for i in range(1, n):
        if coord[i] >= now + mid:
            now = coord[i]
            cnt += 1

    return cnt


# 공유기 설치 간격 자체를 이진탐색
def binary_search(n: int, c: int, coord: list[int]) -> int:
    start, end = 1, coord[-1] - coord[0]
    best_dist = 0

    while start <= end:
        mid = (start + end) // 2
        cnt = setup_router(n, mid, coord)

        # 공유기 설치 개수가 부족하면 공유기 사이 거리 감소시킴
        if cnt >= c:
            best_dist = mid
            start = mid + 1
        else:
            end = mid - 1

    return best_dist


def main():
    n, c = map(int, input().split())
    coord = sorted(int(input()) for _ in range(n))
    print(binary_search(n, c, coord))


if __name__ == "__main__":
    main()

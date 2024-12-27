# 2866 문자열 잘라내기 / 자료 구조, 문자열, 이분 탐색, 해시를 사용한 집합과 맵

# 주어진 행 'mid'부터 시작하는 부분 문자열을 비교하는 함수
def compare_str(c: int, mid: int, table: list[str]):
    str_set = set()

    for i in range(c):
        substr = ''.join(row[i] for row in table[mid:])
        str_set.add(substr)

    return True if len(str_set) == c else False

# 최대 행 인덱스를 찾기 위해 이분 탐색을 수행하는 함수
def binary_search(r: int, c: int, table: list[str]):
    small, big = 0, r - 1
    ans = 0

    while small <= big:
        mid = (small + big) // 2
        if compare_str(c, mid, table):
            ans = max(ans, mid)
            small = mid + 1
        else:
            big = mid - 1

    return ans

r, c = map(int, input().split())
table = [input() for _ in range(r)]
print(binary_search(r, c, table))
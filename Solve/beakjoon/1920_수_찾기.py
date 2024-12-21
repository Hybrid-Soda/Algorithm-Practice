# 1920 수 찾기


def binary_search(target: int, data: list[int]) -> bool:
    left, right = 0, len(data) - 1

    while left <= right:
        mid = (left + right) // 2
        if data[mid] == target:
            return True
        elif data[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return False


def main():
    n = int(input())
    arr = sorted(map(int, input().split()))
    m = int(input())
    targets = map(int, input().split())

    results = [1 if binary_search(target, arr) else 0 for target in targets]
    print("\n".join(map(str, results)))


if __name__ == "__main__":
    main()

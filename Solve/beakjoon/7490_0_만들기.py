# 7490 0 만들기 / 구현, 문자열, 브루트포스 알고리즘, 백트래킹


def dfs(string: str, now_num: int, end_num: int, now_res: int, last: int):
    if now_num > end_num:
        if now_res == 0:
            print(string)
        return

    new_last = last * 10 + (now_num if last > 0 else -now_num)
    dfs(
        string + f" {now_num}",
        now_num + 1,
        end_num,
        now_res - last + new_last,
        new_last,
    )
    dfs(string + f"+{now_num}", now_num + 1, end_num, now_res + now_num, now_num)
    dfs(string + f"-{now_num}", now_num + 1, end_num, now_res - now_num, -now_num)


for _ in range(int(input())):
    n = int(input())
    dfs("1", 2, n, 1, 1)
    print()

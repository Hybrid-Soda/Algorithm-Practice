# 12919 A와 B 2 / 문자열, 브루트포스 알고리즘, 재귀

s = input()
t = input()


def plus_a(string: str):
    return string + "A"


def plus_b(string: str):
    return "B" + string[::-1]


def game(s: str, t: str):
    if s == t:
        print(1)
        exit()

    if len(s) >= len(t) or not (s in t or s[::-1] in t):
        return None

    game(plus_a(s), t)
    game(plus_b(s), t)


game(s, t)
print(0)

# 10867 중복 빼고 정렬하기 / 정렬

_ = int(input())
p = sorted(set(map(int, input().split())))
print(*p)
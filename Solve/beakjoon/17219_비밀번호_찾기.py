# 17219 비밀번호 찾기
import sys
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
sites = dict()

for _ in range(n):
    uri, password = input().rstrip().split()
    sites[uri] = password

for _ in range(m):
    print(sites[input().rstrip()])
# 11723 집합 / 구현, 비트마스킹

import sys
input = sys.stdin.readline

s = [0] * 21

for _ in range(int(input())):
    cmd = input().rstrip().split()
    
    if len(cmd) == 2: x = int(cmd[1])

    if cmd[0] == 'add':
        s[x] = 1
    elif cmd[0] == 'remove':
        s[x] = 0
    elif cmd[0] == 'check':
        print(1 if s[x] else 0)
    elif cmd[0] == 'toggle':
        s[x] = 0 if s[x] else 1
    elif cmd[0] == 'all':
        s = [1] * 21
    elif cmd[0] == 'empty':
        s = [0] * 21
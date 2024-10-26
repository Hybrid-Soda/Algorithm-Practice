# 25757 임스와 함께하는 미니게임 / 자료 구조, 문자열, 해시를 사용한 집합과 맵
import sys
input = sys.stdin.readline

N, game = input().split()
N = int(N)
applicants = len(set(input() for _ in range(N)))

if game == 'Y':
    print(applicants)
elif game == 'F':
    print(applicants//2)
else:
    print(applicants//3)
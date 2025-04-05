# 2220 힙 정렬 / 자료 구조, 그리디 알고리즘
# n은 맨 앞에 있도록
# 1은 맨 끝에 있도록 (heappop 시 맨 끝에 있는 원소가 맨 앞으로 옴)
# k번 째 원소 > 2k+1, 2k+2번째 원소
# 1을 계속 맨위로 올린 후 최대 수를 넣고 1을 맨 아래로 옮김

n = int(input())

if n == 1:
    print(1)
    exit()

heap = [1]

def move_up(idx):
    while idx > 0:
        parent = (idx-1) // 2
        heap[idx], heap[parent] = heap[parent], heap[idx]
        idx = parent

for i in range(2, n+1):
    move_up(len(heap)-1)
    heap[0] = i
    heap.append(1)

print(*heap)
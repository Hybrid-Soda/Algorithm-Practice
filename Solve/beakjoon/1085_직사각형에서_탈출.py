# 1085 직사각형에서 탈출 / 수학, 기하학

x, y, w, h = map(int, input().split())
print(min(x, w-x, y, h-y))
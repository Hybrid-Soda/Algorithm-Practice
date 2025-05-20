# 2485 가로수 / 수학, 정수론, 유클리드 호제법

import sys, math
input = sys.stdin.readline

case=int(input())
trees=[]
space=[]
trees.append(int(input()))

for i in range(1,case):
    tree=int(input())
    trees.append(tree)                         
    space.append(trees[i]-trees[i-1])

min_space=math.gcd(*space)

print(((trees[-1]-trees[0])//min_space)-1-(case-2))
# 1449 수리공 항승

n, l = map(int, input().split())
data = sorted(map(int, input().split()))

start = data[0]
count = 1

for location in data[1:]:
  if location not in range(start, start+l):
    start = location
    count += 1

print(count)
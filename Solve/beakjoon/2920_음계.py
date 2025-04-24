# 2920 음계 / 구현

scale = list(map(int, input().split()))
is_asc = True if scale[0] < scale[1] else False

for i in range(7):
    if (is_asc and scale[i] > scale[i+1]) or (not is_asc and scale[i] < scale[i+1]):
        exit(print('mixed'))

print('ascending' if is_asc else 'descending')
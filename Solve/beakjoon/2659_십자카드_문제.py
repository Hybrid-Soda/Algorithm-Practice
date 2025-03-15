# 2659 십자카드 문제 / 구현, 브루트포스 알고리즘, 정렬

def rotation(card):
    rotations = [card[i:] + card[:i] for i in range(4)]
    return min(rotations)

card = ''.join(input().split())
c_num = int(rotation(card))
valid_count = 1

for num in range(1111, c_num):
    num_str = str(num)
    if '0' in num_str:
        continue
    if rotation(num_str) == num_str:
        valid_count += 1

print(valid_count)
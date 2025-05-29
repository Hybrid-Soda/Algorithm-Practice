# 2621 카드게임 / 구현, 많은 조건 분기

card = [[0]*4, [0]*10, []]

for _ in range(5):
    color, idx = input().split()

    if color == 'R':
        card[0][0] += 1
    elif color == 'B':
        card[0][1] += 1
    elif color == 'Y':
        card[0][2] += 1
    elif color == 'G':
        card[0][3] += 1
    card[1][int(idx)] += 1
    card[2].append(int(idx))

    
if 5 in card[0]:
    if max(card[2]) - min(card[2]) == 4:
        print(max(card[2]) + 900)
    else:
        print(max(card[2]) + 600)

elif 4 in card[1]:
    print(800 + card[1].index(4))

elif 3 in card[1]:
    if 2 in card[1]:
        print(card[1].index(3)*10 + card[1].index(2) + 700)
    else:
        print(card[1].index(3) + 400)

elif 2 in card[1]:
    if card[1].count(2) == 2:
        nums = []
        for i in range(1, 10):
            if card[1][i] == 2:
                nums.append(i)
        print(min(nums) + max(nums)*10 + 300)
    else:
        print(card[1].index(2) + 200)

else:
    if max(card[2]) - min(card[2]) == 4:
        print(max(card[2]) + 500)
    else:
        print(max(card[2]) + 100)
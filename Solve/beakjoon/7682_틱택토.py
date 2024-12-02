# 7682 틱택토 / 구현


def count_piece(board: str):
    ox = [0, 0]

    for piece in board:
        if piece == "O":
            ox[0] += 1
        elif piece == "X":
            ox[1] += 1

    return ox


def check_winner(board: str):
    bingo = set()

    # 가로
    for i in range(0, 9, 3):
        if board[i] == board[i + 1] == board[i + 2] and board[i] in ("O", "X"):
            bingo.add(board[i])

    # 세로
    for i in range(3):
        if board[i] == board[i + 3] == board[i + 6] and board[i] in ("O", "X"):
            bingo.add(board[i])

    # 대각
    if board[0] == board[4] == board[8] and board[0] in ("O", "X"):
        bingo.add(board[0])

    if board[2] == board[4] == board[6] and board[2] in ("O", "X"):
        bingo.add(board[2])

    # 판별
    if len(bingo) == 1:
        return bingo.pop()
    elif len(bingo) == 2:
        return "D"
    else:
        return False


while True:
    board = input()

    if board == "end":
        break

    # 먼저 각 말의 개수부터 구한다
    count_o, count_x = count_piece(board)
    winner = check_winner(board)

    # O 승인 경우
    if count_o == count_x and winner == "O":
        print("valid")
        continue

    # X 승인 경우, 무승부인 경우
    if count_o == count_x - 1:
        if winner == "X" or (not winner and count_o + count_x == 9):
            print("valid")
            continue

    print("invalid")

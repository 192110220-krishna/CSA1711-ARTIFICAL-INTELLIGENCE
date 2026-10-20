
def minimax(depth, is_maximizing):
    if scores == 10:
        return 10 - depth
    if scores == -10:
        return depth - 10
    if not any(cell == " " for cell in board):
        return 0

    if is_maximizing:
        best = -float("inf")
        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                best = max(best, minimax(depth + 1, False))
                board[i] = " "
        return best
    else:
        best = float("inf")
        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                best = min(best, minimax(depth + 1, True))
                board[i] = " "
        return best

def evaluate():
    for a, b, c in wins:
        if board[a] == board[b] == board[c] != " ":
            return 10 if board[a] == "X" else -10
    return 0

def minimax(depth, is_maximizing):
    score = evaluate()

    if score == 10:
        return score - depth
    if score == -10:
        return score + depth
    if not any(cell == " " for cell in board):
        return 0

    if is_maximizing:
        best = -float("inf")
        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                best = max(best, minimax(depth + 1, False))
                board[i] = " "
        return best
    else:
        best = float("inf")
        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                best = min(best, minimax(depth + 1, True))
                board[i] = " "
        return best

def find_best_move():
    best_value = float("inf")
    best_move = -1

    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            move_value = minimax(0, True)
            board[i] = " "

            if move_value < best_value:
                best_value = move_value
                best_move = i

    return best_move

def display():
    for i in range(0, 9, 3):
        print(" | ".join(board[i:i + 3]))
        if i < 6:
            print("--+---+--")

wins = [
    (0, 1, 2), (3, 4, 5), (6, 7, 8),
    (0, 3, 6), (1, 4, 7), (2, 5, 8),
    (0, 4, 8), (2, 4, 6)
]

board = [" "] * 9

print("Tic-Tac-Toe: You are X, Computer is O")
print("Positions:")
print("1 | 2 | 3")
print("--+---+--")
print("4 | 5 | 6")
print("--+---+--")
print("7 | 8 | 9")

while True:
    display()

    try:
        pos = int(input("Enter your position (1-9): ")) - 1
    except ValueError:
        print("Enter a valid number.")
        continue

    if pos < 0 or pos > 8 or board[pos] != " ":
        print("Invalid position. Try again.")
        continue

    board[pos] = "X"

    if evaluate() == 10:
        display()
        print("You win!")
        break

    if not any(cell == " " for cell in board):
        display()
        print("It's a draw!")
        break

    move = find_best_move()
    board[move] = "O"
    print("Computer chooses position:", move + 1)

    if evaluate() == -10:
        display()
        print("Computer wins!")
        break

    if not any(cell == " " for cell in board):
        display()
        print("It's a draw!")
        break

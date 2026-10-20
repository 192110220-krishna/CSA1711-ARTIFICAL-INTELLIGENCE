
board = [" "] * 9

wins = [
    (0, 1, 2), (3, 4, 5), (6, 7, 8),
    (0, 3, 6), (1, 4, 7), (2, 5, 8),
    (0, 4, 8), (2, 4, 6)
]

def display():
    for i in range(0, 9, 3):
        print(" " + " | ".join(board[i:i+3]))
        if i < 6:
            print("---+---+---")

def winner():
    for a, b, c in wins:
        if board[a] != " " and board[a] == board[b] == board[c]:
            return board[a]
    return None

moves = 0

while moves < 9:
    display()

    player = "X" if moves % 2 == 0 else "O"

    try:
        pos = int(input(
            f"Player {player}, enter position (1-9): "
        )) - 1
    except ValueError:
        print("Please enter a valid number.")
        continue

    if pos < 0 or pos > 8 or board[pos] != " ":
        print("Invalid or occupied position. Try again.")
        continue

    board[pos] = player
    moves += 1

    if winner():
        display()
        print(f"Player {player} wins!")
        break
else:
    display()
    print("It's a draw!")

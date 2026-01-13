def print_board(board):
    for i, row in enumerate(board):
        print(" | ".join(row))
        if i < len(board) - 1:
            print("-" * 5)


def check_winner(board):
    # Lignes
    for row in board:
        if row[0] != " " and row.count(row[0]) == len(row):
            return row[0]  # retourne le symbole du gagnant

    # Colonnes
    for col in range(len(board[0])):
        if board[0][col] != " " and board[0][col] == board[1][col] == board[2][col]:
            return board[0][col]

    # Diagonale principale
    if board[0][0] != " " and board[0][0] == board[1][1] == board[2][2]:
        return board[0][0]

    # Diagonale secondaire
    if board[0][2] != " " and board[0][2] == board[1][1] == board[2][0]:
        return board[0][2]

    return None  # pas de gagnant


def is_board_full(board):
    for row in board:
        if " " in row:
            return False
    return True


def tic_tac_toe():
    board = [[" "] * 3 for _ in range(3)]
    player = "X"

    while True:
        print_board(board)

        # Saisie sécurisée
        try:
            row = int(input(f"Enter row (0, 1, or 2) for player {player}: "))
            col = int(input(f"Enter column (0, 1, or 2) for player {player}: "))
        except ValueError:
            print("Please enter numbers only (0, 1, or 2).")
            continue

        if not (0 <= row <= 2 and 0 <= col <= 2):
            print("Row and column must be 0, 1, or 2.")
            continue

        if board[row][col] != " ":
            print("That spot is already taken! Try again.")
            continue

        board[row][col] = player

        winner = check_winner(board)
        if winner:
            print_board(board)
            print(f"Player {winner} wins!")
            break

        if is_board_full(board):
            print_board(board)
            print("It's a draw!")
            break

        # Changement de joueur
        player = "O" if player == "X" else "X"


if __name__ == "__main__":
    tic_tac_toe()

import numpy as np

board = np.array([['-', '-', '-'],['-', '-', '-'],['-', '-', '-']])

p1s = 'X'
p2s = 'O'


def won(symbol):
    # Check rows and columns
    for i in range(3):
        if all(board[i, :] == symbol) or all(board[:, i] == symbol):
            return True
    # Check diagonals
    if all(np.diag(board) == symbol) or all(np.diag(np.fliplr(board)) == symbol):
        return True
    return False


def place(symbol):
    print(np.matrix(board))
    while True:
        row = int(input("Enter row (1 or 2 or 3): "))
        col = int(input("Enter column (1 or 2 or 3): "))
        if row in [1, 2, 3] and col in [1, 2, 3]:
            if board[row - 1][col - 1] == '-':
                board[row - 1][col - 1] = symbol
                break
            else:
                print("That spot is already taken. Try again.")
        else:
            print("Invalid input. Please enter values between 1 and 3.")


def play():
    for turn in range(9):
        if turn % 2 == 0:
            print("X turn")
            place(p1s)
            if won(p1s):
                print(np.matrix(board))
                print("X wins!")
                break
        else:
            print("O turn")
            place(p2s)
            if won(p2s):
                print(np.matrix(board))
                print("O wins!")
                break
    else:
        print("It's a draw!")


# Run the game
play()
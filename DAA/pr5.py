
n = 4

board = []

for i in range(n):
    row = []
    for j in range(n):
        row.append(0)
    board.append(row)


def safe(row, col):

    for i in range(row):
        for j in range(n):
            if board[i][j] == 1:
                if j == col or abs(i-row) == abs(j-col):
                    return False

    return True


def solve(row):

    if row == n:
        return True

    for col in range(n):
        if safe(row, col):
            board[row][col] = 1

            if solve(row + 1):
                return True

            board[row][col] = 0

    return False


# First queen
board[0][1] = 1

if solve(1):
    print("Solution exists")
    for row in board:
        print(row)
else:
    print("No solution exists")


 

def check(board, i, j, kk):
    for k in range(9):
        if board[i][k] == kk:
            return False
        if board[k][j] == kk:
            return False
        if board[3 * (i // 3) + k // 3][3 * (j // 3) + k % 3] == kk:
            return False
    return True

def placing(board, i, j):
    if i == 9:
        return True  
    if j == 9:
        return placing(board, i + 1, 0)
    if board[i][j] != '.':
        return placing(board, i, j + 1)

    for k in range(1, 10):
        kk = str(k)
        if check(board, i, j, kk):
            board[i][j] = kk
            if placing(board, i, j + 1):
                return True
            board[i][j] = '.'
    return False

def solveSudoku(board):
    placing(board, 0, 0) 

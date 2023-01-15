global N
N = 4


def printSolution(board):
    """Print N queen board
    """
    for i in range(N):
        for j in range(N):
            print(board[i][j], end=' ')
        print()


def isSafe(board, row, col):
    """
    A utility function to check if a knight can be placed on
    board[row][col].
    """

    if not (row+1 > len(board)-1 or col-2 < 0):
        if (board[row+1][col-2] == 1):
            return False
    if not (row-1 < 0 or col-2 < 0):
        if (board[row-1][col-2] == 1):
            return False
    if not (row-2 < 0 or col-1 < 0):
        if (board[row-2][col-2] == 1):
            return False
    if not (row-2 < 0 or col+1 > len(board)-1):
        if (board[row-2][col+1] == 1):
            return False
    if not (row+1 > len(board)-1 or col+2 > len(board)-1):
        if (board[row+1][col+2] == 1):
            return False
    if not (row-1 < 0 or col+2 > len(board)-1):
        if (board[row-1][col+2] == 1):
            return False
    if not (row+2 > len(board)-1 or col-1 < 0):
        if (board[row+2][col-2] == 1):
            return False
    if not (row+2 > len(board)-1 or col+1 > len(board)-1):
        if (board[row+2][col+1] == 1):
            return False

    return True


def solve_kk_util(board, col):
    # base case: If all queens are places
    # then return true
    if col >= N:
        return True

    # Consider this column and try placing queens in all rows one by one
    for i in range(N):
        if isSafe(board, i, col):
            # Plase this queen in board[i][col]
            board[i][col] = 1

            # recursive apporach to place rest of the queens
            if solve_kk_util(board, col+1) == True:
                return True

            # if placing queen in board[i][col]
            # doesnt lead to a solution, then
            # queen from board [i][col]
            board[i][col] = 0

    # if this queen can not be placed in any row in
    # this column col then return false
    return False


def solve_kk():
    """
    This function solves the K knight problem using 
    backtracking. It manily uses solve_kk_util() to 
    solve the problem.
    It returns false if queens cannont be placed, otherwise
    return true and placement of queens in the form of 1s.
    not that there may be more than one solutions, this function prints
    one of the feasible solutions
    """
    board = [[0, 0, 0, 0],
             [0, 0, 0, 0],
             [0, 0, 0, 0],
             [0, 0, 0, 0]
             ]
    if solve_kk_util(board, 0) == False:
        print("Solution does not exist")
        return False

    printSolution(board)
    return True


solve_kk()

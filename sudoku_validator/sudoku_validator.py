#Sudoku Validator
def read_sodoku():
    board=[ ]
    for _ in range (9):
        row= input().strip()

        #Check if row has exactly 9 characters
        if len(row)!=9:
            return None
        #Check if all characters are digits from 1 to 9
        for ch in row:
            if ch not in "123456789":
                return None
        board.append(list(row))
    return board
def is_valid_sodoku(board):
    valid_set=set("123456789")
    #Check rows
    for row in board:
        if set(row)!= valid_set:
            return False
    #Check colums
    for col in range(9):
        column=[board[row][col] for row in range (9)]
        if set(column)!= valid_set:
            return False
    #Check 3x3 sub-squares
    for row_block in range (0,9,3):
        for col_block in range (0,9,3):
            block=[]
            for i in range (3):
                for j in range(3):
                    block. append(board[row_block+i][col_block+j])
            if set(block)!=valid_set:
                    return False
    return True
#Main program
board= read_sodoku()
if board is None:
    print("No")
elif is_valid_sodoku(board):
    print("Yes")
else:
    print("No")

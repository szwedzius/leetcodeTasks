#I believe that in this task we need to iterate through the whole array once
#And create necessary structures to check for duplicates
#I assume that the time complexity is about O(n) because we will have 3 arrays of rows columns and squares
# and each one will be analayzed for duplicates and space complexity is O(n)
def isValidSudoku(self, board: list[list[str]]):
    rows = [[] for i in range(0,9)]
    columns = [[] for i in range(0,9)]
    squares = [[] for i in range(0,9)]
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == ".":
                continue
            rows[i].append(board[i][j])
            columns[j].append(board[i][j])
            squares[int(i/3)+int(j/3)*3].append(board[i][j])

    for x in range(len(board)):
        rowSet = set(rows[x])
        colSet = set(columns[x])
        sqSet = set(squares[x])
        if len(rows[x]) != len(rowSet) or len(colSet) != len(columns[x]) or len(squares[x]) != len(sqSet):
            return False

    return True


result = isValidSudoku(0,
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]])

print(result)
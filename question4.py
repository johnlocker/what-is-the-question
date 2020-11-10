def question4(grid):
    # check rows
    for row in grid:
        if len(row) != len(set(row)):
            print(row)
            return False
    # check cols
    for i in range(len(grid)):
        col = [grid[j][i] for j in range(len(grid))]
        if len(col) != len(set(col)):
            print(col)
            return False
    # check squares
    for s in [0, 3, 6]:
        for q in [0, 3, 6]:
            squareList = [g[q:(q + 3)] for g in grid[s:(s + 3)]]
            square = [num for subList in squareList for num in subList]
            if len(square) != len(set(square)):
                return False
    return True


grid1 = [[1, 3, 2, 5, 4, 6, 9, 2, 7],
[4, 6, 5, 8, 7, 9, 3, 8, 1],
[7, 9, 8, 2, 1, 3, 6, 5, 4],
[9, 2, 1, 4, 3, 5, 8, 7, 6],
[3, 5, 4, 7, 6, 8, 2, 1, 9],
[6, 8, 7, 1, 9, 2, 5, 4, 3],
[5, 7, 6, 9, 8, 1, 4, 3, 2],
[2, 4, 3, 6, 5, 7, 1, 9, 8],
[8, 1, 9, 3, 2, 4, 7, 6, 5]]
assert question4(grid1) == False

grid2 = [[1,3,4,2,5,6,9,8,7], 
 [4,6,8,5,7,9,3,2,1], 
 [7,9,2,8,1,3,6,5,4], 
 [9,2,3,1,4,5,8,7,6], 
 [3,5,7,4,6,8,2,1,9], 
 [6,8,1,7,9,2,5,4,3], 
 [5,7,6,9,8,1,4,3,2], 
 [2,4,5,6,3,7,1,9,8], 
 [8,1,9,3,2,4,7,6,5]]
assert question4(grid2) == False

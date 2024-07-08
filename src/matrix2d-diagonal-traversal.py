def diagonal_traversal(matrix):
    num_rows = len(matrix)
    num_cols = len(matrix[0])
    
    for diagonal in range(num_rows + num_cols - 1):
        if diagonal < num_rows:
            row = diagonal
            col = 0
        else:
            row = num_rows - 1
            col = diagonal - num_rows + 1
        
        while row >= 0 and col < num_cols:
            print(matrix[row][col], end=' ')
            row -= 1
            col += 1
    print()

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

diagonal_traversal(matrix)

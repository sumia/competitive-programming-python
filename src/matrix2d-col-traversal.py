def column_wise_traversal(matrix):
    cols = len(matrix[0])
    rows = len(matrix)

    for col in range(cols):
        for row in range(rows):
            print(matrix[row][col], end=' ')
        print()

matrix = [
    [1, 2, 3],
    [4 ,5, 6],
    [7, 8, 9]
]

print(column_wise_traversal(matrix))
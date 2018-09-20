def find_saddle_points(matrix):
    result = []
    m = len(matrix)
    n = len(matrix[0])
    for i in range(m):
        for j in range(n):
            elem = matrix[i][j]
            column = [matrix[k][j] for k in range(m)]
            if min(matrix[i]) >= elem >= max(column):
                result.append([i, j])
    return result


lst = [[3, 8, 7],
       [5, 9, 6],
       [2, 6, 7]]

print(find_saddle_points(lst))

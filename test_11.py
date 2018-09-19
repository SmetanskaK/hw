lst = [[12, 17, 0, 34],
       [56, 8, 3, 4]]


def sort_alt(matrix):
    m = len(matrix)
    n = len(matrix[0])
    for i in range(n):
        column = []
        for j in range(m):
            column.append(matrix[j][i])
        if i % 2 == 0:
            column.sort(reverse=True)
        else:
            column.sort()
        for j in range(m):
            matrix[j][i] = column[j]
    return matrix


print(sort_alt(lst))

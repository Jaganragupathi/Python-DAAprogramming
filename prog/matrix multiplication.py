def matrix_multiply(A, B):
    if len(A[0]) != len(B):
        raise ValueError
    result = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                result[i][j] += A[i][k] * B[k][j]
    return result
A = [[1, 2, 3, 4],
     [5, 6, 7, 8],
     [9, 10, 11, 12],
     [13, 14, 15, 16]]
B = [[17, 18, 19, 20],
     [21, 22, 23, 24],
     [25, 26, 27, 28],
     [29, 30, 31, 32]]
try:
    result = matrix_multiply(A, B)
    print("Result of matrix multiplication:")
    for row in result:
        print(row)
except ValueError as e:
    print(e)

def binomial_coefficient_dp(n, k):
    C = []
    for i in range(n+1):
        row = []
        for j in range(k+1):
            row.append(0)
        C.append(row)
    for i in range(n+1):
        for j in range(min(i, k)+1):
            if j == 0 or j == i:
                C[i][j] = 1
            else:
                C[i][j] = C[i-1][j-1] + C[i-1][j]    
    return C[n][k]
n = 5
k = 2
print(binomial_coefficient_dp(n, k))

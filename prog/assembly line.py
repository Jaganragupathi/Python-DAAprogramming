def assembly_line_scheduling(a, t, e, x):
    n = len(a[0])  
    T1 = [0] * n  
    T2 = [0] * n  
    T1[0] = e[0] + a[0][0]
    T2[0] = e[1] + a[1][0]
    for j in range(1, n):
        T1[j] = min(T1[j-1] + a[0][j], T2[j-1] + t[1][j] + a[0][j])
        T2[j] = min(T2[j-1] + a[1][j], T1[j-1] + t[0][j] + a[1][j])
    final_time = min(T1[n-1] + x[0], T2[n-1] + x[1])    
    return final_time
a = [[4, 5, 3, 2],
     [2, 10, 1, 4]]
t = [[0, 7, 4, 5],
     [0, 9, 2, 8]]
e = [10, 12]
x = [18, 7]
print(f"The minimum time to complete the assembly is: {assembly_line_scheduling(a, t, e, x)}")

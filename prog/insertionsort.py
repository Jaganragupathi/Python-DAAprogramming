l = [2,5,1,4,7,6]
n = len(l)
for i in range(1,n):
    key = l[i]
    j = i-1
    while j>=0 and key<l[j]:
        l[j+1]=l[j]
        j = j-1
    l[j+1]=key
print(l)

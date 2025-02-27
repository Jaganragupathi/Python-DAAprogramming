a=[5,6,9,2,1]
n=len(a)
for i in range(n):
    min=i
    for j in range(i+1,n):
        if a[j]<a[min]:
            min=j
        temp=a[i]
        a[i]=a[min]
        a[min]=temp
print(a)

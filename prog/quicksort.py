def partition(a,l,h):
    p = a[h]
    i=l-1
    for j in range(l,h):
        if a[j]<= p:
            i = i+1
            a[i],a[j]=a[j],a[i]
    a[i+1],a[h]=a[h],a[i+1]
    return i+1
def quicksort(a,l,h):
    if l<h:
        pi = partition(a,l,h)
        quicksort(a,l,pi-1)
        quicksort(a,pi+1,h)
a = [1,7,4,1,10,9,-2]
s = len(a)
quicksort(a,0,s-1)
print(a)

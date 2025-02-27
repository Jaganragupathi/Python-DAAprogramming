def binarysearch(l,h,a,k):
    while(l<=h):
        mid = (l+h)//2
        if a[mid]>k:
            h=mid-1
        elif a[mid]<k:
            l=mid+1
        else:
            return mid

a = [200,201,202,500]
n = len(a)
l,h=0,n-1
t = 500
print(binarysearch(l,h,a,t))

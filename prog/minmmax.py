#Find maximum and minimum
a=[1,2,3]
l=0
h=len(a)                                                        
min=l
max=h
for i in range(0,h):
    min=a[0]
    max=a[0]
    if min>a[i]:
        min=a[i]
for i in range(0,h):        
    if max<a[i]:
        max=a[i]
print(min)
print(max)

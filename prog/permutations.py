def permutation(lst, r):
    if r == 0:
        return [[]]
    if len(lst) == 0:
        return []
    l = []
    for i in range(len(lst)):
        m = lst[i]
        remLst = lst[:i] + lst[i+1:]
        i=0
        for p in permutation(remLst, r-1):
            if [m]>p:
                l.append([m] + p)
                for i in range(len(l)):
                    l[i].sort()
    return l
n=int(input("ENTER NUMBER"))
data=[]
for i in range(0,n):
    p=input("ENTER ARRAY ELEMENTS: ")
    data.append(p) 
r =int(input("ENTER NUMBER")) 
p = permutation(data, r)
for i in range(0, len(p)):
    print(p[i])

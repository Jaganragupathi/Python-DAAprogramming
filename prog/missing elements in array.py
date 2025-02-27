n=[3,0,1]
m=max(n)
m1=min(n)
for i in range (min,max+1):
    if i in n:
        continue
    else:
        print(i,"is not present")

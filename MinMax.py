n=int(input())
ls=[]
for i in range(0,n) :
    x = int(input())
    ls.append(x)
ls.sort()
print(ls[0])
print(ls[n-1])
n = int(input())
ls = []
for i in range(1,1000001,1) :
    ls.append(0)
for i in range(0,n,1) :
    x = int(input())
    ls[x]+=1
a = int(input())
ans = 0
for i in range(0,(a//2)+1) : 
    if i+i==a :
        ans += ls[i]*(ls[i]-1)//2
    else :
        ans += ls[i]*ls[a-i]
print(ans)

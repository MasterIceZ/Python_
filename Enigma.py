n=int(input())
for i in range(0,(n-1),1) :
    if i==0 :
        continue
    print("."*(n-1-i-1),end="")
    print("*"*(2*i-1),end="")
    print("."*(n-1-i-1))
for i in range(1,(n-2)) :
    print("."*(i+1-1),end="")
    print("*"*((n-1)-i),end="")
    print("."*(i+1-1))
    

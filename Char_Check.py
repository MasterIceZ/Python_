s=input()
if s.isupper()==False and s.islower()==False :
    print("Mix")
elif s.islower() :
    print("All Small Letter")
else : 
    print("All Capital Letter")
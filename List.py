import random
def gen(ls) :
    for i in range(0,10,1) :
        ls.append(random.choice([1,2,3,4,5,6,7,8,9,10]))
    return ls
ls = []
ls = gen(ls)
print(ls)

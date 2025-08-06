i=1

while i<=5:
    a=6-i
    while a>=1:
        if a!=1:
            print(i,a,end=",")
        elif a!=5:
            print(i,a,end=" ** ")
        else:
            print(i,a)
        a-=1
    i+=1
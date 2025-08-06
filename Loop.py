print("Print number from 1 to 4 below each other")
#a=1
'''while a<5:
    print(a)
    a+=1'''
'''while a<5:
    print(a,end='    ')
    a+=1'''
for i in range(1,31):
    if i%10==0:
        print(i,end="\n")
    else:
        print(i,end=" - ")
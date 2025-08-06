#hahah funny

def hello_world(output):
    output("Hello World!")

hello_world(print)
print("Hello World!")

#if elif else condition
a=int(input("Enter a number:"))

if a==0:
    print("ZERO")
elif a==1:
    print("ONE")
else:
    print("ERROR")

#print numbers from 1 to 4 with spaces between them
print("Print number from 1 to 4 with spaces between them")
print('1',end='    ')
print('2',end='    ')
print('3',end='    ')
print('4',end='    ')

#same but 1 and 2 in same line but rest in second lines
print("Print number from 1 to 4 with spaces between them")
print('1',end='    ')
print('2',end='    ') #can also use \n but the similarity of code is compramised for a loop
print(" ")
print('3',end='    ')
print('4',end='    ')
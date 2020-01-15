#to check given number is prime or not
flag =0
x=int(input("enter number to check prime or not"))
for i in range(2,int(x/2)):
    if x % i == 0:
        flag = 1
if flag == 0:
    print(x,"it is prime")
else:
    print(x,"it is not prime")

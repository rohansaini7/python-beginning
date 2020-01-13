#to count digits in integer
x=int(input("enter number to find number of digits"))
count=0
while x > 0:
    x=x//10
    count += 1
print(count,": digits")


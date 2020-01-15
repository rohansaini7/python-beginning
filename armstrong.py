x = int(input("enter number to check armstrong or not"))
num = x
a = []
c = 0
arr = 0
total = 0
power = 0
while num > 0:
    num = num // 10
    c += 1

num = x
for i in range(c):
    arr = num % 10
    a.append(arr)
    num = num // 10

for i in a:
    power = pow(i, c)
    total = total + power
if x == total:
    print(x, "is armstring")
else:
    print(x, "is not armstring")

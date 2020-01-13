a=int(input("eneter no to check armstrong"))
cube=0
res=0
b=0
num = a
while num>0:
    b=num %10
    cube=b**3
    res +=cube
    num=num//10

if res==a:
    print(a,"armstring no")
else:
    print("not armstrong")



# to check input is alphabet or not

a = input("enetr any alphabet")
b=ord(a)
x = 0
y = 0
for i in range(ord('a'), ord('z')+1):
    # ord gives integer value of character
    if i == b:
        x += 1
for j in range(ord('A'),ord('Z')):
    if b == j:
        y += 1
if x == 1 or y == 1:
    print ("input is alphabet")
else:
    print ("not alphabet")


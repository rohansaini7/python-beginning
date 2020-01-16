x = input("to check palindrome")
a = len(x)
j = 0
flag=False
for i in range(int(a / 2)):
    j = a - 1 - i
    if x[i] != x[j]:
        flag=True
        break
    else:
        pass
print(' not palindrome' if flag else "palindrome")
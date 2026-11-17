# You can convert lowercase to uppercase and uppercase to lowercase using ASCII values with ord() and chr().
# ord() returns the Unicode number of a character.(charecter to number)
# chr() converts a Unicode number into its corresponding character.(Number to charecter)

s = input()
res=""
for i in s:
    if('a'<=i<='z'):
        res=res+chr(ord(i)-32)
    elif('A'<= i <='Z'):
        res=res+chr(ord(i)+32)
    else:
        res=res+i
print(res)

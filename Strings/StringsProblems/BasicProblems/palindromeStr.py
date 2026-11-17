s = input()
rev = ""
for ch in s:
    rev = ch+rev
print(rev)
if(rev==s):
    print("Palindrome")
else:
    print("Not a palindrome")
 
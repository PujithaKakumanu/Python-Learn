s=input()
# print(s[0],s[-1])
# print(s[0],s[len(s)-1])

first=s[0]
last=""
for i in range(len(s)):
    last=i
print(first,s[last])
# s=input().strip()
# res=""
# count=0
# for i in s:
#     if(i==" "):
#         count=count+1
# print(count+1)

s = input().strip()
count = 0

for i in range(len(s)):
    if s[i] != " ":
        if i == 0 or s[i-1] == " ":
            count = count + 1

print(count)


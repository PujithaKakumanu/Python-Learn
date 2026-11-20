s = input()
res = ""

for ch in s:
    if ch not in res:
        res+=ch

print(res)

# Using set : set doesn't allow the duplicates
s=input()
seen=set()
res=""
for i in s:
    if i not in seen:
        seen.add(i)
        res+=i  #preserve original order
print(res)

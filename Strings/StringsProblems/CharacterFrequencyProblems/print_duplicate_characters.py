s = input()
freq = {}
res =""

for ch in s:
    freq[ch] = freq.get(ch,0)+1
for char in freq:
    if freq[char]>1:
        res+=char
print(res)

#Approch-2 using sets concepts

s=input()
seen =set()
duplicates=""
for ch in s:
    if ch in seen:
        duplicates+=ch
    else:
        seen.add(ch)
print(duplicates)

s = input()
freq = {}
for ch in s:
    freq[ch]=freq.get(ch,0)+1

max_count=0
max_char=[]

for char,count in freq.items():
    if count>max_count:
        max_count=count
        max_char=[char]
    elif count==max_count:
        max_char.append(char)
print(max_char)
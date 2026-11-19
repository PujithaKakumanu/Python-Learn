s = input()
freq = {}
for ch in s:
    freq[ch]=freq.get(ch,0)+1

min_count=float('inf')
min_char=[]
for char,count in freq.items():
    if count<min_count:
        min_count=count
        min_char=[char]
    elif count==min_count:
        min_char.append(char)
print(min_char)


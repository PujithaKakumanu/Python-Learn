
# s=input()
# for char in s:
#     if s.count(char)==1:
#         print(char,end=" ")

# Approch-2
s = input()
freq={}
for ch in s:
    freq[ch]=freq.get(ch,0)+1
for char in s:
    if freq[char]==1:
        print(char,end =" ")
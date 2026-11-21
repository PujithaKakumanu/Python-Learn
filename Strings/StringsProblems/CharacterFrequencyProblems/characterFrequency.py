# For Count the frequency of each character:
# Take an empty dictionary.
# Iterate through each character in the string.
# Check whether the character already exists in the dictionary.
# If it exists, increase its count by 1.
# Otherwise, initialize its count to 1.

s = input()
freq = {}
for ch in s:
    if ch in freq:
        freq[ch]+=1
    else:
        freq[ch]=1
print(freq)

for char,count in freq.items():
    print(f"{char}:{count}")

# Approch-2  using set() and count().

s= input()
for ch in set(s):
    print(ch,":",s.count(ch))

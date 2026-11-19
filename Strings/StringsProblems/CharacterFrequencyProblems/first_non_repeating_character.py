# Step 1: Count the frequency of every character.
# Step 2: Traverse the string again.
# Step 3: Return the first character whose frequency is 1.

# Python dictionary has a get() method.
# Syntax: dictionary.get(key, default_value)
# It means:
# If the key exists, return its value.
# If the key doesn't exist, return the default value.

s = input()
char_count = {}
for ch in s:
    char_count[ch] = char_count.get(ch,0)+1
    # if ch in char_count:
    #     char_count[ch]+=1
    # else:
    #     char_count[ch]=1

for ch in s:
    if char_count[ch] == 1:
        print("First Non Repeating Charecter is: "+ch)
        break


# # Approch-2
# from collections import Counter
# s = input()
# count = Counter(s)
# for ch in s:
#     if count[ch]==1:
#         print(ch)
#         break

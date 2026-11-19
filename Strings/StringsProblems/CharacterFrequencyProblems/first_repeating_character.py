# Use Set when you only need to check whether an element appeared before.
# Use Dictionary when you need to count how many times an element appeared.
# A Python set stores unique elements.
# Logic:
# Create an empty set.
# Traverse the string character by character.
# Check whether the character already exists in the set.
# If it exists, return that character.
# Otherwise, add it to the set.

s = input()
seen=()
for ch in s:
    if ch in seen:
        print("First repeaing charecter is: "+ch)
        break
    else:
        seen.add(ch)


# s=input()
# char_count = {}
# for ch in s:
    
#     if ch in char_count:
#         print(ch)
#         break
#     else:
#         char_count[ch]=1

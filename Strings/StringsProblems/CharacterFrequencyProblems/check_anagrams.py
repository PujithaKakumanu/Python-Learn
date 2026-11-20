# anagram:
# Two strings are called anagrams 
# if they contain exactly the same characters with the same frequency,
# but the order of characters can be different.

# Approach 1: Using sorting ---> O(n log n) 
# s1=input()
# s2=input()

# if sorted(s1)==sorted(s2):
#     print("Anagrams")
# else:
#     print("Not an Anagrams")


s1 = input()
s2 = input()

char_count = {}

if len(s1) != len(s2):
    print("Not anagrams")
    exit()

for ch in s1:
    char_count[ch] = char_count.get(ch, 0) + 1

for ch in s2:
    if ch not in char_count:
        print("Not anagrams")
        exit()

    char_count[ch] -= 1

    if char_count[ch] < 0:
        print("Not anagrams")
        exit()

print("Anagrams")

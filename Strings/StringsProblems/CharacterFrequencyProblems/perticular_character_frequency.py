s=input()

char=input()
print(s.count(char))

# Approch-2
s=input()
char=input()
count=0
for ch in s:
    if  ch == char:
        count+=1
print(count)


s=input()
vcount=0
cCount=0
# for i in range(len(s)):
#     if(s[i]=='A' or s[i]=='E' or s[i]=='I' or s[i]=='O' or s[i]=='U' or s[i]=='a' or s[i]=='e' or s[i]=='i' or s[i]=='o' or s[i]=='u'):
#         vcount=vcount+1
#     else:
#         cCount=cCount+1
# print(vcount,cCount)

for i in range(len(s)):
    if(s[i] in "aeiouAEIOU"):
        vcount=vcount+1
    else:
        cCount=cCount+1
print(vcount,cCount)
#  ASCII comparisons - Python can compare characters based on their Unicode values
s = input()
lowerCount=0
upperCount=0

# for i in s:
#     if(i.isupper()):
#         upperCount=upperCount+1
#     else:
#         lowerCount=lowerCount+1

for i in s:
    if('A'<=i<='Z'):
        upperCount=upperCount+1
        print("UpperCase",i)
    else:
        lowerCount=lowerCount+1
        print("Lowercase",i)
  
print(upperCount,lowerCount)

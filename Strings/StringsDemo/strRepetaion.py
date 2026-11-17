# Repetition of a string using * operator.
# general syntax: string * n (where n is the number of times the string is to be repeated)
s = "Hello "
print(s * 3)

s = "Hello My name is kakumanu Pujitha. I am a 2026 Graduate. I love to learn Python and Machine Learning."
s = s.split()
for word in s:
    print("".join(word*2),end=" ")
    

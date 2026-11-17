# casefold() method is used to convert the string into lower case. 
# It is similar to lower() method but casefold() method is more aggressive in converting the string into lower case. 
# It is used for caseless matching.
# General Syntax: string.casefold()
s = "KaKuMaNu PuJiThA @2026"
print(s.casefold())

# center() method is used to center align the string within the specified width.
# General Syntax: string.center(width, fillchar)
# fillchar is optional. It is used to fill the remaining space with the specified character. The default value of fillchar is a space.
s = "KaKuMaNu PuJiThA @2026"
print(s.center(50, '*'))

#encode() method is used to encode the string using the specified encoding.
# General Syntax: string.encode(encoding, errors)
s = "KaKuMaNu PuJiThA @2026"
print(s.encode('utf-8', 'strict'))

#endswith()	 method is used to check whet
# her the string ends with the specified suffix or not. 
# It returns True if the string ends with the specified suffix, otherwise it returns False.
# General Syntax: string.endswith(suffix, start, end)
#start and end are optional. It is used to specify the start and end index of the string. 
# The default value of start is 0 and the default value of end is the length of the string.
s = "KaKuMaNu PuJiThA @2026"
print(s.endswith("2026"))
print(s.endswith("2026", 0, 25))

# expandtabs() method is used to replace the tab characters with spaces.
# General Syntax: string.expandtabs(tabsize) 
#expandtabs() method without any arguments, it uses the default tab size of 8 spaces

s = "Name\tAge\tLocation"
res = s.expandtabs(4)
print(res)
s = "hello welcome to AP"
print(s.expandtabs())
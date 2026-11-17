# Split method is used to split the string into a list of substrings based on a specified delimiter.
# Split method divides the string into smaller strings and returns them as a list.
# General syntax: string.split(delimiter, maxsplit)
# When no saparator is specified, split() divides the string using whitespace


s = "Hello welcome to Andra Pradesh, India"
print(s.split())  # Splitting by whitespace
print(s.split(","))  # Splitting by comma
print(s.split(None, 1))  # Splitting by whitespace, but only once

s = "My name is Pujitha Kakumanu"
print(s.split())  # Splitting by whitespace
print(s.split(None, 1))  # Splitting by whitespace, but only once

#Split using a specific character
s = "apple,banana,cherry"
print(s.split(","))  # Splitting by comma

s = "one;two;three;four"
print(s.split(";"))  # Splitting by semicolon

s = "2024-06-15"
print(s.split("-"))  # Splitting by hyphen

s = "HeyKhelloKhowKareKyouKdoing?"
print(s.split("K"))  # Splitting by 'K'
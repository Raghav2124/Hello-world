#Check if "free" is present in the following text
txt = "The best things in life are free!"
print("free" in txt)
print("free" not in txt)
#slicing
print(txt[2:6])
#upper case 
print(txt.upper())
print(txt.lower())
print(txt.strip())#remove whitespaces from start and end
print(txt)
a="Hello"
print(a+" "+txt)
#Almost any value is evaluated to True if it has some sort of content.
#Any string is True, except empty strings.
#Any number is True, except 0.
#Any list, tuple, set, and dictionary are True, except empty ones.
print(bool(""))
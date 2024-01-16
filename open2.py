f=open("hello.txt","r")
for x in f:
    print(x)
    # This will print every line one by one in the file

print("ALTERNATE METHOD")
f.seek(0,0)#because the file pointer is not pointing to the start of the file 
# f=open("hello.txt","r")
print(f.read())
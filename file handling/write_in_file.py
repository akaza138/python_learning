'''# write the file 
file=open("nothing.txt","w")
file.write("This is the example testing\n")
file.write("welcome\n")
file.close()

# read the file
file=open("nothing.txt","r")
content  = file.read()
print("reading the file content :",content)
file.close()

# append in the file 
file = open("nothing.txt","a")
file.write("Adding the new line\n")
file.close()
'''
# using the "with" method so you don't have to close the file manually
with open("nothing.txt","r") as file:
    for line in file :
        print(line.strip())
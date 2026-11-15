'''
user_feedback=input("enter your feedback:")
with open ("nothing.txt", "a") as file:
    file=file.write(user_feedback)
print("Thank you for you feedback")
'''

# csv file handling
with open ("file.csv","w") as file:
    while True:
        line=file.readline()
        if not line:
            break
        else:
            print(line)
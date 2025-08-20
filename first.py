name = input("Enter your name: ")
nots= input("write your notes: ")

with open("file.txt","w")as f:
    f.write("-----------------\n")
    f.write(f"Your name is: {name}\n")
    f.write(f"Your notes: {nots}\n")
    f.write("-----------------")

print("\'The data saved successfully\'\n")

with open("file.txt","r")as f:
    print(f.read())

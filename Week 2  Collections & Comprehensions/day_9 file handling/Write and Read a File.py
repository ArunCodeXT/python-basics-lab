# Step 1: Create a new file and write text into it
file = open("sample.txt", "w")
file.write("Hello! Welcome to Python file handling.\n")
file.write("This is your first file.\n")
file.close()

# Step 2: Reopen the file in read mode and display content
file = open("sample.txt", "r")
content = file.read()
print(content)
file.close()

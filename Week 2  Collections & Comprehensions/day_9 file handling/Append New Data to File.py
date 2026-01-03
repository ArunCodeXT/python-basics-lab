file = open("sample.txt", "a")
file.write("This line is newly added!\n")
file.close()

# Verify
with open("sample.txt", "r") as file:
    print(file.read())

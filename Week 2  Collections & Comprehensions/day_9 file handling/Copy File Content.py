with open("sample.txt", "r") as source:
    with open("copy.txt", "w") as dest:
        dest.write(source.read())

print("File copied successfully!")

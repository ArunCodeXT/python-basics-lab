data = ["Python\n", "Java\n", "C++\n", "JavaScript\n"]

with open("languages.txt", "w") as file:
    file.writelines(data)

print("Data written successfully!")

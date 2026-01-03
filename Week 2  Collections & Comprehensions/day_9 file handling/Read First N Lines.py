with open("sample.txt", "r") as file:
    n = 2
    for i in range(n):
        print(file.readline(), end="")

with open("sample.txt", "r") as file:
    text = file.read()
    words = text.split()
    print("Lines:", text.count('\n') + 1)
    print("Words:", len(words))
    print("Characters:", len(text))

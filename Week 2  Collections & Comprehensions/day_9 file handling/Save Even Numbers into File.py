with open("numbers.txt", "w") as f:
    for i in range(1, 21):
        f.write(str(i) + "\n")

with open("numbers.txt", "r") as f1, open("even.txt", "w") as f2:
    for line in f1:
        num = int(line)
        if num % 2 == 0:
            f2.write(str(num) + "\n")

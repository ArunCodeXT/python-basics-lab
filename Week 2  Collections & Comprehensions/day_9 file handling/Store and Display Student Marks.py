with open("students.txt", "w") as f:
    n = int(input("Enter number of students: "))
    for i in range(n):
        name = input("Enter name: ")
        marks = input("Enter marks: ")
        f.write(f"{name},{marks}\n")

# Display students scoring > 80
print("\nStudents scoring above 80:")
with open("students.txt", "r") as f:
    for line in f:
        name, marks = line.strip().split(',')
        if int(marks) > 80:
            print(name, marks)

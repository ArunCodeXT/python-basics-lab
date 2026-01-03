mark=int(input("Enter marks:"))
if mark<=100 and mark>=0 :
    if mark>=90:
        print("A")
    elif mark>=80:
        print("B")
    elif mark>=70:
        print("C")
    elif mark>=60:
        print("D")
    elif mark>=35:
        print("E")
    else:
        print("F")
else:
    print("Invalid marks")    
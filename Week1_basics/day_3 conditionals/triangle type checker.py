a=float(input("Enter side1:"))
b=float(input("Enter side2:"))
c=float(input("enter side3:"))
if a==b==c:
    print("Equilateral triangle")
elif a==b or b==c or a==c :
    print("isosceles triangle")
else:
    print("scalene triangle")
    

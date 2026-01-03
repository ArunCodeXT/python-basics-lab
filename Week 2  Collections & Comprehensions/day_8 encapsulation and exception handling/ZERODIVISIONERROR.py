try:
    a=int(input("Enetr a number:"))
    b=int(input("Enter a number:"))
    c=a/b
except ZeroDivisionError:
    print("values is divded by zero")
else:
    print("no error occured")
finally:
    print("drill2 completed")

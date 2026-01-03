try:
    num=int(input("Enetr a number:"))
    print("num",num)
except ValueError:
    print("invalid integer")
else:
    print("no error")
finally:
    print("drill1 completed")
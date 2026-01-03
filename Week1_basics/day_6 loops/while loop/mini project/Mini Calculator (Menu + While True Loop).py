while True:
    print("\n--- Calculator ---")
    print("1.Add  2.Sub  3.Mul  4.Div  5.Exit")
    ch = input("Enter choice: ")

    if ch == '5':
        print("Exiting...")
        break

    a = int(input("Enter first: "))
    b = int(input("Enter second: "))

    if ch == '1':
        print("Result:", a + b)
    elif ch == '2':
        print("Result:", a - b)
    elif ch == '3':
        print("Result:", a * b)
    elif ch == '4':
        print("Result:", a / b)
    else:
        print("Invalid choice!")

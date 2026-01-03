n = int(input("Enter a number: "))
i = 2
while i < n:
    if n % i == 0:
        print(f"{n} is not prime")
        break
    i += 1
else:
    print(f"{n} is prime")

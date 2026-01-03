a, b = 0, 1
limit = 50
while a <= limit:
    print(a, end=" ")
    a, b = b, a + b

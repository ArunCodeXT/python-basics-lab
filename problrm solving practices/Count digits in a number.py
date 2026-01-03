def count_digit(n):
    if n==0:
        return 0
    return 1+count_digit(n//10)
n=12345
print(count_digit(n))
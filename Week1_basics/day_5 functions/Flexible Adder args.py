def add_all(*nums):
    total = 0
    for n in nums:
        total += n
    return total

print(add_all(2, 4, 6))        # 12
print(add_all(10, 20, 30, 40)) # 100

s = "hello"

# strings are immutable → convert to list
arr = []
for ch in s:
    arr.append(ch)

left = 0
right = len(arr) - 1

while left < right:
    # swap
    temp = arr[left]
    arr[left] = arr[right]
    arr[right] = temp

    left += 1
    right -= 1

# convert back to string
result = ""
for ch in arr:
    result += ch

print(result)

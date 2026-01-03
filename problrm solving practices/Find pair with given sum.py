def find_pair_sorted(arr, target):
    left = 0
    right = len(arr) - 1

    while left < right:
        s = arr[left] + arr[right]

        if s == target:
            return (arr[left], arr[right])
        elif s < target:
            left += 1
        else:
            right -= 1

    return None


arr = [2, 7, 11, 15]
print(find_pair_sorted(arr, 9))

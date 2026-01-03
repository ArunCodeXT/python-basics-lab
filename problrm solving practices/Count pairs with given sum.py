def find_pair_sorted(arr, target):
    arr.sort()
    left = 0
    right = len(arr) - 1
    count=0
    while left < right:
        s = arr[left] + arr[right]
        if s == target:
            count+=1
            left+=1
            right-=1
        elif s < target:
            left += 1
        else:
            right -= 1

    return count


arr = [2, 7, 11, 15, 6, 3, 8, 1]
print(find_pair_sorted(arr, 9))

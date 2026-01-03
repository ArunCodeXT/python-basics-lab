arr1 = [1,2,3,4,5,2,3]
arr2 = [1,2,4,3,2,1,1]

merged = []

# process first array
for i in range(len(arr1)):
    found = False
    for j in range(len(merged)):
        if arr1[i] == merged[j]:
            found = True
            break
    if not found:
        merged.append(arr1[i])

# process second array
for i in range(len(arr2)):
    found = False
    for j in range(len(merged)):
        if arr2[i] == merged[j]:
            found = True
            break
    if not found:
        merged.append(arr2[i])

print(merged)

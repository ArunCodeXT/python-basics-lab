def largeste(arr,i,largest):
    if i==len(arr):
        return largest
    if arr[i]<largest:
        largest=arr[i]
    return largeste(arr,i+1,largest)
arr=[3,6,8,3,9,2]
print(largeste(arr,0,arr[0]))
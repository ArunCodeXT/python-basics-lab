def array(arr,left,right):
    if left>=right:
        return
    arr[left],arr[right]=arr[right],arr[left]
    return array(arr,left+1,right-1)
arr=[1,2,4,5,6,7,8,9]
array(arr,0,len(arr)-1)
print(arr)
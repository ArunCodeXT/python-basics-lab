def add(arr,i):
    if i==len(arr):
        return 0
    return arr[i]+add(arr,i+1)
arr=[1,2,3,4,5,6,7,8,9,10]
total=add(arr,0)
avg=total/len(arr)
print(avg)

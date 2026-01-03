def duplicates(arr,i,seen,list):
    if i == len(arr):
        return list
    if arr[i] not in seen:
        seen.add(arr[i])
        list.append(arr[i])
    return duplicates(arr,i+1,seen,list)
arr=[1,1,3,3,4,5,3]
lst=duplicates(arr,0,set(),[])
print(lst)
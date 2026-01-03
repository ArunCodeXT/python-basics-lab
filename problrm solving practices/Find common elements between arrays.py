arr=[1,2,3,4,5,2,3]
arr2=[1,2,4,3,2,1,1]
lst=[]
i=0
while i<len(arr):
    j=0
    while j<len(arr2):
        lst.append(arr[i]+arr2[j])
        break
    i=i+1
print(lst)

    


























arr=[1,1,2,2,3,3,4]
n=len(arr)
if n==0:
    print([])
else:
    i=0
    j=1
    while j<n:
        if arr[i]!=arr[j]:
            i+=1
            arr[i]=arr[j]
        j+=1
result=[]
k=0
while k<=i:
    result.append(arr[k])
    k+=1
print(result)
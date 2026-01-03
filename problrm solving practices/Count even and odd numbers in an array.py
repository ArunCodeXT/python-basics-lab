'''
arr=[1,3,4,5,6,7,89,45,67]
countodd=0
counteven=0
for i in range(len(arr)):
    if arr[i]%2==0:
        counteven+=1
    else:
        countodd+=1
print("odd=",countodd)
print("even=",counteven)
'''
def oddeven(arr,i):
    if i==len(arr):
        return 0,0
    even,odd=oddeven(arr,i+1)
    if arr[i]%2==0:
        return even+1,odd
    else:
        return even,odd+1
arr=[2,3,4,85,9,8]
even,odd=oddeven(arr,0)
print(odd)
print(even)

    

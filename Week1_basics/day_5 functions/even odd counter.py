def count_even_odd(nums):
    odd=0
    even=0
    for n in nums:
        if n%2==0 :
            odd+=1
        else:
            even+=1
    return odd,even
o,e=count_even_odd([1,2,3,4,5,6,7,8,9,10])
print("odd=",o,"even=",e,end='')
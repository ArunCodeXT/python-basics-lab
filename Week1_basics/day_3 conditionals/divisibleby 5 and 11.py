n=int(input("Enter no:"))
if n%5==0 and n%11==0 :
    print("divisible by 5 and 11")
elif n%5!=0 and n%11==0 :
    print("only divisible by 11")
elif n%5==0 and n%11!=0 :
    print("only divisible by 5")
else:
    print("not  divisible by both 5 anad 11")
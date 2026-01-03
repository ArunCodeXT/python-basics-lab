cp=float(input("Enter cost price:"))
sp=float(input("Enter selling price:"))
if cp<sp :
    print("profit ₹",sp-cp)
elif cp>sp :
    print("loss ₹",cp-sp)
else:
    print("no loss")
cname=input("customer name:")
age=int(input("enter age:"))
amount=float(input("total bill amount:"))
discount=''
if 0<age<18:
    print("not eligible for discounts")
    membership='--'
    couponcode='--'
    ttamount=amount
    discount=0
    discount1=0
    gst=amount*0.18
    finalamount=amount+gst
elif age>=18 :
    print("membership status(1.yes/2.no)")
    mship=input()
    if mship=='1':
        membership='yes'
    elif mship=='2':
        membership='no'
    else:
        membership='invalid'
    print("coupon code(optional choice:SAVE10,SAVE20,FREESHIP)")
    ccode=input()
    if ccode=='1':
        couponcode='SAVE10'
    elif ccode=='2':
        couponcode='SAVE20'
    elif ccode=='3':
        couponcode='FREESHIP'
    else:
        couponcode="invalid coupon"
    if mship=='1':
        if amount>=5000:
            discount=amount*0.20
            tamount=amount-discount
        elif amount>=2000:
            discount=amount*0.10
            tamount=amount-discount
        else:
            discount=0
            tamount=amount-discount
    elif mship=='2':
        discount='0.00(no discount is apllied)'
        tamount=amount-0.00
    else:
        dicount='no discount'
        tamount='error'
    if ccode=='1':
        discount1=tamount*0.10
        ttamount=tamount-discount1
    elif ccode=='2':
        if amount>=4000 :
            discount1=tamount*0.20
            ttamount=tamount-discount1
        else:
            discount1='0.00(only if amount>=4000)'
            ttamount=tamount-0.00
    elif ccode=='3':
        discount1='100.00(you get free delivery worth ₹100)'
        ttamount=tamount-100.00
    else:
        discount='invalid coupon'
        ttamount=0.00
    gst=ttamount*0.18
    finalamount=ttamount+gst
    print("customer Name:",cname)
    print("Age:",age)
    print("original amount:₹",amount)
    print("membership(yes/no)",membership)
    print("membership discount:₹",discount)
    print("coupon code:",couponcode)
    print("coupon discount:₹",discount1)
    print("After discount:",ttamount)
    print("GST:₹",gst)
    print("final payment amount:₹",finalamount)
else:
    print("invalid age")



year=int(input("Entr year:"))
if year>0 :
    if (year%100!=0 and year%4==0) or year%400==0 :  #logic:it is used to find leap year in century years like 2000,1900 otherwise it will not show accurate output for century years
        print("leap year")
    else:
        print("not leap year")
else:
    print("invalid year")


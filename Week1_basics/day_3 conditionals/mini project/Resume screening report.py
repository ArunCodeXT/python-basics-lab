name=input("Name:")
age=int(input("Age:"))
experience=float(input("Experience(in yrs):"))
print("skill:(1.python/2.java/3.sql/4.c++)")
skill=input()
print("Education(choose:1.BTech,2.MTech,3.Diploma,4.Other)")
education=input()
skill1=''
if skill=='1':
    skill1='Python'
elif skill=='2':
    skill1='Java'
elif skill=='3':
    skill1='SQL'
elif skill=='4':
    skill1='C++'
else:
    skill1='no skill'
education1=''
if education=='1':
    education1='BTech'
elif education=='2':
    education1='MTech'
elif education=='3':
    education1='Diploma'
elif education=='4':
    education1='Other'
else:
    education1+"no qualification"
result=''
if (age>=21 or age<=35) and experience>=2 and (skill=='1' or skill=='3') and (education=='1' or education=='2'):
    result='selected!'
elif (age>35 or age<20) and experience==1 and (skill=='4' or skill=='2') and education=='3' :
    result='Needs Review - Not enough experience or mismatched skill.'
elif experience<1 and education=='4':
    result='Rejected due to lack of experience.'
else:
    result='invalid details'
print("Resume Screening Report")
print("-----------------------")
print("Name:",name)
print("Age:",age)
print("Experience:",experience,"years")
print("Skill:",skill1)
print("Education:",education1)
print("Result:",result)




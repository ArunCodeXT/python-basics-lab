class College:
    name = "IIT Chennai"   # class variable

# create 2 students
s1 = College()
s2 = College()

print(s1.name)   # IIT Chennai
print(s2.name)   # IIT Chennai

College.name = "NIT Trichy"  # change for all
print(s1.name)   # NIT Trichy

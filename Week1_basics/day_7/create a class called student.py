class student:
    def __init__(self,name,regno):
        self.name=name
        self.regno=regno
    def display(self):
        print("student name:",self.name)
        print("student regno:",self.regno)
s1=student("luffy",2345)
s1.name="sanji"
s1.display()

s2=student("zoro",3333)
s2.display()

class Father:
    def car(self):
        print("Owns BMW")

class Son(Father):
    def bike(self):
        print("Owns KTM")

class Daughter(Father):
    def laptop(self):
        print("Has MacBook")

s = Son()
d = Daughter()
s.car(); s.bike()
d.car(); d.laptop()

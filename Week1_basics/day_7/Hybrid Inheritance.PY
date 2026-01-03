class GrandFather:
    def land(self):
        print("Has land")

class Father(GrandFather):
    def car(self):
        print("Has car")

class Mother:
    def house(self):
        print("Has house")

class Son(Father, Mother):
    def bike(self):
        print("Has bike")

s = Son()
s.land()
s.car()
s.house()
s.bike()

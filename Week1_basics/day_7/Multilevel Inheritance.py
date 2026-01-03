class GrandFather:
    def house(self):
        print("Owns a big house")

class Father(GrandFather):
    def car(self):
        print("Owns a car")

class Son(Father):
    def bike(self):
        print("Owns a bike")

s = Son()
s.house()
s.car()
s.bike()

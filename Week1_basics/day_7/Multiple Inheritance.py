class Father:
    def car(self):
        print("Has a car")

class Mother:
    def house(self):
        print("Has a house")

class Child(Father, Mother):
    def bike(self):
        print("Has a bike")

c = Child()
c.car()
c.house()

c.bike()
c.bike()
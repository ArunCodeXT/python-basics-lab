class Car:
    def show(self):
        print("Brand:", self.brand)
        print("Color:", self.color)

c1 = Car()
c1.brand = "BMW"
c1.color = "Black"

c2 = Car()
c2.brand = "Audi"
c2.color = "Red"

c1.show()
c2.show()

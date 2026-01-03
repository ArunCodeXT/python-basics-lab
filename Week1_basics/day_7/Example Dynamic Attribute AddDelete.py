class Dog:
    def bark(self):
        print(self.name, "is barking!")

d = Dog()
d.name = "Tommy"
d.bark()

del d.name  # delete attribute

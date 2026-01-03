class calculator:
    def __init__(self,a,b):
        self.a=a
        self.b=b 
    def add(self):
        print("sum:",self.a+self.b)
    def sub(self):
        print("sub:",self.a-self.b)
    def multiply(self):
        print("multiply:",self.a*self.b)
    def division(self):
        print("division:",self.a/self.b)

calc=calculator(1,2)
calc.add()
calc.sub()
calc.multiply()
calc.division()
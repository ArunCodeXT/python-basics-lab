class employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
class manager(employee):
    def __init__(self,name,salary,department):
        super().__init__(name,salary)
        self.department=department
    def display(self):
        print("name:",self.name)
        print("salary:",self.salary)
        print("department:",self.department)
call=manager("luffy",50000,"cse")
call.display()

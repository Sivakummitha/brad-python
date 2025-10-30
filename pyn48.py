#Create a class employee with name, age, and salary attributes, where salary must be a private attribute that cannot be accessed outside the class.
class employye:
    def __init__(self,name,age,salary):
        self.name=name
        self.age=age
        self.salary=salary
    def display(self):
        print("name: ",self.name)
        print("age: ",self.age)
        print("salary: ",self.salary)
    def get_salary(self):
        return self.salary
    def set_salary(self,new_salary):
        if new_salary>0:
            self.salary=new_salary
        else:
            print("no salary")
emp1=employye("siva",21,25000)
emp1.display()
print(emp1.get_salary)
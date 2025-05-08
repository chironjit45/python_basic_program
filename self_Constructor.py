class Employee:
    no_of_leaves = 8

    def printdetails(self):
        return f"Name is {self.name}. Salary is {self.salary} and Role is {self.role}"
hiro = Employee()
ritu = Employee()

hiro.name = "Hiro"
hiro.salary = 5432
hiro.role = "Instructor"

print(hiro.printdetails())




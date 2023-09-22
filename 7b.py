class Employee:
    def __init__(self):
        self.name=" "
        self.empid=" "
        self.depid=" "
        self.salary=0
        
    def employread(self):
        self.name=input("enter the name of the employee:")
        self.empid=input("enter the employee id:")
        self.depid=input("enter the dept id:")
        self.salary=float(input("enter the salary of the employee:"))
        
    def empdisplay(self):
        print("the name of the employee:",self.name)
        print("employee id:",self.empid)
        print("dept id:",self.depid)
        print("salary of the employee:",self.salary)
    
    def updatesalary(self):
        self.salary=float(input("enter the salary of the employee:"))
        print("updated salary of the employee:",self.salary)

e1=Employee()
e1.employread()
e1.empdisplay()
e1.updatesalary()
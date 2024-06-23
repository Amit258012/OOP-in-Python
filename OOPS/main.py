from abstraction import Nokia
from encapsulation import Employee
from inheritance import Manager
from inheritance_dev import Developer
from multiple_inheritance import FlyingCar

# Encapsulation Examples
emp1 = Employee("Amit", "Jahagirdar", 1000000)
emp2 = Employee("Vinit", "Jahagirdar", 5000000)
emp1.fullName = "Amruta Kulkarni"

print(emp1.email)
print(emp1.fullName)
del emp1.fullName

# Inheritance Examples
dev1 = Developer("Amit", "Jahagirdar", 1000000, "Python")
dev2 = Developer("Vinit", "Jahagirdar", 5000000, "JavaScript")

# Manager Examples
mgr_1 = Manager("Sue", "Smith", 90000, [dev1])
mgr_1.add_employee(dev2)
mgr_1.print_employee()
mgr_1.remove_employee(dev1)
mgr_1.print_employee()

# Abstraction Examples
phone = Nokia("nokia 1100")
print(phone.power)
print(phone.call_target("Amit"))

# Multiple Inheritance Examples
flying_car = FlyingCar()
flying_car.start()

'''
class A:
    def test(self):
        print("This is instance method")
obj = A()
obj.test()      

class Bank:
    def __init__(self):
        print("This is constructor")
    def test1(self):
        print("Instances method")
    def test2(self):
        print("Instances method")
obj = Bank()
obj.test1()
obj.test2()     

class Bank:
    def __init__(self):
        print(self) #Store the object refernce
obj = Bank()        

class Bank:
    def __init__(self, An, Name, Branch):
        self.An = An
        self.Name = Name
        self.Branch = Branch
    def get_name(self):
        return self.Name
    def get_branch(self):
        return self.Branch
    def set_branch(self, new_branch):
        self.Branch = new_branch
obj = Bank(100, "sai", "SBI")
print(obj.get_name())
print(obj.get_branch())
obj.set_branch("ABC")
print(obj.get_branch())
print(obj.set_branch())     

import re
class Bank:
    def __init__(self, An, Name, Branch):
        self.An = An
        self.Name = Name
        self.Branch = Branch
    def get_branch(self):
        return self.Branch
    def set_branch(self, new_branch):
        exp = "^[A-Z]{3}$"
        if re.search(exp, str(new_branch)):
            self.Branch = new_branch
        else:
            print("Invalid Branch:", new_branch)
obj = Bank(101, "sai", "ABC")
print(obj.get_branch())
obj.set_branch("ABB")
obj.set_branch("qwe")
print(obj.get_branch())     

import re
class Bank:
    def __init__(self, An, Name, Branch):
        self.__An = An              #Private Attributes
        self.__Name = Name          #Private Attributes
        self.__Branch = Branch      #Private Attributes
        
    def get_branch(self):
        return self.__branch
    def set_branch(self, new_branch):
        exp = "^[A-Z]{3}$"
        if re.search(exp, str(new_branch)):
            self.branch = new_branch
        else:
            print("Invalid Branch:", new_branch)
    def get_an(self):
        return self.__An
obj = Bank(100, "sai", "ABC")
print(obj.get_an())         
        
class Bank:
    def __init__(self, An, Name, Branch):
        self.An = An
        self.Name = Name
        self.Branch = Branch
    def get_name(self):
        return "0 " + self.Name

class Salary(Bank):
    def __init__(self, An, Name, Branch, Balance, Emp):
        Bank.__init__(self, An, Name, Branch)
        self.Balance = Balance
        self.Emp = Emp
    def get_balance(self):
        return 0  + self.Balance
obj = Salary(100, "SAI", "SBI", 100000, "Acct")
print(obj.get_balance())
print(obj.get_name())           

class Bank:
    def __init__(self, An, Name, Branch):
        self.An = An
        self.Name = Name
        self.Branch = Branch
    def get_Name(self):
        name = self.Name
        return name
    
    def set_branch(self, new_branch):
        self.Branch = new_branch
    def get_branch(self):
        return self.Branch
        
class Salary(Bank):
    def __init__(self, An, Name, Branch, Balance, Emp):
        Bank.__init__(self, An, Name, Branch)
        #super().__init__(self, An, Name, Branch)
        self.Balance = Balance
        self.Emp = Emp
        
    def show_balance(self):
        return self.Balance
    def deposit(self, amount):
        if isinstance(amount, int) and amount>=100:
            print("Deposit successfully", amount)
            self.Balance = self.Balance + amount
        else:
            print("Please deposit 100 above", amount)
                 
    def withdraw(self, amt):
        if isinstance(amt, int) and amt >= 100:
            print("Deposit successfully", amt)
            if self.Balance >= amt:
                self.Balance = self.Balance -   amt
            else:
                print("Insufficient balance", self.Balance, "Could not withdraw", amt)
        else:
            print("Could not withdraw", amt)

if __name__ == "__main__":
    obj = Salary(11, "lahari", "SBI", 1000, 22)
    print(obj.get_Name())
    obj.set_branch("ICICI")
    print(obj.get_branch())
    print(obj.show_balance())
    obj.deposit(199)
    print(obj.show_balance())
    x = obj.withdraw(500)
    print(obj.show_balance())       


class A:
    def test(self):
        print("A")
class B(A):
    def test(self):
        print("B")
class C(A):
    def test(self):
        print("C")
class D(B,C):
    def test(self):
        super().test()
        print("D")
obj = D()
obj.test()      

class Office:
    count = 0
    def __init__(self, Name):
        self.Name = Name
        Office.count = Office.count+1
a = Office("Sai")
b = Office("aa")
c = Office("s")
print(Office.count) 

class Bank:
    count = 0
    def __init__(self, Name):
        self.Name = Name
        Bank.count = Bank.count + 1
    def get_count(self):
        print(self)
        return Bank.count
    @classmethod
    def counter(self):
        print(self)
        return self.count
        
    @staticmethod
    def add(a,b):
        return a+b
b1 = Bank("A")
out = b1.add(10,20)
print(out)

print(Bank.add(10,30))      

#Single Inheritence:
class Parent:
    def display(self):
        print("This parent class")
class Child(Parent):
    def a(self):
        Parent.display(self)
        print("Child class")
obj = Child()
obj.a()
#obj.display()          

class Parent:
    def display(self):
        print("This is parent class")
class Child(Parent):
    def display(self):
        Parent.display(self)
        print("This is child class")
obj = Child()
obj.display()       

class Parent:
    def __init__(self):
        print("Parent class constructor")
class Child(Parent):
    def __init__(self):
        Parent.__init__(self)
        print("Child class constructor")
obj = Child()       

class Parent:
    def __init__(self, Name):
        self.Name = Name
class Child(Parent):
    def display(self):
        print(f'Name: {self.Name}')
obj = Child("sai")
obj.display()       

class Parent:
    def display(self, msg):
        print(f'parent says: {msg}')
class Child(Parent):
    def display(self, msg):
        Parent.display(self, msg)
        print(f'child says: {msg}')
obj = Child()
obj.display("sai")      

class Parent:
    def __init__(self, name):
        self.name = name
class Child(Parent):
    def get_name(self):
        return self.name
obj = Child("Hello")
print(obj.get_name())   

class Parent:
    def display(self):
        print("This is parent class")
class Child(Parent):
    def additional_method(self):
        Parent.display(self)
obj = Child()
#obj.display()
obj.additional_method()     

class Parent:
    def __init__(self, name):
        self.name = name
class Child(Parent):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age
    def display(self):
        print(f'Name: {self.name}, Age: {self.age}')
obj = Child("sai", 25)
obj.display()       

class Parent:
    var1 = "sao"
class Child(Parent):
    var2 = "hi"
obj = Child()
print(obj.var1)
print(obj.var2)     

class Parent:
    def display(self):
        print("This is parent class")
        return self
class Child(Parent):
    def additional_method(self):
        print("child method")
        return self
obj = Child()
print(obj.display())        

from abc import ABC, abstractmethod
class Parent:
    @abstractmethod
    def abstract_method(self):
        pass
class Child(Parent):
    def abstract_method(self):
        print("Implemented abstract method")
obj = Child()
obj.abstract_method()       

#Single Inheritences with Data Validation:
class Parent:
    def __init__(self, name):
        if not isinstance(name, str):
            raise ValueError("Name must be string")
        self.name = name
class Child(Parent):
    def __init__(self, name, age):
        super().__init__(name)
        if not isinstance(age, int):
            raise ValueError("Age must be integer")
        self.age = age
    def display(self):
        print(f'Name: {self.name}, Age: {self.age}')
obj = Child("ABC", 123)
obj.display()       

class Employee:
    def __init__(self, name, emp_id):
        self.name = name
        self.emp_id = emp_id
    def display(self):
        print(f"Name: {self.name}, Id: {self.emp_id}")
class Developer(Employee):
    def __init__(self, name, emp_id, program_language):
        super().__init__(name, emp_id)
        self.program_language = program_language
    def display(self):
        super().display()
        print(f"Program: {self.program_language}")

dev = Developer("sai", 100, "py")
dev.display()       

class Animal:
    def __init__(self, name):
        self.name = name
    def speak(self):
        return f"{self.name} say hello!"
class Dog(Animal):
    def speak(self):
        super().speak()
        return f"{self.name} say woof!"
class Labrador(Dog):
    def speak(self):
        super().speak()
        return f"{self.name} says Bark!"
obj = Labrador("Lab")
print(obj.speak())      

#Multi-level inheritence with constructor:

class Vechile:
    def __init__(self, brand):
        self.brand = brand
    def display_info(self):
        print(self.brand)
class Car(Vechile):
    def __init__(self, brand, model):
        Vechile.__init__(self, brand)
        self.model = model
    def display_info(self):
        super().display_info()
        print(f"Model: {self.model}")
        
class ElectricCar(Car):
    def __init__(self, brand, model, battery_capacity):
        super().__init__(brand, model)
        self.battery_capacity = battery_capacity
    def display_info(self):
        super().display_info()
        print(f"Battery_Capacity: {self.battery_capacity}")
        #super().display_info()
obj = ElectricCar("Tata Nexon", 2024, "5000kmphs")
obj.display_info()      

#Diamond problem in multi-level inheritences:

class A:
    def method(self):
        return "A method"
class B(A):
    def method(self):
        return "B method"
class C(A):
    def method(self):
        return "C method"
class D(B,C):
    def method(self):
        pass
obj = D()
print(obj.method())     

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def display_info(self):
        return f"Name: {self.name}, Age: {self.age}"
class Employee(Person):
    def __init__(self, name, age, salary):
        Person.__init__(self, name, age)
        self.salary = salary
    def display_info(self):
        return f"Name: {self.name}, Age: {self.age}, Salary: {self.salary}"
class Manager(Employee):
    def __init__(self, name, age, salary, department):
        super().__init__(name, age, salary)
        self.department = department
    def display_info(self):
        return f"Name: {self.name}, Age: {self.age}, Salary: {self.salary}, Department: {self.department}"
obj = Manager("sai", 30, 55000, "IT")
print(obj.display_info())       

class Printable:
    def print_info(self):
        return f"Printable Information: {self.info}"
class JSONMixin:
    def to_json(self):
        return {"info": self.info}
class XMLMixin:
    def to_xml(self):
        return f"<info>{self.info}</info>"
class DataObject(Printable, JSONMixin, XMLMixin):
    def __init__(self, info):
        self.info = info
data = DataObject("SampleData")
print(data.print_info())
print(data.to_json())
print(data.to_xml())        

#Abstract Method:
from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height
class Square(Rectangle):
    def __init__(self, width, height,side):
        super().__init__(width, height)
sqr = Square(5)
print(sqr.area())       

#Overridding with multi-level inheritence:
class A:
    def method(self):
        print("A method")
class B(A):
    def method(self):
        print("B method")
        super().method()
class C(B):
    def method(self):
        super().method()
        print("C method")
obj = C()
obj.method()   

#Multi inheritence:
class A:
    def method_A(self):
        return "A method"
class B:
    def method_B(self):
        return "B method"
class C(B, A):
    def method_C(self):
        return "C method"
obj = C()
print(obj.method_C())       

class Vechicle:
    def __init__(self, brand):
        self.brand = brand
    def display_info(self):
        return "Brand:" + self.brand
        
class Engine:
    def __init__(self, fuel_type):
        self.fuel_type = fuel_type
    def engine_info(self):
        return f"Fuel Type: {self.fuel_type}"
        
class Car(Vechicle, Engine):
    def __init__(self, brand, fuel_type, model):
        Vechicle.__init__(self, brand)
        Engine.__init__(self, fuel_type)
        self.model = model
    def display(self):
        return f"{self.display_info()}, {self.engine_info()}, Model:{self.model}"
        
obj = Car("Tata", "Petrol", 2024)
print(obj.display())        

#Diamond Pattern:
class A:
    def method(self):
        print("A Method")
        
class B(A):
    def method(self):
        print("B Method")
        super().method()
class C(A):
    def method(self):
        print("C Method")
        super().method()
class D(B, C):
    def method(self):
        print("D Method")
        super().method()
obj = D()
print(obj.method())     
        
class Printable:
    def print_info(self):
        return f"Printable Information: {self.info}"
class JSONMixin:
    def json_info(self):
        return f"info: {self.info}"
class XMLMixin:
    def to_xml(self):
        return "f<info>{self.info}</info>"
class DataObject(Printable, JSONMixin, XMLMixin):
    def __init__(self, info):
        self.info = info
if __name__ == "__main__":
    obj = DataObject("Sample DATa")
    print(obj.print_info())         
    
from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height
class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height
    def area(self):
        return 0.5*self.base*self.height
class square(Rectangle, Triangle):
    def __init__(self, side):
        Rectangle.__init__(self, side, side)
        Triangle.__init__(self, side, side)
obj = square(5)
print(obj.area())           

class Animal:
    def __init__(self, speices):
        self.speices = speices
    def speak(self):
        pass
class Dog(Animal):
    def speak(self):
        return "woof"
class Cat(Animal):
    def speak(self):
        return "Meow"
obj = Dog("LAB")
obj1 = Cat("Pilli")
print(obj.speices+obj.speak())  

class Shape:
    def area(self):
        pass
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14*self.radius**2
class Square(Shape):
    def __init__(self, side):
        self.side = side
    def area(self):
        return self.side**2
obj = [Circle(8), Square(10)]
for item in obj:
    print(item.area())      
    
class India:
    def capital(self):
        return "New Delhi"
    def language(self):
        return "Hindi"
class USA:
    def capital(self):
        return "Washington, D.C"
    def language(self):
        return "English"
def print_details(country):
    print("Capital:", country.capital())
    print("Language:", country.language())
country = [India(), USA()]
for count in country:
    print_details(count)        
    
#Duck Typing in python:
class Parrot:
    def fly(self):
        return "Parrot can fly"
class Airplane:
    def fly(self):
        return "Airplane can fly"
class Whale:
    def swim(self):
        return "Whale can swim"
def can_fly(obj):
    if hasattr(obj, 'fly'):
        return obj.fly()
    else:
        return "These object cannot fly"
objects = [Parrot(), Airplane(), Whale()]
for obj in objects:
    print(can_fly(obj))     '''
    
    
fr = open(r"D:\Saiiiiiiiiiiii\Python_Practise\pythonProject1\excel_data.xlsx")
x = fr.read()
fr.close()
print(x)
    

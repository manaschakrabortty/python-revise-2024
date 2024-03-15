# class Student:#class
#     name="manas"

# s1=Student()#object
# print(s1.name)


# class Car:
#     color= "blue"
#     brand= "AUDI"

# car1=Car()
# print(car1.color)


#CONSTRUCTORS

# class Student:


    #DEFAULT CONSTRUCTORS
    # def __init__(self):
    #     pass

    #PARAMETERIZED CONSTRUCTORS
#     def __init__(self, fullname,marks) :
#         self.name = fullname
#         self.marks= marks
#         print("adding a new data ")

# s1= Student("Manas",99)
# print(s1.name,s1.marks)

# s2= Student("purbasa",98)
# print(s1.name, s2.marks)


# class Student:
#     collage_name="ABC COLLAGE"
#     name= "anything"#class attr
#     def __init__(self, fullname,marks) :
#             self.name = fullname#obj attr>class attr
#             self.marks= marks
#             print("adding a new data ")

# s1= Student("Manas",97)
# print(s1.name)           

#Q1) CREATE STUDENT CLASS THAT TAKES NAME & MARKS OF 3 SUBJECT AS ARGUMENTS IN A CONSTRUCTOR ,THEN CREATE A MEHOD TO PRINT THE AVERAGE
# class Student:
#     def __init__(self,name,marks):
#         self.name = name
#         self.marks = marks 
#     def get_avg(self):
#         sum=0
#         for val in self.marks:
#             sum += val
#             print("hii",self.name,"ur avg is ",sum/3)
# s1 = Student("manas",[99,98,99])
# s1.get_avg()

#STATIC METHOD
# @staticmethod
# def hello():
#     print("hello")
# s1.hello() 
#OOPS
#1) ABSTRACTION 2) ENCAPSULATION 3) INHERITANCE 4) POLYMORPHISM




# CREATE ACCOUNT CLASS WITH 2 ATTRIBUTES - BALANCE &ACCOUNTS NO. CEATE METHODS FOR DEBIT, CREDIT& PRINTING THE BALANCE.
# class Account:
#     def __init__(self,bal,acc):
#         self.balance = bal
#         self.account_no = acc

#     def debit(self, amount):
#         self.balance -= amount
#         print("RS ", amount, "was debited")
#         print("total balance =", self.get_balance())

#         def credit(self, amount):
#             self.balance += amount
#             print("RS ", amount, "was credited")
#             print("total balance =", self.get_balance())

#         def get_balance(self):
#             return self.balance
        
#         acc1 = Account(1000,12345)
#         acc1.debit(1000)
#         acc1.credit(300)
        

#del keyword
# class Student:
#     def __init__(self, name):
#         self.name = name

# s1 = Student("manas")
# print(s1.name)
# del s1.name
# print(s1.name)

#private attr,methods
# class Person:
#     __name = "anonymous"
#     def __hello():
#         print("hii person")
# p1= Person()
# print(p1.__name)


#INHERITANCE

# class Car:
#     @staticmethod
#     def start():
#         print("start..")
    
#     @staticmethod
#     def stop():
#         print("stop..")


# class Toyotacar(Car):
#     def __init__(self,name):
#         self.name= name
# car1=Toyotacar("fortuner")
# car2=Toyotacar("prius")
# print(car1.name)


#MULTI-LEVEL INHERITANCE
# class Car:
#     @staticmethod
#     def start():
#         print("start..")
    
#     @staticmethod
#     def stop():
#         print("stop..")


# class Toyotacar(Car):
#     def __init__(self,brand):
#         self.brand= brand

# class Fortuner(Toyotacar):
#     def __init__(self, type):
#         self.type= type

# car1= Fortuner("disel")
# car1.start()

#MULTIPLE INHERITANCE
# class A:
#     varA = "WELCOME TO A"
# class B:
#     varB = "WELCOME TO B"
# class C(A,B):
#     varC = "WELCOME TO C"
# c1= C()
# print(c1.varC)
# print(c1.varB)
# print(c1.varA)

#CLASSMETHOD

# class Person:
#     name="anonymous"

#     # def changeName(obj, name):
#     #     self.__class__.name = "rahul"
#     @classmethod
#     def changeName(cls,name):
#         cls.name = name

# p1=Person()
# p1.changeName("rahul kumar")
# print(p1.name)
# print(Person.name)




# class Student:
#     def __init__(self,phy,chem,math):
#         self.phy=phy
#         self.chem=chem
#         self.math= math
#         self.persentage=str((self.phy + self.chem + self.math) /3)+"%"
# stu1=Student(98,99,97)
# print(stu1.persentage) 



#PROPERTY METHOD

# class Student:
#     def __init__(self,phy,chem,math):
#         self.phy=phy
#         self.chem=chem
#         self.math= math

#         # self.persentage=str((self.phy + self.chem + self.math) /3)+"%"
#     @property
#     def persentage(self):
#         return str((self.phy + self.chem + self.math) /3)+"%"

# stu1=Student(98,99,97)
# print(stu1.persentage) 
# stu1.phy= 89
# print(stu1.persentage)


#POLYMORPHISM : OPERATOR OVERLOADING
# class Complex:
#     def __init__(self,real,img):
#         self.real=real
#         self.img = img

#     def showNumber(self):
#         print(self.real,"i +",self.img,"j")

# num1=Complex(1,3)
# num1.showNumber()
# num1=Complex(5,8)
# num1.showNumber()


# class Complex:
#     def __init__(self,real,img):
#         self.real=real
#         self.img = img

#     def showNumber(self):
#         print(self.real,"i +",self.img,"j")

#     def __add__(self, num2):
#         newReal= self.real + num2.real
#         newImg = self.img +num2.img
#         return Complex(newReal,newImg)

# num1=Complex(1,3)
# num1.showNumber()

# num1=Complex(5,8)
# num1.showNumber()

# num3=num1 + num2
# num3.showNumber()



#Q1) DEFINE A CIRCLE CLASS TO CREATE A CIRCLE WITH RADIUS r USING THE CONSTRUCTOR
        #DEFINE AN AREA() METHOD OF THE CLASS WHICH CALCULATE THE AREA OF THE CIRCLE
        # DEFINE A PARAMETER () METHOD OF THE CLASS WHICH ALLLOWS YOU TO CALCULATE THE PERIMETER OF THE CIRCLE


# class Circle:
#     def __init__(self,radius):
#         self.radius= radius


#     def area(self):
#         return 3.14 * self.radius **2
    
#     def perimeter(serlf):
#         return 2* 3.14 *serlf.radius


# c1= Circle(21)
# print(c1.area())
# print(c1.perimeter())


# #q)
# class Order:
#     def __init__(self, item, price):
#         self.item = item
#         self.price = price
        
#     def __gt__(self,odr2):
#         return self.price > odr2.price
    
# odr1 = Order("chips", 20)
# odr2 = Order("tea", 14)

# print(odr1 > odr2)
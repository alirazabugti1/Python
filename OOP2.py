#deleting object
# class Student:
#     def __init__(self,name):
#         self.name=name

# s1=Student("Ali Raza")

# print(s1.name)


# del s1 #will delete object

# print(s1.name) #Will Give Error here because deleted before.


#Encapsulation

# class Account:

#     def setter(self,balance,__accountnumber):
#         self.balance=balance
#         self.__accountnumber=__accountnumber

#     def secretmethod(self):
#         print("I am secret you can't acess Me")

# s1=Account()
# s1.setter(15000,1111)
# print(s1.balance) #will print
# print(s1.__accountnumber) #throws error because accountnumbe is private as delcare using __


# s1.secretmethod()

#Inheritance

class Car:
    @staticmethod
    def start():
        print("Starting Car:")
    @staticmethod
    def stop():
        print("Stopping Car")

class Toyota(Car): #Inherited From Car class
    def __init__(self,name):
        self.name=name

car1=Toyota("Fortuner")
car2=Toyota("Pajero")

print("Car1 Info:")
car1.start()
car1.stop()
print(car1.name)


print("Car2 Info:")
car2.start()
car2.stop()
print(car2.name)

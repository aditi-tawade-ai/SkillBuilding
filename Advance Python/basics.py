'''
# docstring- used for multiline comment
----------------------------------------------
Class and Object

Class- is a template , blueprint, structure used to create an object
class = properties(variables) + behaviour(methods)
--------------------------------

class Car:
    # properties
    doors = 4
    engine = 1
    e_name = 'turbo'

    # behaviour- operations
    def drive(self):
        print('Drive the car')
    
    def drift(self):
        print('Drift the car')
        
# Object- Is an entity which phsically exist in the memory
# Def- Object is an instance of a class
# call the class to create an object
bmw = Car()
# bmw = object   # Car()---> constructor used to allocate a memory
print(bmw.e_name)
bmw.drive()
 ----------------------------------------

class Human:
    eyes = 2
    head = 1
    hands = 2

    def walk(self):
        print('Walking')
        print('Head:',self.head)
        print('Eyes:',self.eyes)

# how many objects we can create--> We can create N objects
prasad = Human()
print('Head:',prasad.head)
prasad.walk()

ravan = Human()
ravan.head = 10
print('Head:',ravan.head)
------------------------------------------

Q. what is self- 
ans: it is a reference variable of a method
who is responcible for accessing  members of a class 
inside a method
-----------------------------------

class Human:
    eyes = 2
    head = 1
    hands = 2

    def sample(self):
        print("Hello GM")

    def info(self):
        print('Eyes:',self.eyes)
        print('Head:',self.head)
        print('Hands:',self.hands)
        # call sample inside info
        self.sample()
# To access the members outside the class 
# we need an Object
h1 = Human()
h1.info()
#h1.sample()

-------------------------------------------

Q. What is Constructor?
- Constructor is nothing but a class calling
- It is used to allocate a memory- to create an object
- In OOP when we call a constructor then it calls __init__() method
-------------------------------------------
'''

class Test:
    def __init__(self):
        print('Constructor calling....')
t1 = Test()  # class calling= constructor calling
t2 = Test()
t1.__init__()
# __init__ is a magic method which is also called as
# dunder method --> double underscore in prefix and suffix


# Q. what is difference between method and function?

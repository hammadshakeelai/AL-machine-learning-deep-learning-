# class Car:
#     #functions in class must accept self as parameter (required)
#     #self is a refrence to the current object
#     #
#     def __init__(self,name=""):# ,*args,**kwargs
#         self.name=name
#     def Horn(self):
#         print("Beeeeeppp...")
#     def travel(self):
#         print("traveling...")
#     def display(self):
#         print(f'this is a {self.name} car')
#         return 1
#
# car = Car("ferrari")
# car.Horn()#Car.Horn(car)
# car.travel()
# # print(car.name)
# print(car.display())
# ################################
# libraries are a class
# 1. Do I need multiple independent Instances each holding their own data?  
# 2. Does the concept bundle related Data **and** Behavior together?  
# 
# 3. Will I need to extend or Customize it via Inheritance later?  
# 4. Do I need to preserve state across method calls?  
# 5. Will Grouping it into a Class improve Readability and Maintenance (not messy)?  
# class Library:
#     pass
# class Rack(Library):
#     pass#theme
# class Book(Rack):
#     pass#name, index on rack, author
##############
# class Student:
#     def __init__(self,name,age,marks):#constructor// init stands for initialized
#         text = "text t"#local variable
#         # all global variables are initialized in init but not required can be initalized in other function but it needs to be called before the value is
#         # in  constructor they are initialized automatically at object creation        
#         self.name=name#global variables
#         self.age=age
#         self.marks=marks
#         self.gpa = 0
#         return None#can return None/nothing but not anything else
        
#     def calc_GPA(self):
#         self.gpa = round(self.marks/25,3)
        
#     def get_GPA(self):
#         return self.gpa
    
# std1 : Student = Student("hammad",20,99)
# std1 . calc_GPA ()
# print (std1.get_GPA())
# ###################
# class Math:
#     def add(self,*args):
#         return sum(args)
#     def multiply(self,*args):
#         result=1
#         for i in args:
#             result*=i
#         return result/len(args)
#     def average(self,*args):
#         return sum(args)/len(args)
# ###############
# class Tokenizer:
#     def get_sentences(self,text):
#         return text.split(".")
#     def get_words(self,sentence):
#         return sentence.split(" ")
#     def get_characters(self,word):
#         return list(word)
# ##################
# ###############
# class Tokenizer:
#     def __init__(self, text ,name,age=0 *args):#cant return any value 
#         self.text = text # public variable
#         self._age = age # protected variable // only accessible by class functions
#         self.__name = name # private variable
        
#     def __setage(self,age):#private function
#         self._age=age
#     def _setage(self,age):#protected function
#         self._age=age
#     def printt(self):#public function
#         print(self.text)
        
#     def printn(self):
#         print(self.__name)
#     def getname(self):# getters
#         return self.__name
#     def setname(self,newname):# setters
#         self.__name = newname
        
#     def create_global_variable(self, text):
#             self.pi = 3.14
    
#     def get_sentences(self,text):
#         return text.split(".")
#     def get_words(self,sentences):
#         words=[]
#         for sentence in sentences:
#             words.extend(sentence.split(" "))
#         return words
#     def get_characters(self,words):
#         characters=[]
#         for word in words:
#             characters.extend(list(word))
#         return characters
#
# p1 = Tokenizer("cbdjnk","hamams")
# # p1.__name
# # p1.printn()
# print(p1.getname())
# p1.setname("namwaz")
# print(p1.getname())
#
# #################
# extend instead of append
# words=list(filter(lambda w:len(w)!=0,words))
# result = zip([1,2,3,4],['a','b','c','d'],['w','x','y','z'])
# #result = [(1,'a','w'),(2,'b','x'),(3,'c','y'),(4,'d','z')]
# import time
# start = time.time()
# class Animal:
#     def __init__(self, name, species, age):
#         self.name = name            # Public
#         self._species = species     # Protected (by convention, single underscore)
#         self.__age = age            # Private (double underscore)

#     # Public method
#     def introduce(self):
#         print(f"I am {self.name}, a {self._species}.")

#     # Protected method
#     def _protected_info(self):
#         print(f"(Protected) I belong to species {self._species}.")

#     # Private method
#     def __private_info(self):
#         print(f"(Private) My age is {self.__age} years.")

#     # Public method to access private method
#     def show_private_info(self):
#         self.__private_info()
# # end = time.time()-start
# print(end)
# a = Animal("Leo", "Lion", 5)

# a.introduce()             # Public
# a._protected_info()       # Technically possible but not recommended
# a.show_private_info()     # Correct way to access private info

# # Direct access:
# print(a.name)              # Public
# print(a._species)          # Possible, but protected
# # print(a.__age)           # Error! __age is private
# # print(a.__private_info()) # Error! __private_info is private
# print(time.time()-end-start)
#########################
# DESTRUCTOR
# BEFORE OBJECT CREATION DESTRUCTOR IS CALLED TO CLOSE FILE OR DELETING VARIABLE OR DISCONNECTING LINKS OR telling that link was disconnected 
# does clean up to protect from memory leakage
# def __init__(self):
#     pass
#     # / parameters
#     # x no return
# def __del__(self):
#     # x no parameters
#     # x no return
#     #cleanup code here
#     # called just before object deletion
#     print("")
    
# del t #to delete object
# class Animal:
#     def __init__(self, name, species, age):
#         self.name = name            # Public
#         self._species = species     # Protected (single underscore)
#         self.__age = age            # Private (double underscore)

#     # Public method
#     def introduce(self):
#         print(f"I am {self.name}, a {self._species}.")

#     # Protected method
#     def _protected_info(self):
#         print(f"(Protected) I belong to species {self._species}.")

#     # Private method
#     def __private_info(self):
#         print(f"(Private) My age is {self.__age} years.")

#     # Public accessor for private info
#     def show_private_info(self):
#         self.__private_info()


# # Dog subclass
# class Dog(Animal):
#     def __init__(self, name, age):
#         super().__init__(name, "Dog", age)

#     def bark(self):
#         # Public behavior
#         print(f"{self.name} says: Woof!")
#         # Can call protected method
#         self._protected_info()

#     def show_age_wrong(self):
#         # Trying to access private __age directly will fail
#         try:
#             print(self.__age)
#         except AttributeError:
#             print("Cannot access private attribute __age directly!")

#     def show_age_correct(self):
#         # Correctly access via the public accessor
#         self.show_private_info()


# # Cat subclass
# class Cat(Animal):
#     def __init__(self, name, age):
#         super().__init__(name, "Cat", age)
#
#     def meow(self):
#         print(f"{self.name} says: Meow!")
#         self._protected_info()
#
#     def peek_age_via_name_mangling(self):
#         # Private attributes are name-mangled: _Animal__age
#         print(f"(Name-mangled) My age is {self._Animal__age} years.")
#
#
# if __name__ == "__main__":
#     d = Dog("Buddy", 3)
#     d.introduce()            # public
#     d.bark()                 # public + protected
#     d.show_age_wrong()       # fails to access __age
#     d.show_age_correct()     # uses public method to show private info
#
#     print()
#
#     c = Cat("Whiskers", 2)
#     c.introduce()            # public
#     c.meow()                 # public + protected
#     c.peek_age_via_name_mangling()  # hacky access via name-mangling
# ######################
# class vehicle:
#     def __init__(self,model):
#         self._model=model
#         self.__chasis = "42637"#private and only available in this class by its functions
#     def get_chasis(self):#search is from bottom to top
#         return self.__chasis
# class car(vehicle):
#     def __init__(self,model):
#         super().__init__(model)# pass parameter to parent
#
#       
#     def model_name(self):
#         print(self._model)
###############
# class Vehicle:
#    
#     def __init__(self, make, model):
#         self.make = make
#         self.model = model
#         self.is_running = False
#
# class Car(Vehicle):
#    
#     def __init__(self, make, model, num_doors):
#         super().__init__(make, model)      # initialize Vehicle part
#         self.num_doors = num_doors         # new attribute for Car
#
#     def open_trunk(self):
#         print(f"Opening trunk of the {self.make} {self.model}.")
#
# # Example usage:
# class C(p1,p2,p3):#multiple inheritance
# name mangling
# searching from left to right
# MRO method resolution order
class A:
    def __init__(self):
        self.x = "set in A"

class B(A):
    def __init__(self):
        super().__init__()
        self.y = "set in B"

class C(A):
    def __init__(self):
        super().__init__()
        self.z = "set in C"

class D(B, C):
    def __init__(self):
        super().__init__()     # B → C → A
        print(self.x)

D()
# Output: set in A set in B set in C
# mro and how to access super class data
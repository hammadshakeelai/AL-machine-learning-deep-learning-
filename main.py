# for x in range(1,5):
#     if((x&1)==0):
#         print("even")
#     else:
#         print("odd")
# print(9>>2)
# print(9<<2)
# print(ord('A')) //returns binary of char\string
# print("hij".replace('h','p'))
# print("text".strip().upper().replace("T","x"))  #// chaining
# print("wxyz".find("x")) #//  find return starting index of substring
# print("wxyz"[1:1+len("xy")])
# print("wxyz"["wxyz".find("xy"):1+len("xy")])
# print("xy zw".split())
# print("1234567".split("4"))
# print("this car. i m strong".split("."))
# print("this car. i m strong".split(".")[0])
# import time
# start_time =time.time()
# ###################
# 4*4 vs 4>>2
# ######################
# end_time=time.time()
# print(end_time-start_time)
# n=input("yunimk")
# k=input("gh: ")
# print(k)
# mutable means changeable
# del my_list
# list.extend([5,8,8,8])
# type(u)
# .pop() #//remove last value and returns it
# .pop(3) // 3 index is popped
# .remove(4) // remove the first value 3 seen 
# text="cfvgbhn"
# print(text)
# list=[1,2,3]
# list[-1]=4##[1,2,4,3]
# POS tagging #// parts of speech
# mulltiple thiings are returns as tuple
# tuple is ordered
#  list.count("y")
# pos_tag=("word","noun")
# word,tag=pos_tag
# {'name':"hammad"}
# dict(nane="hammad")
# .keys() .values() .items() .get(key) .pop(key) .clear() 
# text='hloo'
# print(list(text))#//splits string individually
# ###############
# dict={
#       1:"yes",
#       2:"no",
#       3:"maybe",
#       4:"for sure"
#      }
# print(dict.keys())
# print(dict.values())
# print(dict.items())
# print(dict.get(4))
# print(dict.get(7))
# print(dict.pop(3))
# print(dict)
# del dict[2]
# print(dict)
# ####################33
# import time
# for i in range(1000,0,-1):
#     print("shayan is number ",i," kutta")
#     time.sleep(0.03)
# print("congratulations")
# #######################
# import time
# for h in range(365):
#     for i in range(24):
#         for j in range(60):
#             for k in range(60):
#                 print(f"{h=}:{i=}:{j=}:{k=}")
# #######################
# dict={"k":4,"3":444}
# for i,j in dict.items():
#     print(i,j)
# import time
# ##################
# if (3 and 1)==1:
#         print("t")
# else:
#         print("f")
# #----
# #########
# x=6
# "even" if x%2==0 else "odd"
# ########
# dict={
#     "d":3,
#     "f":5
# }
# for i,(key,value) in enumerate(dict.items()):
#     print(key,value,i)
# ##############
# r=5
# for i in range(r):
#     if i==3:
#         r=2
#     print("1")
#     #failure once a loop is set to run a set amount times , it will run that many time no matter if dozakh se farishta bhi a kar badalna chahe
# #################
# print([i for i in range(8)])
# print([i**3 for i in range(8)])
# print([i.lower() for i in ["TCY","FCK","GAF","AYY"]])
# print( [(i,j) for i in range(4) for j in range(4)])
# print([w for w in ['python','is','powerful'] if len(w)<=4])
# print(list("python"))
# ###########
# t=[]
# t[0]="hu"##error
# print(t)
# del list ##if intialized
# del num1,num2
# ###########
# r=print("helllo")
# print(r)
# None
# ##########
# i=iter(["p","j","o","l"])
# print(next(i))
# print(next(i))
# print(next(i))
# trained data epoch
# class myiterrator():
#     def __init__(self,path):
#         self.path=path
#         self.index=-1
#     def __next__(self):
#         self.index+=1
#         return self.path[self.index]

# i = myiterrator(["scbur","fuhdc","fvfv"])
# print(next(i))
# print(next(i))
# print(next(i))
# ##########
# tight coupling //whenglobal variables are used locally
# def add(num1,num2):
#   return num1+num2
# overloading?
# ##############
# def g(*args):
#     # args is a tuple (1,2,3,4,5)
#     return sum(args)
# print(g(1,2,3,4,5))
# #############
# def g(*kwargs):
#     # kwargs is a dict that store key words arguments
#     for i in kwargs:
#         print()
# print(g(j=9,k=8))
# positioal arm=guments always comes before key words arguments
# ##############
# def addition(x1,x2,*args,**kwargs):
#     print(x1,x2,args,kwargs)
# addition(4,7,9,9,name=6,age="sge")
# ################
# def getfive(*args):
#     for i in args:
#         if i == 5:
#             return 5
#     return 0
# print(getfive(1,2,3,4,5))
# #########
# fo="kk"
# print(f"{fo=} : jgigkhn {86}")
# ############
# sq = lambda x : x**3
# print(sq(7))
# ##########
# f=3
# print(lambda f: f**2)
# ###############
# o= lambda : (3,3)
# print(o())
# ############
# o= lambda : {3:3}
# print(o())
# ################
# def f(o,io):#send functions to a function as argument to callback
#     for i in o:
#         print(f"{i=}")
#     io()#callback
# f([1,2,3,4,5],lambda : print("suceesful"))
# ######
# if callable(callback):# to check if a function is callable
#     print("yes")
# ########
# def f():
#     print("hello")
# def g():
#     return f
# a=g()
# # a=g()()
# a()
# ############
# def parent(callback):
#     def child(mystr):
#         print(mystr)
#     return child,callback
# child,callback=parent(lambda :print("no"))
# child("hello")
# callback()#most callbacks are lambda
# ####################
# map(iter,callback)#DOES MAPPING
# use iter to send values one by one to callback for filtering then returns a value/list
# values=[1,2,3,4]
# values = map(lambda x: x**2, values)
# # for i in values:
# #     print(i)
# values = list(values)
# print(values)
# #becoz of memory wastage thus it will only give you values when you need them
# lazy loading
# #############
# filter(bool function,value)#only true values that goes through function are returned
# rest are filtered out
# passwords = ["tff", "xtdhtf", "hdt"]
# passwords = filter(lambda pw: len(pw) >= 4, passwords)
# print(list(passwords))
# ##########
# def outer_function():
#     def inner_function():
#         print("this is from inner function")
#     print("this is from outer function")
#     inner_function()
#     return inner_function
# inner_function_brought = outer_function()
# inner_function_brought()
# #################
# from time import time
# def measureTime(func):
#     def wrapper():
#         start_time = time()
#         func()#decorator
#         end_time = time()
#         print("time taken was ",round(end_time - start_time,6))
#     return wrapper
        
# @measureTime
# def dosomelooping():
#     for i in range(10):
#         print(i, end="\r")
#         # pass
# dosomelooping()
# @measureTime
# def filterPassword():
#     passwords=["fgd","egerthgrh","fdhdrt","hdfgbdfg"]
#     filtered_passwords=[]
#     for password in passwords:
#         if len(password)>=8:
#             filtered_passwords.append(password)
#     return filtered_passwords
# filterPassword()
# ###############
from time import time
def measureTime(func):
    def wrapper():
        start_time = time()
        result = func()
        end_time = time()
        print("time taken was ",round(end_time - start_time,6))
        return result
    return wrapper
        
@measureTime
def filterPassword():
    passwords=["fgd","egerthgrh","fdhdrt","hdfgbdfg"]
    filtered_passwords=[]
    for password in passwords:
        if len(password)>=6:
            filtered_passwords.append(password)
    return filtered_passwords

print(list(filterPassword()))
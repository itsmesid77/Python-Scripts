# # Creating Functions
# def my_func():
#     print("Hello World!")
# my_func()
# # Arguments 
# def my_func(fname):
#     print(fname + " " + "Malhotra")
# my_func("Amit")
# my_func("Nysa")
# my_func("Sysha")
# def my_func(fname,lname):
#     print(fname + " " + lname)
# my_func("Amit","Malhotra")
# # Wrong input
# def my_func(fname,lname):
#     print(fname + " " + lname)
# my_func("Amit")
# # Attribtry Arguments : when many inputs are given 
# def my_func(*kids):
#     print("The Youngest child is " + kids[2])
# my_func("Ram","Shyam","Kam")
# Keywords Arguments
# def my_func(child3,child2,child1):
#     print("The Youngest child is " + child3)
# my_func(child1 = "Ram",child2="Shyam",child3="Ham")
# # Qwarks Argument
# def my_func(**kid):
#     print("Her last name is " + kid["lname"])
# my_func(fname="Sysha",lname="Malhotra")
# # Default value argument
# def my_func(country="Norway"):
#     print("I am from " + country)
# my_func("India")
# my_func("Brazil")
# my_func()
# my_func("America")
# # List in argument
# def my_func(food):
#     for x in food:
#         print(x)
# fruits = ["Apple","Banana","Cherry"]
# my_func(fruits)
# def my_func(x):
#     return 5 * x
# print(my_func(3))
# print(my_func(5))
# print(my_func(9))
# name = "Amit"
# print(len(name))
# def add_2(a,b):
#     return a + b
# total = add_2(5,4)
# print(total)
# def add_2(a,b):
#     return a + b
# print(add_2(5,4))
# def add_2(num1,num2):
#     return num1 + num2
# a = int(input("Enter first number: "))
# b = int(input("Enter Second number: "))
# total = add_2(a,b)
# print(total)
# def add(num1,num2,num3):
#     print(num1 + num2 + num3)
# add(234,432,345)
# # Program to check whether the number is odd or not
# def my_func(num):
#     if num % 2 == 0:
#         print("It's an even number")
#     else:
#         print("It's a odd number.")
# a = int(input("Enter the number you want to check: "))
# my_func(a)
# Function defining
# def myfunc():
#     print("Siddharth")
#     print(23*23)
# myfunc()
# def myfunc(str1,str2):
#     print(str1)
#     print(str2)
# myfunc("Sid","dharth")
# myfunc("Amit","Malhotra")
# def print_something(name,age):
#     print("My name is " + name + " and my age is " + str(age))
# print_something("Siddharth",21)
# def print_something(name,age):
#     print("My name is " , name, " and my age is ",age)
# print_something("Siddharth",21)
# def print_something(name="Someone",age="Unknown"):
#     print("My name is ", name, "and my age is ",age)
# print_something("Siddharth")
# def print_something(name="Someone",age="Unknown"):
#     print("My name is ", name, "and my age is ",age)
# print_something(None,21)
# def print_something(name="Someone",age="Unknown"):
#     print("My name is", name, "and my age is",age)
# print_something(age=21,name="Siddharth")
# def print_something(*people):
#     for person in people:
#         print("This person is", person)
# print_something("Siddharth","Niranjan","Subhash","Harjas")
# def do_math(num1,num2):
#     return num1 + num2
# math1 = do_math(15,7)
# math2 = do_math(11,34)
# print("First sum is", math1, "and the second sum is",math2)
# def user_info(firstname,lastname=None,age=19):
#     print(f"Your firstname is {firstname}")
#     print(f"Your Lastname is {lastname}")
#     print(f"Your age is {age}")
# user_info("Siddharth")
# def func():
#     x = 7
#     return x
# def func2():
#     print(x)
# func2()
# def func():
#     x = 7
#     return x
# print(func())
# x = 5  #Global Variable
# def func():
#     x = 7 #local Variable
#     return x
# print(func())
# x = 5
# def func():
#     global x
#     x = 7
#     return(x)
# print(func())
# print(x)
# x = 5
# def func():
#     global x
#     x = 7
#     return x
# print(x)
# print(func())
# x = 5
# def func():
#     global x
#     x = 7
#     return x
# print(x)
# print(func())
# print(x)
# To check whether a number is even or not
# x = int(input("Enter the number you want to check : "))
# if x % 2 == 0:
#     print("It's an even number.")
# else:
# #     print("It's an odd number.")
# x = int(input("Enter the year you want to check: "))
# # if x % 4 == 0:
# #     print("It's a leap year.")
# # else:
# #     print("It's not a leap year.")
# result = "Leap Year" if x % 4 == 0 else 
def fun():a = []; print(type(a))
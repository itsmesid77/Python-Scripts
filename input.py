# name = input("Enter Your Name ")
# print("Hello" + " " + name)
# age = input("Enter Your age ")
# print("Your age is " + age)
# number_1 = input("Enter first Number: ")
# number_2 = input("Enter second Number: ")
# total  = number_1 + number_2
# print("Total is " + total)
# number_1 = int(input("Enter first Number: "))
# number_2 = int(input("Enter second Number: "))
# total  = number_1 + number_2
# print("Total is " + str(total))
# number_1 = float(44)
# number_2 = int(33)
# print(number_1 + number_2)
# name ,age = "Siddharth" , 19
# print("Hello " + name + " " + "Your Age is " + str(age) )
# name ,age = "Siddharth" , "19"
# print("Hello " + name + " " + "Your Age is " + age )
# name , age = input("Enter Your Name and age  : ") .split()
# print(name)
# print(age)
# name , age = input("Enter Your Name and age  : ") .split(",")
# print(name)
# print(age)
# #formatting for python2
# name = "Siddharth"
# age = 19
# print("Hello {}! Your age is {}." .format(name,age))
# # Formatting for python 3 - 3.10
# name = "Siddharth"
# age = 19
# print(f"Hello {name}! Your age is {age}.")
# Assignment
# x,y,z = int(input("Enter First Number : " )),int(input("Enter Second Number : ")),int(input("Enter Third number : "))
# c = int((x + y + z)/3)
# print(f"The Average of {x} , {y} , {z} is {c}")
x,y,z = input("Enter 3 numbers: ") .split(" ")
c = (int(x) + int(y) + int(z))/3
print(f"The Average of {x} , {y} , {z}  is {c} ")

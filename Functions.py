
# function

# def myfunc():
#     print("Hello I am Massmatic!!")
# myfunc()

# def myfunc(fname):
#     print(fname + " Malhotra")

# myfunc("Amit")
# myfunc("Nysa")

# def myfunc1(fname,lname):
#     print(fname + lname)
# myfunc1("Siddharth")


# def myfunc(*kids):
#     print("The youngest child is " + kids[0])
# myfunc("Akshay","Arpit","Siddharth")


# def myfunc(child3,child2,child1):
#     print("The Youngest child is " + child3)
# myfunc(child1="Sahil",child2="Jaspreet",child3="Akshay")

# def myfunc(**kid):
#     print("Her Name is " + kid["lname"])
# myfunc(fname = "Akshay" , lname = "Maruti")

# def myfunc(country = "India"):
#     print("I am from " + country)
# myfunc()
# myfunc("Sweden")

# def myfunc(food):
#     for x in food:
#         print(x)
# fruits = ["Apple","Banana","Cherry"]
# myfunc(fruits)

# def myfunc(x):
#     return 5*x
# print(myfunc(10))


# x = "Akshay"
# print(len(x))

# def mycalc(a,b):
#     return a + b
# total = mycalc(5,4)
# print(total)
# sum = mycalc(343432,3421)
# print(sum)

# def add_two(num1,num2):
#     return num1 + num2
# a = int(input("1st num = "))
# b = int(input("2nd num = "))
# print(add_two(a,b))

# def myfunc(num):
#     if num % 2 == 0:
#        return "Even"
#     return "odd"
    
# print(myfunc(1))


def myfunc(num):
    if num % 2 == 0:
       return True
    return False
    
print(myfunc(1))


def user_info(fname,lname,age):
    print(f"Your First name is {fname}")
    print(f"Your Last name is {lname}")
    print(f"Your age is {age}")
    


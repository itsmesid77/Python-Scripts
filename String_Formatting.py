# name = "Siddharth"
# age = 20
# print("Hello " + name + " your age is " + str(age))
name = "Siddharth"
age = 20
# print("Hello {} Your age is {}".format(name,age))
# print(f"Hello {name} your age is {age}")
# num1 = 10
# num2 = 20
# num3 =30
# print(f"num1 = {num1} num2 = {num2} num3 = {num3} and average = {(num1+num2+num3)//3}")
a,b,c = input("Enter the 3 numbers seperating with ',': ").split(",")
print(f"num1 = {a} num2 = {b} num3 = {c} and average = {(a+b+c)//3}")
# quantity = 3
# item_no = 567
# price = 49.95
# my_order = "I want {} pieces of item {} for {}$"
# print(my_order.format(quantity,item_no,price))
quantity = 3
item_no = 567
price = 49.95
my_order = "I want to pay {2} dollars for {0} pieces of item {1}."
print(my_order.format(quantity,item_no,price))
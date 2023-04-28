# # name = "Amit"
# # print(name+"Malhotra")
# # name+="Malhotra"
# # print(name)
# # age = 20
# # age = age+1
# # print(age)
# # age = 23
# # age += 2
# # print(age)
# # print(10==9)
# # print(10>9)
# # print(10<9)
# # a = 200
# # b = 33
# # if b < a:
# #     print("b is not greater than a")
# # else:
# #     print("b i greater than a")
# # print(bool("Hello"))
# # print(bool(20))
# # x = "Hello"
# # y = 15
# # print(bool(x))
# # print(bool(y))
# # print(10+5)
# # x=5
# # print(x)
# # x = 5
# # x+=3
# # print(x)
# # x-=3
# # print(x)
# # x*=3
# # print(x)
# # x/=3
# # print(x)
# # x%=3
# # print(x)
# # x //= 3
# # print(x)
# # x = 5
# # x **= 3
# # print(x)
# # x = 5
# # x &= 3
# # print(x)
# # x =5
# # x |= 3
# # print(x)
# # x = 5
# # x ^= 3
# # print(x)
# # x = 5
# # x <<= 3
# # print(x)
# # x = 5
# # x >>= 3
# # print(x)

# # # Comparision Operators
# # x= 5
# # y= 3
# # print(x==y)
# # print(x!=y)
# # print(x<y)
# # print(x>=y)
# # print(x<=y)

# # # Logical Operators
# # x = 5
# # print(x>3 and x<10)
# # print(x>3 or x < 4)
# # print(not(x<3 and x<10))

# # # Indentifier operator
# # x = ["apple","Banana"]
# # y = ["apple","Banana"]
# # z = x
# # print(x is z)
# # print(x is y)
# # print(x == y)
# # x = ["Banana","Apple"]
# # y = ["Banana","Apple"]
# # z = x
# # print(x is not y)
# # print(x is not z)
# # print(x != y)

# # Membership Operator
# x = ["Apple","Banana"]
# print("Banana" in x)
# print("Pinapple" not in x)


# this_list = ["apple","banana","cherry", "orange", "kiwi", "mango"]
# this_list[1:3] = ["melon", "pineapple", "lemon"]
# print(this_list)

# this_list = ["apple","banana","cherry"]
# this_list.insert(2, "watermelon") 
# print(this_list)

# this_list = ["apple","banana","cherry"]
# this_list.append("orange")
# print(this_list)

# """ this_list = ["apple","banana","cherry"]
# this_list.instet(1, "orange")
# print(this_list) """

# this_list = ["apple","banana","cherry"]
# tropical = ["mango", "pineapple", "papaya"]
# this_list.extend(tropical)
# print(this_list)

# this_list = ["apple","banana","cherry"]
# this_tuple = ("kiwi", "orange")
# this_list.extend(this_tuple)
# print(this_list)


# this_list = ["apple","banana","cherry"]
# this_list.remove("banana")
# print(this_list)

# this_list = ["apple","banana","cherry"]
# this_list.pop(1)
# print(this_list)

# this_list = ["apple","banana","cherry"]
# del this_list[0]
# print(this_list)

# this_list = ["apple","banana","cherry"]
# del this_list[2]
# print(this_list)

# this_list = ["apple","banana","cherry"]
# this_list.clear()
# print(this_list)

# this_list = ["apple","banana","cherry"]

# for x in this_list:
#     print(x)

# this_list = ["apple","banana","cherry"]
# for i in range(len(this_list)):
#     print(this_list[i])

# this_list = ["apple","banana","cherry"]

# """ i = 0 
# while i < len(this_list):
#     print(this_list[i])
#     i = i + 1
#  """

# fruits = ["apple","banana","chebrry", "kibwi", "mango"]
# new_list = []

# for x in fruits:
#     if "b" in x:
#         new_list.append(x)
#         print(new_list)

# fruits = ["apple","banana","cherry", "kiwi", "mango"]
# new_list = [x for x in fruits if "a" in x]
# print(new_list)

# #condition

# fruits = ["apple","banana","cherry","kiwi", "mangooo"]
# new_list = [x for x in fruits if x=="apple"]
# print(new_list)


# fruits = ["apple","banana","cherry", "kiwi", "mango"]
# new_list = [x for x in fruits]
# print(new_list)

# new_list = [x for x in range(10)]
# print(new_list)

# new_list = [x for x in range(10) if x>5]
# print(new_list)

# fruits = ["Apple","Bnanana","Cherry","Kiwi","Mango"]
# new_list = [ x for x in fruits if x != "Apple"]
# new_list = [ x for x in fruits]
# print(new_list)

# new_list = [x for x in range(10)]
# print(new_list)

# fruits = ["Apple","Bnanana","Cherry","Kiwi","Mango"]
# new_list = [x.upper() for x in fruits]

# fruits = ["Apple","Bnanana","Cherry","Kiwi","Mango"]
# new_list = ['Hello' for x in fruits]
# print(new_list)

# fruits = ["Apple","Bnanana","Cherry","Kiwi","Mango"]
# new_list = [x if x != "Banana" else "Orange" for x in fruits]

# the_list = ["Orange","Apple","Cherry","Kiwi","Banana"]
# the_list.sort()
# print(the_list)

# thelist = [100,10,65,32,25,54]
# thelist.sort()
# print(thelist)

# thelist = [100,10,65,32,25,54]
# thelist.sort(reverse=True)
# print(thelist)

# the_list = ["Orange","Apple","Cherry","Kiwi","Banana"]
# the_list.sort(reverse=True)
# print(the_list)

# def myfunc(n):
#     return abs(n-50)
# this_list = [100,50,65,82,23]
# this_list.sort(key=myfunc)
# print(this_list)

# this_list = ["Orange","banana","Kiwi","cherry"]
# this_list.sort()
# print(this_list)

# this_list = ["Orange","banana","Kiwi","cherry"]
# this_list.sort(key=str.lower)
# print(this_list)

# this_list = ["Orange","banana","Kiwi","cherry"]
# this_list.reverse()
# print(this_list)

# this_list = ["Apple","Banana","Cherry"]
# mylist = this_list.copy()
# print(mylist)

# this_list = ["Apple","Banana","Cherry"]
# mylist = list(this_list)
# print(mylist)

# list1 = ["a","b","c","d"]
# list2 = [1,2,3,4]
# list3 = list1 + list2
# print(list3)

# list1 = ["a","b","c","d"]
# list2 = [1,2,3,4]
# for x in list2:
#     list1.append(x)
# print(list1)

# # list1 = ["a","b","c","d"]
# # list2 = [1,2,3,4]
# # for x in list2:
# #     list1.extend(x)
# # print(list1)

# this_tuple = ("Apple","Banana","Cherry")
# print(this_tuple)

# this_tuple = ("Apple","Banana","Cherry","Apple")
# print(this_tuple)
# print(len(this_tuple))

# this_tuple = ("Apple")
# print(type(this_tuple))

# tuple1 = ("Apple","Banana")
# tuple2 = (1,2,3,4,5)
# tuple3 = (True,False,True)
# tuple4 = ("Apple",1,True,3,"Banana")
# print(tuple1)
# print(tuple2)
# print(tuple3)
# print(tuple4)

# this_tuple = tuple((1,2,"Apple"))
# print(this_tuple)

# this_tuple = ("Apple","Banana","Cherry")
# print(this_tuple[1])
# print(this_tuple[-1])


# this_tuple = ("Apple","Banana","Cherry","Mango","Kiwi","Peech")
# print(this_tuple[2:5])
# x = list(this_tuple)
# x[1] = "Lichi"
# this_tuple = tuple(x)
# print(this_tuple)

# # and Operator
# a = 200
# b = 33
# c = 500
# if a > b and c > a:
#     print("Both the conditions are true")

# # or operator
# a = 200
# b = 33
# c = 500
# if a > b or a>c:
#     print("Atleast one the condition is true.")

# name = 'abc'
# age = 19
# if name == 'abc' and age == 25:
#     print("Condition True")
# else:
#     print("Condition False")


# name = 'abc'
# age = 29
# if name == 'abc' or age == 19:
#     print("Condition True")
# else:
#     print("Condition False")

# name,age = input("Enter your name and age: ").split()
# age = int(age)
# if (name[0] == "a" or name[0] == "A") and age > 10:
#     print("You can watch Singham")
# else:
#     print("Sorry! You cannot watch Singham")

# age = input("Enter your age: ")
# age = int(age)
# if age == 0 or age < 0:
#     print("You can't watch.")
# elif 0 < age <= 3:
# elif 3 < age <= 10:
#     print("Ticket price = 150/-")
# elif 10 < age <= 60:
#     print("Ticket Price = 250/-")
# else:
#     print("Ticket Price is 200/-")

# try:
#     print(x)
# except:
#     print("Hello")
# from unicodedata import name
# try:
#     print(x)
# except NameError:
#     print("Variable not defined")
# except:
#     print("Something went wrong")
# try:
#     print("Hello")
# except:
#     print("Something went wrong")
# else:
#     print("Nothing went wronng")
# try:
#     print("Hello")
# except:
#     print("Something went wrong")
# finally:
#     print("Nothing went wronng")
# try:
#     f = open("demo.txt")
#     try:
#         f.write("My name is Siddharth Rao")
#     except:
#         print("Something went wrong in writting the file")
#     finally:
#         f.close()
# except:
#     print("Something went wrong in opening the file")
# x = -1
# if x < 0:
#     raise Exception("Sorry no number less than 0")
# x = "Hello"
# if not type(x) is int:
#     raise TypeError("Plz input integer value only")
username = input("Enter Username: ")
print("Username is " + username)
# 2.7 method
# username = raw_input("Enter Username: ")
# print("Username is " + username)
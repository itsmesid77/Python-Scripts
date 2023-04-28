# # AND Operator 
# a = 200
# b = 33
# c = 500
# if a < b and c > a:
#     print("Both the conditions are satisfied!")
# # OR Operator
# a = 200
# b = 33
# c = 500
# if a < b or c > a:
#     print("Atleast 1 condition is satisfied!")
# # String and integer
# name = "Vikas"
# age = 40
# if name == "Vikas" and age == 19:
#     print("Both the conditions are satisfied!!")
# else:
#     print("Both the conditions are not satisfied!!!")
# name = "Vikas"
# age = 40
# if name == "Vikas" or age == 19:
#     print("One of the conditions is satisfied!!")
# else:
#     print("Both the conditions are not satisfied!!!")
user_name = input("Enter your name: ")
user_age = input("Enter your age: ")
user_age = int(user_age)
if user_age <= 10 and (user_name[0] == "a" or user_name[0] == "A"):
    print("You can watch Singham Movie")
else:
    print("You cannot watch Singham Movie")

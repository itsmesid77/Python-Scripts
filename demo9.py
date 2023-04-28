x = ["apple", "banana"]
print("banana" in x)

x = ["apple", "banana"]
print("pinapple" not in x)

#python list 
#list, tuple, set, dict 
#list #list is changeable
this_list = ["apple","banana", "cherry"]
print(this_list)

#ordered
this_list = ["apple", "banana","cherry", "apple", "cherry"]
print(this_list)
print(len(this_list))

list1 = ["apple","banana","cherry"]
list2 = [1,5,7,9,3]
list3 = [True, False, True, False]
print(list1)
print(list2)
print(list3)

list1 = ["abc", 34, True, 14, "male"]
print(list1)

#type 
my_list = ["apple", "banana", "cherry"]
print(type(my_list))

#constructor 
this_list = list(("apple", "banana","cherry"))
print(this_list)

this_list = ["apple","banana","cherry"]
print(this_list[1])
print(this_list[-1])
 
this_list = ["apple","banana","cherry", "orange", "kiwi", "pineapple", "mango"]
print(this_list[2:5])
print(this_list[:4])
print(this_list[2:])
print(this_list[-4:-1])

this_list = ["apple","banana","cherry"]
if "apple" in this_list:
    print("Yes Apple is in the fruit list")

this_list = ["apple","banana","cherry"]
this_list[1] = "melon"
print(this_list)

this_list = ["apple","banana","cherry", "orange", "kiwi", "mango"]
this_list[1:3] = ["melon", "pineapple", "lemon"]
print(this_list)

this_list = ["apple","banana","cherry"]
this_list.insert(2, "watermelon") 
print(this_list)

this_list = ["apple","banana","cherry"]
this_list.append("orange")
print(this_list)

""" this_list = ["apple","banana","cherry"]
this_list.instet(1, "orange")
print(this_list) """

this_list = ["apple","banana","cherry"]
tropical = ["mango", "pineapple", "papaya"]
this_list.extend(tropical)
print(this_list)

this_list = ["apple","banana","cherry"]
this_tuple = ("kiwi", "orange")
this_list.extend(this_tuple)
print(this_list)


this_list = ["apple","banana","cherry"]
this_list.remove("banana")
print(this_list)

this_list = ["apple","banana","cherry"]
this_list.pop(1)
print(this_list)

this_list = ["apple","banana","cherry"]
del this_list[0]
print(this_list)

this_list = ["apple","banana","cherry"]
del this_list[2]
print(this_list)

this_list = ["apple","banana","cherry"]
this_list.clear()
print(this_list)

this_list = ["apple","banana","cherry"]

for x in this_list:
    print(x)

this_list = ["apple","banana","cherry"]
for i in range(len(this_list)):
    print(this_list[i])

this_list = ["apple","banana","cherry"]

""" i = 0 
while i < len(this_list):
    print(this_list[i])
    i = i + 1
 """

fruits = ["apple","banana","chebrry", "kibwi", "mango"]
new_list = []

for x in fruits:
    if "b" in x:
        new_list.append(x)
        print(new_list)

fruits = ["apple","banana","cherry", "kiwi", "mango"]
new_list = [x for x in fruits if "a" in x]
print(new_list)

#condition

fruits = ["apple","banana","cherry","kiwi", "mangooo"]
new_list = [x for x in fruits if x=="apple"]
print(new_list)


fruits = ["apple","banana","cherry", "kiwi", "mango"]
new_list = [x for x in fruits]
print(new_list)

new_list = [x for x in range(10)]
print(new_list)

new_list = [x for x in range(10) if x>5]
print(new_list)


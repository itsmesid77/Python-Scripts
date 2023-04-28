#update tuples 
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)

this_tuple = ("apple", "banana", "cherry")
y = list(this_tuple)
y.append("orange")
this_tuple = tuple(y)
print(this_tuple)

this_tuple = ("apple","banana","cherry")
y = ("orange",)
this_tuple += y
print(this_tuple)


this_tuple = ("apple", "banana", "cherry")
y = list(this_tuple)
y.remove("apple")
this_tuple = tuple(y)
print(this_tuple)

this_tuple = ("apple", "banana", "cherry")
#del this_tuple 
print(this_tuple)

this_tuple = ("apple", "banana", "cherry")
(green, yellow, red) = this_tuple
print(green)
print(yellow)
print(red)


fruits = ("apple", "banana", "cherry", "raspberry", "Kiwi")
(green, yellow, *red) = fruits 
print(green)
print(yellow)
print(red)


fruits = ("apple", "banana", "cherry", "raspberry","cherry","cherry", "Kiwi")
(green, *tropic, red) = fruits 
print(green)
print(tropic)
print(red)

fruits = ("apple", "banana", "cherry", "raspberry", "//")
for x in fruits:
    print(x)

fruits = ("apple", "banana", "cherry", "raspberry")
for i in range(len(fruits)):
    print(fruits[i])

fruits = ("apple", "banana", "cherry", "raspberry", "//")
i = 0 
while i<len(fruits):
    print(fruits[i])
    i += 1

tuple1 = ("a", "b", "c")
tuple2 = (1,2,3)
tuple3 = tuple1 + tuple2 
print(tuple3)

fruits = ("apple", "banana", "cherry", "raspberry", "//")
my_tuple = fruits * 2 
print(my_tuple)

this_set = {"apple", "banana", "cherry"}
print(this_set)

this_set = {"apple", "banana", "cherry", "apple"}
print(len(this_set))

set1 = {"apple", "banana", "cherry"}
set2 = {1,7,8,3,9}
set3 = {True, False, True}
print(set1)
print(set2)
print(set3)

set1 = {"a", "b", "c", 30, True, 40, "mail"}
print(type(set1))

this_set = set(("apple", "banana", "cherry"))
print(this_set)


this_set = {"apple", "banana", "cherry"}

if "banana" in this_set:
    print(True)

this_set = {"apple", "banana", "cherry"}
this_set.add("kiwi")
print(this_set)




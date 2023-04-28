
#dictionary in python 
#dictionary is a group of items, ordered, written in {} and can be changable

this_dict = {"brand": "ford", "model":"mustang", "year":2022}
print(this_dict)

this_dict = {"brand": "ford", "model":"mustang", "year":2022}
print(this_dict["brand"])


this_dict = {"brand": "ford", "model":"mustang", "year":2022, "year":1964}
print(len(this_dict))
print(type(this_dict))

#get method

this_dict = {"brand": "ford", "model":"mustang", "year":2022}
x = this_dict.get("model")
print(x)


#keys method 

this_dict = {"brand": "ford", "model":"mustang", "year":2022}
x = this_dict.keys()
print(x)

this_dict = {"brand": "ford", "model":"mustang", "year":2022}
x = this_dict.values()
print(x)
this_dict['color'] = "white"
print(x)

this_dict = {"brand": "ford", "model":"mustang", "year":2022}
x = this_dict.values()
print(x)
this_dict["year"] = 2020
print(x)
this_dict["color"] = "red"
print(x)

this_dict = {"brand": "ford", "model":"mustang", "year":2022}
x = this_dict.items()
print(x)
this_dict["year"] = 2020
print(x)
this_dict["color"] = "red"
print(x) 

this_dict = {"brand": "ford", "model":"mustang", "year":2022}
if "model" in this_dict:
    print("yes, model is present")


this_dict = {"brand": "ford", "model":"mustang", "year":2022}
this_dict.pop("model")
print(this_dict)

this_dict = {"brand": "ford", "model":"mustang", "year":2022}
this_dict.popitem()
print(this_dict)
 
del this_dict["model"]
print(this_dict)


""" this_dict = {"brand": "ford", "model":"mustang", "year":2022}
del this_dict
print(this_dict) """

this_dict = {"brand": "ford", "model":"mustang", "year":2022}
this_dict.clear()
print(this_dict)

this_dict = {"brand": "ford", "model":"mustang", "year":2022}

for x in this_dict.items():
    print(x)

this_dict = {"brand": "ford", "model":"mustang", "year":2022}
x = this_dict.copy()
#this_dict.copy(x)
print(x)





# x  = {"Apple","Banana","Cherry"}
# y = {"Google","Microsoft","Apple"}
# z = x.symmetric_difference(y)
# print(z)


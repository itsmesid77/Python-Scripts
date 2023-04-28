# formatting string
#left align
from pprint import pprint


txt = "We have {:<8} chickens"
print(txt.format(49))
#right align
txt = "We have {:>8} chickens"
print(txt.format(49))
#center align
txt = "We have {:^8} chikens"
print(txt.format(49))
#spaces between -+
txt = "The temprature is {:=8}degree celsius"
print(txt.format(-5))
#column +
txt = "The temprature is between {:+} and {:+} degree celsius"
print(txt.format(-3,7))
txt = "The temprature is between {:-} and {:-} degree celsius"
print(txt.format(-3,7))
txt = "The temprature is between {:} and {:} degree celsius"
print(txt.format(-3,7))
txt = "the universe is {:,} years old"
print(txt.format(13800000000))
txt = "the universe is {:_} years old"
print(txt.format(13800000000))
#decimal to binary conversion
txt = "The binary version of {0} is {0:b}"
print(txt.format(5))
#octal to decimal conversion
txt = "We have {:d} chickens"
print(txt.format(0o101))
#binary to decimal conversion
txt = "We have {:d} chickens"
print(txt.format(0b101))
#Scientific number format in lower case
txt = "We have {:e} chickens"
print(txt.format(5))
#Scientific number format upper case
txt = "We have {:E} chickens"
print(txt.format(5))
txt = "The price is {:.2f} dollars"
print(txt.format(45))
txt = "The price is {:.5f} dollars"
print(txt.format(45))
txt = "The price is {:f} dollars"
print(txt.format(45))
x = float('inf')
txt = "The price is {:F} dollars"
print(txt.format(x))
txt = "The price is {:f} dollars"
print(txt.format(x))
#decimal to octal conversion
txt = "The octal version of {0} is {0:o}"
print(txt.format(10))
#decimal to hexa conversion
txt = "The hexadecimal version of {0} is {0:x}"
print(txt.format(155))
txt = "The hexadecimal version of {0} is {0:X}"
print(txt.format(255))
txt = "you scored {:%}"
print(txt.format(0.25))
txt = "you scored {:.0%}"
print(txt.format(0.25))
txt = "Hello, welcome to my world"
x = txt.index("welcome")
print(x)
txt = "Hello, welcome to my world"
x = txt.index("e")
print(x)
txt = "Hello, welcome to my world"
x = txt.index("e",5,10)
print(x)
#alpha numeric
txt = "Company12"
x = txt.isalnum()
print(x)
txt = "Company 12"
x = txt.isalnum()
print(x)
txt = "companyx"
x = txt.isalpha()
print(x)
txt = "company10"
x = txt.isalpha()
print(x)
txt = "\u0033"
x = txt.isdecimal()
print(x)
a = "\u0030" #unicode for 0
b = "\u0047"
print(a.isdecimal())
print(b.isdecimal())
txt = "50800"
x = txt.isdigit()
print(x)
a = "\u0047" #unicode for G
print(a.isdigit())
#iside
txt = "Demo"
x = txt.isidentifier()
print(x)
a = "MyFolder"
b = "Demo002"
c = "2bring"
d = "mydemo"
print(a.isidentifier())
print(b.isidentifier())
print(c.isidentifier())
print(d.isidentifier())
#islower
txt = "hello world"
x = txt.islower()
print(x)
a = "Hello World"
b = "hello 123"
c = "mynameisnirmala"
print(a.islower())
print(b.islower())
print(c.islower())
#isnumeric
txt = "564453"
x = txt.isnumeric()
print(x)
a = "\u0030"
b = "\u00b2"
c = "10km2"
d = "-1"
e = "1.5"
print(a.isnumeric())
print(b.isnumeric())
print(c.isnumeric())
print(d.isnumeric())
print(e.isnumeric())
#isprintable method
txt = "Hello Are You # 1 ?"
x = txt.isprintable()
print(x)
txt = "Hello\nAre You # 1 ?"
x = txt.isprintable()
print(x)
#isspace method
txt = " "
x = txt.isspace()
print(x)
txt = " s "
x = txt.isspace()
print(x)
#istitle method
txt = "Hello, And Welcome To My World"
x = txt.istitle()
print(x)
a = "HELLO, AND WELCOME TO MY WORLD"
b = "Hello"
c = "22 Names"
d = "This Is %!?"
print(a.istitle())
print(b.istitle())
print(c.istitle())
print(d.istitle())
#isupper method
txt = "THIS IS AMIT"
x = txt.isupper()
print(x)
a = "Hello World"
b = "hello 123"
c = "MY NAME IS NIRANJAN"
print(a.isupper())
print(b.isupper())
print(c.isupper())
#join method
mytuple = ("john", "raj", "harjas")
x = "#".join(mytuple)
print(x)
myabc = {"name": "siddharth", "country": "india"}
myseprator = "TEXT"
x = myseprator.join(myabc)
print(x)
#Ljust method
txt = "banana"
x = txt.ljust(20)
print(x, "my favorite fruit.")
text = "banana"
x = text.ljust(20, "*")
print(x)
#lower method
txt = "Hello my FRIENDS"
x = txt.lower()
print(x)
txt = "    banana    "
x = txt.lstrip()
print("of all fruits", x, "is my favorite")
txt = ",,,,,,ssaawww.....banana"
x = txt.lstrip(",.asw")
print(x)
#mapping table
txt = "hello siddharth"
mytable = txt.maketrans("s", "p")
print(txt.translate(mytable))
txt = "Hi Sam!"
x = "mSa"
y = "eJo"
mytable = txt.maketrans(x,y)
print(txt.translate(mytable))
txt = "Good night Sam!"
x = "mSa"
y = "eJo"
z = "odnght"
mytable = txt.maketrans(x,y,z)
print(txt.translate(mytable))
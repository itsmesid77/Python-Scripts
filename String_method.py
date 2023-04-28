# txt = "hello, welcome to my world!"
# x = txt.capitalize()
# print(x)
# txt = "PYTHON IS FUN"
# x = txt.capitalize()
# print(x)
# txt = "Hello, Welcome To My World!"
# x = txt.casefold()
# print(x)
# txt = "Banana"
# x = txt.center(20)
# print(x)
# txt = "Banana"
# x = txt.center(20,'*')
# print(x)
# txt = "I love apples, apples are my  favourite fruit."
# x = txt.count("apple")
# print(x)
# txt = "I love apples, apples are my favourite fruit."
# x = txt.count("apple",10,24)
# print(x)
# txt = "My name is Ståle"
# x = txt.encode()
# print(x)
# txt = "My name is Ståle"
# print(txt.encode(encoding="ascii",errors="backslashreplace"))
# print(txt.encode(encoding="ascii",errors="ignore"))
# print(txt.encode(encoding="ascii",errors="xmlcharrefreplace"))
# print(txt.encode(encoding="ascii",errors="namereplace"))
# print(txt.encode(encoding="ascii",errors="replace"))
# txt = "Hello, welcome to my world."
# x = txt.endswith('.')
# print(x)
# txt = "Hello, welcome to my world."
# x = txt.endswith('my world.')
# print(x)
# x = txt.endswith('my world.',5,11)
# print(x)
# txt = "H\te\tl\tl\to"
# x = txt.expandtabs(2)
# print(x)
# print(txt.expandtabs())
# print(txt.expandtabs(2))
# print(txt.expandtabs(4))
# print(txt.expandtabs(10))
# txt = "Hello, welcome to my world!"
# x = txt.find("welcome")
# print(x)
# txt = "Hello, welcome to my world!"
# x = txt.find("e")
# print(x)
# txt = "Hello, welcome to my world!"
# x = txt.find("e",5,10)
# print(x)
# txt = "Hello, welcome to my world!"
# x = txt.find("e",5,10)
# print(x)
# txt = "Hello, welcome to my world!"
# x = txt.find("q",5,10)
# print(x)
# txt = "for only price {price: .2f} dollars."
# print(txt.format(price=49))
# txt1 = "My name is {fname}, I am {age}".format(fname="Addy",age=21)
# txt2 = "My name is {0}, I am {1}".format("Siddharth",36)
# txt3 = "My name is  {}, I am {}".format("Akshay",12)
# print(txt1)
# print(txt2)
# print(txt3)

#fomatting types
 # :< left align
 # :> right align
 # :^ center align
 # := place sign to left most position
 # :+ denotes the the positive or negative 
 # :- denotes negative number
 # : give space
 # :, thousand spertor
 # :_ use as a thousand operator

# txt = "We have {:<} chickens"
# print(txt.format(49))
# txt =  "We have {:<8} chickens."
# print(txt.format(49))
# txt =  "We have {:<} chickens."
# print(txt.format(49))
# txt = "The temperature is between {:} and {:} celcius"
# print(txt.format(3,7))
# txt = "The universe is {:,} years old."
# print(txt.format(100000000000))
# txt = "The universe is {:_} years old."
# print(txt.format(100000000000))
# txt = "The binary version of {0} is {0:b}"
# print(txt.format(5))
# txt = "We have {0:d} pens"
# print(txt.format(0b101))
# txt = "We have {0:e} pens"
# print(txt.format(0b101))
# txt = "We have {0:E} pens"
# print(txt.format(0b101))
# txt = "The price is {:.2f}$"
# print(txt.format(45))
# txt = "The price is {:f}$"
# print(txt.format(45))
# txt = "The price is {:F}$"
# print(txt.format(45))
# x = float('inf')
# txt = ("Price is {:F}$")
# print(txt.format(x))
# x = float('inf')
# txt = ("Price is {:f}$")
# print(txt.format(x))
# txt = "The octal version of {0} is {0:o}"
# print(txt.format(10))
# txt = "The hexa version of {0} is {0:x}"
# print(txt.format(255))
# txt = "The octal version of {0} is {0:X}"
# print(txt.format(255))
# txt = "You Scored {:.0%}"
# print(txt.format(0.25))
# String Index
# txt = "Hello, welcome to my world!"
# y = txt.index("welcome")
# print(y)
# txt = "Hello, welcome to my world!"
# y = txt.index("e")
# print(y)
# txt = "Company12"
# y = txt.isalnum()
# print(y)
# txt = "Company"
# y = txt.isalpha()
# print(y)
# txt = "\u0033"
# y = txt.isdecimal()
# print(y)
# txt = "\u0047"
# y = txt.isdecimal()
# print(y)
# txt = "5083"
# y = txt.isdigit()
# print(y)
# txt = "\u0030"
# txt1 = "\u00b2"
# print(txt.isdigit())
# print(txt1.isdigit())
# txt = "demo"
# print(txt.isidentifier()) 
# txt = "my demo"
# print(txt.isidentifier()) 
# txt = "2demo"
# print(txt.isidentifier()) 
# txt = "hello world"
# print(txt.islower())
# txt = "my name is Aditya"
# print(txt.islower())
# txt = "123"
# print(txt.isnumeric())
# txt = "Hello, Welcome to my world!"
# print(txt.isprintable())
# txt = " "
# print(txt.isspace())
# txt = " s "
# print(txt.isspace())
# txt = "Hello Welcome To My World!"
# print(txt.istitle())
# a = "HELLO AND WELCOME TO MY WORLD!"
# b = "Hello How Are You?"
# c = "Names"
# d = "This Is %'!?"
# print(a.istitle())
# print(b.istitle())
# print(c.istitle())
# print(d.istitle())
# txt = "THIS IS NOW"
# print(txt.isupper())
# mytuple = ("Addy","Siddharth","Akshay")
# x = "#".join(mytuple)
# print(x)
# my_dic = {"Name":"Addy","Country":"India"}
# mysep = "test"
# x = mysep.join(my_dic)
# print(x)
# txt = "banana"
# x = txt.ljust(20)
# print(x," is my favourite fruit")
# txt = "banana"
# x = txt.ljust(20,"o")
# print(x," is my favourite fruit")
# txt = "Hello my FRIENDS"
# print(txt.lower())
# txt = "  banana "
# print("all fruits " + txt.lstrip() +" is my favourite")
# txt = ",,,,,ssaawdlllsstttt......banana"
# x = txt.lstrip(",sawdlt.")
# print(x)
# txt = "Hello Sam"
# x = txt.maketrans("S","P")
# print(txt.translate(x))
# txt = "Hello Sam"
# x = "aSm"
# y = "oJe"
# z = txt.maketrans(x,y)
# print(txt.translate(z))
# txt = "Goodnight Sam"
# x = "mSa"
# y = "eJo"
# z = "odnght"
# mytable = txt.maketrans(x,y,z)
# print(txt.translate(mytable))
txt = "I could eat banana all day"
x = txt.partition("banana")
print(x)
# txt = "I could eat banana all day"
# x = txt.partition("apple")
# print(x)
# txt = "apple,banana,cherry"
# x = txt.rsplit(",")
# print(x)
# txt = "  banana  "
# x = txt.rstrip()
# print("of all fruits",x,"is my favourite")
# txt = "banana,,,,,ssqqwww..."
# print(txt.rstrip(",sqw."))
# txt = "Welcome to the jungle"
# x = txt.split()
# print(x)
# txt = "Hello,my name is addy, i am 20yrs old."
# print(txt.split(","))
# txt = "apple#banana#cherry"
# print(txt.split("#"))
# txt = "apple#banana#cherry#orange"
# print(txt.split("#",1))
# txt = "Thank You for the music\nWelcome to the jungle"
# print(txt.splitlines())
# txt = "Thank You for the music\nWelcome to the jungle"
# print(txt.splitlines(True))
# txt = "50"
# x = txt.zfill(10)
# print(x)
# a = "hello"
# b = "Welcome to the Jungle"
# c = "10.000"
# print(a.zfill(10))
# print(b.zfill(10))
# print(c.zfill(10))
# name = "            Sid             "
# dots = "............................"
# print(name.lstrip()+dots)
# print(name.rstrip()+dots)
# print(name.strip()+dots)
# name = "    AM   IT  "
# dots = "...................."
# print(name.replace(" ","")+dots)
# Replace and find method
# string = "She is beautiful and she is good dancer.She is cute."
# print(string.replace(" ","_"))
# print(string.replace("is","was"))
# print(string.replace("is","was",2))
# print(string.find("is",5))
# string = "She is beautiful and she is good dancer.She is cute."
# is_pos1 = string.find("is")
# is_pos2 = string.find("is",is_pos1+1)
# print(is_pos2)
# name="Siddharth"
# print(name.center(30,"*"))
# name = input("Enter your name: ")
# print(name.center(len(name)+10,"*"))
# string = "Amit"
# print(string.replace("t","T"))
# string = "string"
# string.replace("t","T")
# print(string)
# string_new = string.replace("t","T")

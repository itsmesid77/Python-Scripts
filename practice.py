# txt = "hello, welcome Back!"
# print(txt.capitalize())
# print(txt.casefold())
# txt = "Banana"
# print(txt.center(50,"-"))
# txt = "I had 9 apples and now I have 5 apples, someone took my 5 apples."
# print(txt.count("apples"))
# txt = "My name is Ståle"
# print(txt.encode())
# print(txt.encode(encoding="ascii", errors="backslashreplace"))
# print(txt.encode(encoding="ascii", errors="ignore"))
# print(txt.encode(encoding="ascii", errors="namereplace"))
# print(txt.encode(encoding="ascii", errors="replace"))
# print(txt.encode(encoding="ascii", errors="xmlcharrefreplace"))
# txt = "Hello World!"
# print(txt.endswith("!"))
# print(txt.endswith("World!",7))
# txt = "H\tE\tL\tL\tO"
# print(txt.expandtabs(10))
# txt = "Hello Welcome back here!"
# print(txt.find("e", 21))
# print(txt.index("a"))
# txt  = "Hello,  The price of item no. {} is {price:.2f}"
# print(txt.format("123", price = 49))
# txt = "Hello, My name is {fname} and my age is {age}"
# print(txt.format(fname="Siddharth", age = 19))
# txt = "Hello, My name is {0} and my age is {1}"
# print(txt.format("Siddharth",19))
# txt = "Hello, My name is {} and my age is {}"
# print(txt.format("Siddharth",19))
# #lower
# x = "My Name is Siddharth"
# print(x.lower())
# #upper
# x = "my name is siddharth"
# print(x.upper())
# #title
# x = "my nAMe iS siDDhaRtH"
# print(x.title())
# #capitalize 
# x = "my Name is SiddhArth"
# print(x.capitalize())
#Join Method 
x = ("Siddharth", "Ram", "Sam")
print(" # ".join(x))
x = {"Name": "Siddharth", "age": 19}
print(" / ".join(x))
x = ("Siddharth", "Ramlal", "Sam")
myseperator = " / "
print(myseperator.join(x))
# Ljust
x = "Apple"
print(x.ljust(20,), "My Favourite.")
print(x.rjust(20,), "My Favourite.")
# Lstrip
x = "12345678Banana12345678"
print("My Favourite" , x.lstrip() , "I like it.")
txt = x.lstrip("12345678")
print(txt)
txt = ",,,,,,ssaawww.....banana"
# spacing formatting string
txt = "I'm {:>10} Yrs Old."
print(txt.format(19))
txt = "I'm {:<10} Yrs Old."
print(txt.format(19))
txt = "I'm {:^10} Yrs Old."
print(txt.format(19))
# Spacing b/w operators
txt = "1 - 5 = {:=5}"
print(txt.format(-4))
txt = "1 + 5 = {:+}"
print(txt.format(6))
txt =  "1 - 5 = {:-} {:-}"
print(txt.format(-4,+6))
txt = "1 - 5 = {:} {:}"
print(txt.format(-4,+3))
txt = "India's Population is {:,}."
print(txt.format(1300000000))

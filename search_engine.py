from googlesearch import search
print("Welcome to google search by massmatic")
query = input("what you want to search on google by Massmatic: ")
for i in search(query, start=0, stop=6):
    print(i)
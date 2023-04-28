from google_search import search
print("Welcome To google search by Massmatic")
query = input("What do you want to search on google by Massmatic: ")
for i in search(query, start =0, stop =6):
    print(i)
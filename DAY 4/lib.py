class book:
    def __init__(self, title, author, year,price,id):
        self.title = title
        self.author = author
        self.year = year
        self.price = price
        self.id = id

lst = []

n = int(input("Enter the number of books: "))
for i in range(n):
    title = input("Enter the title of the book: ")
    author = input("Enter the author of the book: ")
    year = int(input("Enter the year of publication: "))
    price = float(input("Enter the price of the book: "))
    id = int(input("Enter the ID of the book: "))
    
    b = book(title, author, year, price,id)
    lst.append(b)

for i in lst:
    print(f"Title: {i.title}, Author: {i.author}, Year: {i.year}, Price: {i.price}, ID: {i.id}")
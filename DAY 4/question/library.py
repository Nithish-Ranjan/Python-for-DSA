class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrow = False
    
    def __str__(self):
        if self.is_borrow:
            return f'"{self.title}" by {self.author} (Borrowed)'
        else:
            return f'"{self.title}" by {self.author}'
    


class Member:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []

    def borrow(self, book):
        self.borrowed_books.append(book)

    def return_book(self, book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)

    def __str__(self):
        borrowed_titles = []
        for book in self.borrowed_books:
            borrowed_titles.append(book.title)
        return f"Member: {self.name}, Borrowed: {borrowed_titles}"

class Library:
    def __init__(self, name):
        self.name = name
        self.books = []
        self.members = []

    def add_book(self, book):
        for b in self.books:
            if b.title.lower() == book.title.lower():
                return False
        self.books.append(book)
        return True
    
    def book_status(self):  
        available = 0
        borrowed = 0

        for book in self.books:
            if book.is_borrow:
                borrowed += 1
            else:
                available += 1

        print("Available: ", available)
        print("Borrowed: ", borrowed)


    def remove_book(self, title):
        book = self.find_book_by_title(title)
        if book and not book.is_borrow:
            self.books.remove(book)
            return True
        return False

    def list_books(self):
        return [str(book) for book in self.books]
    
    def find_book_by_title(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                return book
        return None

    def add_member(self, member):
        for m in self.members:
            if m.name.lower() == member.name.lower():
                print("Member already exists.")
                return
        self.members.append(member)
        
    def search_books(self, query):
        result = []

        for book in self.books:
            if query.lower() in book.title.lower() or query.lower() in book.author.lower():
             result.append(book)

        return result

    def borrow_book(self, title, member_name):
        book = self.find_book_by_title(title)
        member = None
        for m in self.members:
            if m.name.lower() == member_name.lower():
                member = m
                break
        if not book:
            return "Book not found."
        if not member:
            return "Member not found."
        if book.is_borrow:
            return "Book already borrowed."
        book.is_borrow = True
        member.borrow(book)
        return "Book borrowed successfully."

    def return_book(self, title, member_name):
        book = self.find_book_by_title(title)
        member = None
        for m in self.members:
            if m.name.lower() == member_name.lower():
                member = m
                break
        if not book:
            return "Book not found."
        if not member:
            return "Member not found."
        if not book.is_borrow:
            return "Book is already available."
        if book not in member.borrowed_books:
            return "This member did not borrow the book."
        book.is_borrow = False
        member.return_book(book)
        return "Book returned successfully."
    
    def list_members(self):
        for member in self.members:
            print(member)

def main():
    library = input("Enter the name of the library: ").strip()
    library = Library(library)
    actions = {
        "1": "List all books",
        "2": "Search for a book",
        "3": "Add a new book",
        "4": "Remove a book",
        "5": "List members",
        "6": "Add member",
        "7": "Borrow a book",
        "8": "Return a book",
        "9": "Books Status",
        "10": "Exit"
    }

    while True:
        print(f"\nWelcome to {library.name}")
        for key, value in actions.items():
            print(f"{key}. {value}")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            print("Books in library:")
            for book in library.list_books():
                print("- " + book)

        elif choice == "2":
            query = input("Enter title or author to search: ").strip()
            results = library.search_books(query)
            if results:
                print("Search results:")
                for book in results:
                    print("- " + str(book))
            else:
                print("No books matched your search.")

        elif choice == "3":
            title = input("Enter book title: ").strip()
            author = input("Enter book author: ").strip()
            library.add_book(Book(title, author))
            print(f'Book "{title}" by {author} added.')

        elif choice == "4":
            title = input("Enter title of the book to remove: ").strip()
            if library.remove_book(title):
                print(f'Book "{title}" removed from library.')
            else:
                print(f'Unable to remove "{title}". It may not exist or is currently borrowed.')

        elif choice == "5":
            print("Library members:")
            library.list_members()

        elif choice == "6":
            name = input("Enter new member name: ")
            library.add_member(Member(name))
            print("Member added.")

        elif choice == "7":
            name = input("Enter member name: ").strip()
            title = input("Enter title of the book to borrow: ").strip()
            print(library.borrow_book(title, name))

        elif choice == "8":
            name = input("Enter member name: ").strip()
            title = input("Enter title of the book to return: ").strip()
            print(library.return_book(title, name))

        elif choice == "9":
            library.book_status()

        elif choice == "10":
            print("Goodbye")
            break

        else:
            print("Invalid option. Please choose again.")


if __name__ == "__main__":
    main()
# Tuple

CATEGORIES = ("Fiction", "Science", "History", "Tech", "Health")

# list
books = []

# a function to create a book and add it to the list.

def create_book(title, author, category, year):
    if category not in CATEGORIES:
        print(f"This book wasn't created becausee ,Category must be one of the following: {CATEGORIES}")
        return None
    
    book = {
        "title": title,
        "author": author,
        "category": category,
        "year": year
    }
    
    books.append(book)
    return book
    

# create a book:

create_book("Atomic Habits", "James Clear", "Fiction", 2018)
create_book("Daniel Lesiamon", "James Clear", "Fiction", 2018)
create_book("Dream Big", "Ben Carson", "Health", 2020)

print(books)

# Read all books

def read_books():
    print("Below are books in the shelf: \n")

    for book in books:
        print(f"Title of the book {book['title']}, auther of the book {book['author']}. ")
                     
# read_books()


# search book and return it

def search_book(title):
    trimmed_title = title.lower()
    
    for index in range(len(books)):
        book = books[index]
        if book["title"].lower() == trimmed_title:
            return book
                


# updating a book.

def update_book(current_title, new_title, new_author, new_year):
    # get the book we need to update from the list of books
    
    book = search_book(current_title)
    
    if book is None:
        print("The book doesn't exist within the records.")
        return False
    
    book["title"] = new_title,
    book["author"] = new_author,
    book["year"] = new_year
    
    print("\n Book updated successfully")
    

update_book("Daniel Lesiamon", "Rich Dad Poor Dad", "Robert", 2019)
# update_book("Mathetics", "Rich Dad Poor Dad", "Robert", 2019)


read_books()

    

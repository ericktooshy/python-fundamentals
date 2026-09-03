class Book:
    # class attribute
    CATEGORIES = ("Fiction", "Science", "History", "Tech", "Health")
    number_of_chapters = 32
    
    # instance attributes
    def __init__(self, title, author, year_of_publish):
        self._title = title # treated as internal, cannot be accessed anyhowly.
        self._author = author
        self._year_of_publish = year_of_publish
    
    # get, set
    
    # create a getter method to allow access of the internal
    @property # decorator
    def title(self):
        return self._title
        
    
    @title.setter
    def title(self, new_value):
        self._title = new_value
        
    @property
    def year(self):
        return self._year_of_publish
            
        
    @year.setter
    def year(self, new_value):
        if new_value > 2026:
            print("Give the correct value")
            raise ValueError("Year of publish cannot be greater than current year.")
        self._year_of_publish = new_value
        
    
   
            
    @property
    def author(self):
        return self._author
        
    @author.setter
    def author(self, new_value):
        self._author = new_value
    
    @classmethod
    def show_all_categories(cls):
        print(cls.CATEGORIES)
        


# we can now create an object out of the Book class

book1 = Book("Atomic Habits", "James Clear", 2018) # instance one of the Book class
book2 = Book("Dream Big", "Ben Carson", 2020) # instance two of the Book class

# book1 and book2 is the real object

# print(Book.CATEGORIES)
# print(book1.CATEGORIES)

# print(Book.number_of_chapters)
# print(book2.number_of_chapters)

book1.title = "George Okumu" # if title is not found, python is creating it a as anew attribute.

book2.year = 2024


book2.author ="Mike mugendi"
# accessing the attributes of the objects directly.
print(book1.year)
print(book2.year, book2.author)

# print(book1.__dict__)
# print(book2.__dict__)

Book.show_all_categories()
book1.show_all_categories()

Book.year




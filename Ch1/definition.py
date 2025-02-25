#creat a basic class
class Book:
    def __init__(self,title):
        self.title = title

#creat a instance of the class
book1 = Book("Brave New World")
book2 = Book("War and Peace")

print(book1)
print(book1.title)

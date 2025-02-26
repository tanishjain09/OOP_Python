#creat a basic class
class Book:
    def __init__(self,title,author,pages,price):
        self.title = title
        self.author = author
        self.pages = pages
        self.price = price
        self.__secret = "This is a secret attribute"
    def getprice(self):
        if hasattr(self,"_discount"):
            return self.price - (self.price * self._discount)
        return self.price

    def setdiscount(self,amount):
        self._discount = amount

class Newspaper:
    def __init__(self,name):
        self.name = name


#creat a instance of the class
book1 = Book("Brave New World","Leo Tolstoy",1225,39.95)
book2 = Book("War and Peace","JD Salinger",234,29.95)
n1 = Newspaper("The Washinton Post")
n2 = Newspaper("The New York Times")

print(type(book1))
# print(type(n2))
#
# print(type(book1) == type(book2))
# print(type(book1) == type(n2))


print(isinstance(book1,Book))
print(isinstance(n1,Newspaper))
print(isinstance(book2,Newspaper))
print(isinstance(n2,object))
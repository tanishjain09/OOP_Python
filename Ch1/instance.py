#creat a basic class
class Book:
    def __init__(self,title,author,pages,price):
        self.title = title
        self.author = author
        self.pages = pages
        self.price = price
        # self.__secret = "This is a secret attribute"
    def getprice(self):
        if hasattr(self,"_discount"):
            return self.price - (self.price * self._discount)
        return self.price

    def setdiscount(self,amount):
        self._discount = amount

#creat a instance of the class
book1 = Book("Brave New World","Leo Tolstoy",1225,39.95)
book2 = Book("War and Peace","JD Salinger",234,29.95)


print(book1.getprice())

print(book2.getprice())
book2.setdiscount(0.25)
print(book2.getprice())

# print(book2.__secret)

import math

class Book:
    def __init__(self, name: str, author: str, isbn: int, price: str) -> None:
        self.name = name
        self.author = author
        self.isbn = isbn
        self.price = price


def print_info(book: Book) -> None:
    maxlenvar = max(len(book.name), len(book.author), len(str(book.isbn)), len(str(book.price)))
    print("name:" + " " * (maxlenvar - len("name:")) + book.name)
    print("author:" + " " * (maxlenvar - len("author:")) + book.author)
    print("isbn:" + " " * (maxlenvar - len("isbn:")) + str(book.isbn))
    print("price:" + " " * (maxlenvar - len("price:")) + str(book.price))
""" 
CC - Jakub Sukdol, this part can be only used for personal use. You must not claim the code as your, redistribute or edit it to other users or sell it for financial profit.
"""

def draw_cover(self):
        print("")
        delka = max(len(self.author),len(self.name))
        print("-"*(delka+4))
        for vys in range(10):
            print("|",end="")
            if vys == 2:
                x = round((delka+2-len(self.name))/2)
                print(" "*x + self.name + " "*x,end="")
            elif vys == 8:
                x = round((delka+2-len(self.author))/2)
                print(" "*x + self.author + " "*x,end="")
            else:
                print(" "*(delka+2),end="")
            print("|")
        print("-"*(delka+4))

print_info(Book("Pierre Gasly", "Aleška", 65646546546, 30))
draw_cover(Book("Pierre Gasly", "Aleška", 65646546546, 30))

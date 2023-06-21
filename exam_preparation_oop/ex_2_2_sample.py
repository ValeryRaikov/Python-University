class Book:
    def __init__ (self,name,code, price, year, author):
        self.book_name= name
        self.book_code=code
        self.book_price=price
        self.book_year=year
        self.book_author=author
    def __str__(self):
        return str.format("Name {} code {} price {} year {} author {} ",self.book_name, self.book_code , self.book_price, self.book_year, self.book_author)

books=[Book("Lord",2034,5.64,1995,"George"),Book("Ford",1034,8.64,2000,"Seorge"),Book("Psichologi",3034,15.64,1998,"Aristotel"),Book("The Quinn",5034,55.64,2020,"Jack")]

def sort_name(b_li):
    result_books= sorted(b_li, key= lambda x: x.book_name, reverse=True)
    for l in result_books:
        print(l)
def author(author,b_list):
    for b in b_list:
        if b.book_author==author:
            print(b)
def search_book(code):
    for i in range(len(books)):
        currentbook = books[i]
        if currentbook.book_code == code:
            print(currentbook.book_year)
            return
    print("The book is not found!")
sort_name(books)
author("George",books)
search_book(1034)
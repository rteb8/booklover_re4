class BookLover:
    import pandas as pd

    def __init__(self, name, email, fav_genre, num_books = 0, book_list = pd.DataFrame({'book_name':[], 'book_rating':[]})):
        self.name = name
        self.email = email
        self.fav_genre = fav_genre
        self.num_books = num_books
        self.book_list = book_list

    def add_book(self, book_name, rating):
        import pandas as pd

        if book_name not in self.book_list['book_name'].values:
            new_book = pd.DataFrame({
                'book_name': [book_name], 
                'book_rating': [rating]
                })
            self.book_list = pd.concat([self.book_list, new_book], ignore_index=True)
            self.num_books += 1
        else:
            print(book_name + " is already in book list")
        
    def has_read(self, book_name):
       read_books = [book_name == name for name in self.book_list['book_name']]
       if True in read_books:
            return True
       else: 
            return False
    
    def num_books_read(self):
        return len(self.book_list)
    
    def fav_books(self):
        fav_books = self.book_list[self.book_list['book_rating'] > 3]
        return fav_books
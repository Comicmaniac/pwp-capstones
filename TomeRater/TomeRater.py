# TomeRater class

class TomeRater:
    def __init__(self):
        self.users = {}
        self.books = {}
    
    def create_book(self, title,isbn):
        return Book(title, isbn)

    def create_novel(self, title, author, isbn):
        return Fiction(title, author, isbn)

    def create_non_fiction(self, title, subject, level, isbn):
        return Non_Fiction(title, subject, level, isbn)

    def add_book_to_user(self, book, email, rating=None):
        if email not in self.users.keys():
            print('No user with email %s' % (email))
        else:
            user = self.users.get(email)
            user.read_book(book, rating)
            user.add_rating(book, rating)
            if rating != None:
                book.add_rating(rating)
            if book not in self.books:
                self.books[book] = 1
            else:
                self.books[book] += 1


    def add_user(self, name, email, user_books=None):
        new_user = User(name, email)
        self.users[new_user.email] = new_user
        self.user_books = user_books
        if self.user_books != None:
            for book in user_books:
                self.add_book_to_user(book, email)


# TomeRater methods for analysis

    def print_catalog(self):
        for book in self.books:
            print(book.title)

    def print_users(self):
        for user in self.users:
            print(user)


    def print_user(self, user, email):
        other_user = User(user, email)
        for user in self.users:
            if user == other_user:
                print(user)        


    def get_most_read_book(self):
        book_read_times = 0
        for book in self.books:
            if self.books[book] > book_read_times:
                book_read_times = self.books[book]
                most_read_book = book.title
        return most_read_book



    def highest_rated_book(self):
        highest_rating = 0
        highest_book = []
        for book in self.books:
            rating = book.get_average_rating()
            if rating > highest_rating:
                highest_rating = rating
                highest_book = book
        return highest_book


    def most_positive_user(self):
        user_highest_average_rating = 0
        for email, user in self.users.items():
            average_rating = user.get_average_rating()
            if average_rating > user_highest_average_rating:
                highest_average_rating = average_rating
                user_highest_average_rating = user.name
            return user_highest_average_rating



# User class

class User(object):
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.books = {}

    def get_email(self):
        return self.email

    def change_email(self, address):
        self.address = address
        for mail in email:
            address = mail
            print('The email address has been updated.')

    def add_rating(self, book, rating = None):
            if rating != None:
                return book.add_rating(rating)

    def __repr__(self):
        return 'User %s, email: %s, number of books read: %s.' % (self.name, self.email, len(self.books))

    def __eq__(self, other_user):
        if other_user is not User: 
            return False
        return self.name == other_user.name and self.email == other_user.email
        
# User class methods for analysis

    def read_book(self, book, rating = None):
        if rating != None and rating >= 0 and rating <= 4:
            self.books[book] = book
            self.books[book].rating = rating


    def get_average_rating(self):
        sum_rating = 0
        if len(self.books)>0:
            for b, book in self.books.items():
                sum_rating += book.rating
            return (sum_rating/len(self.books))
        else:
            return 0


# Book class

class Book(object):
    def __init__(self, title, isbn):
        self.title = title
        self.isbn = isbn
        self.ratings = []

    def get_title(self):
        return self.title

    def get_isbn(self):
        return self.isbn


    def set_isbn(self, new_isbn):
        self.new_isbn = new_isbn
        for book in self.books.keys():
            new_isbn = isbn
            print('The isbn has been updated.')

    def add_rating(self, rating):

        if rating >= 0 and rating <= 4:
            self.ratings.append(rating)
        else:
            print('Invalid Rating')

    def __repr__(self):
        return 'Book title %s, isbn %s,' % (self.title, self.isbn)

    def __eq__(self, other_book):
        if other_book is not Book: 
            return False
        return self.title == other_book.title and self.isbn == other_book.isbn

# Book class methods for analysis and changes

    def get_average_rating(self):
        if len(self.ratings) > 0: 
            return sum(self.ratings)/len(self.ratings)
        else:
            print('No ratings yet')
        return 0


    def __hash__(self):
        return hash((self.title, self.isbn))


# Fiction class, subclass of Book

class Fiction(Book):
    def __init__(self, title, isbn, author):
        super().__init__(title, isbn)
        self.author = author

    def get_author(self, author):
        return self.author

    def __repr__(self):
        return "%s by %s" % (self.title, self.author)


#Non fiction class, subclass of Book

class Non_Fiction(Book):
    def __init__(self, title, subject, level, isbn):
        super().__init__(subject, level)
        self.subject = subject
        self.level = level

    def get_subject(self):
        return self.subject

    def get_level(self):
        return self.level

    def __repr__(self):
        return "%s, a %s manual on %s" % (self.title, self.level, self.subject)
        

##κλαση BookStore που περιέχει ολα τα βιβλία και την διεπαφή του χρήστη 
class BookStore:
    def __init__(self):
        # Αρχικοποίηση λίστας για την αποθήκευση των βιβλίων
        self.book_list = []
        
    ##μεθοδος addBook(), για εισαγωγή ενος βιβλίου στην λιστα self.book_list
    def addBook(self, *args):
        #αρχικοποιηση μιας temp μεταβλητης να ειναι το Book που εισήγαγε ο χρηστης
        #ωστε μετα να εχουμε δυνατοτητα να το εισαγουμε στην λιστα οπως και να το τυπώσουμε
        temp_book = Book(*args)
        self.book_list.append(temp_book)
        print(f"{temp_book}(Επιτυχής προσθήκη!)")

    #μεθοδος searchBooksByAuthor(), για ελεγχο αν υπάρχει το ονομα που εδωσε
    #ο χρηστης μεσα στο attribute author καποιου Book αντικειμενου στην λιστα
    #self.book_list, αν υπάρχει εισάγει ολο το αντικείμενο μεσα στην λιστα
    #self.authors_list και την επιστρεφει στο τελος, αν δεν βρεθεί συγγραφέας
    #επιστρέφει μια κενή λίστα 
    def searchBooksByAuthor(self, author = None):
        #αρχικοποιηση λιστας self.authors_list
        self.authors_list = []
        #αμυντικος προγραμματισμός για την εισαγωγή του author
        while True:
            try:
                author = str(input("Πληκτρολογήστε όνομα και επώνυμο συγγραφέα: "))
                if author.isnumeric():
                    raise ValueError
                break
            except ValueError:
                print("Λάθος καταχώρηση.")
        for book in self.book_list:
            if book.author == author:
                self.authors_list.append(str(book))
        return self.authors_list
    
    #μεθοδος deleteBookWithISBN(), για διαγραφή ενός αντικειμένου Book αφού ο χρήστης
    #εισάγει σωστα το isbn του βιβλιου προς διαγραφη και αντιστοιχει με το attribute
    #isbn του αντικειμένου, αν δεν βρεθει αντικείμενο ενημερώνει αναλόγως
    def deleteBookWithISBN(self, isbn = None):
        #αμυντικος προγραμματισμος για την εισαγωγή του isbn
        while True:
            try:
                isbn = str(input("Πληκτρολογήστε ISBN: "))
                if len(isbn) != 10:
                    raise ValueError
                if not isbn.isnumeric():
                    raise ValueError
                break
            except ValueError:
                print("Λάθος καταχώρηση.")
        for book in self.book_list:
            if book.isbn == isbn:
                self.book_list.remove(book)
                #αν διαγραφεί ένα Book() αντικείμενο απο την λιστα self.book_list
                #τοτε μειώνεται η μεταβλητή κλάσης για την καταμέτρηση των Book()
                #κατα 1
                Book.count -= 1
                print(f"Το βιβλίο {book} διαγράφηκε.")
                return
        print("Το βιβλίο δεν βρέθηκε.")

    #χρήση της ειδικής συνάρτησης __str__ για αλλαγή του τρόπου εκτυπώματος
    #ενος αντικειμένου BookStore()
    def __str__(self):
        if not Book.count:
            all_books_str = "Δεν βρέθηκαν βιβλία."
        else:
            all_books_str = f"Πλήθος βιβλίων: {Book.count}\n"
            for book in self.book_list:
                all_books_str += str(book) + "\n"
        return all_books_str


##κλάση Book() που περιέχει όλα τα attributes ενος βιβλίου
class Book:
    count = 0#μεταβλητή κλάσης Book() για καταμέτρηση των Book() αντικειμένων
    def __init__(self, title, author, year, price, isbn):
        ##αμυντικος προγραμματισμος σε περιπτωση εισαγωγής λάθος τύπου δεδομενων
        ##σε οποιοδηποτε attribute ενος book
        if type(title) != str:
            raise TypeError
        self.title = title
        if type(author) != str:
            raise TypeError
        self.author = author
        if type(year) != int:
            raise TypeError
        self.year = year
        if type(price) != float:
            raise TypeError
        self.price = price
        #εκτος απο type handling κοιταμε και αν το length του isbn δεν ειναι 10 ή 13
        if type(isbn) != str or len(isbn) != 10 and len(isbn) != 13:
            raise TypeError
        self.isbn = isbn
        # κάθε φορά που φτιάχνεται ένα Book() αντικείμενο αυξάνεται αυτη η μεταβλητή
        Book.count += 1

    #ειδική συνάρτηση __str__ για αλλαγή του τρόπου εκτυπώματος ενός αντικειμένου Book()
    def __str__(self):
        return f"Βιβλίο: {self.title}, Συγγραφέας: {self.author}, Έτος: {self.year}, Τιμή: {self.price}€, ISBN: {self.isbn}."


##ενδεικτική χρήση των BookStore() και Book() Κλάσεων
if __name__=="__main__":
    bs = BookStore()
    print("\n0) Καταχώρηση Βιβλίων\n=====================")
    bs.addBook("Python Crash Course", "Eric Matthews", 2016, 27.95, "1593279280")
    bs.addBook("Learning Python ", "Mark Lutz", 2021, 40.29, "1449355730")
    bs.addBook("Head First Python", "Paul Barry", 2017, 36.25, "7519813630")
    bs.addBook("Introduction to Machine Learning with Python", "Andreas C. Mulle", 2020, 31.99, "1449369413")
    bs.addBook("Python for Data Analysis","Wes McKinney", 2022, 38.38, "1098104032")
    bs.addBook("Deep Learning with Python", "Francois Chollet", 2017, 30.20, "1617284433")

    print("\n1) Αναζήτηση βιβλίων με το όνομα και επώνυμο συγγραφέα\n======================================================")
    bk = bs.searchBooksByAuthor()
    if bk:
        print("Τα βιβλία που βρέθηκαν είναι:")
        for b in bk:
            print("\t",b)
    else:
        print(" Δεν υπάρχουν βιβλία με αυτόν τον συγγραφέα ")
    print("\n2) Διαγραφή βιβλίου με βάση το ISBN\n===================================")
    bs.deleteBookWithISBN()
    print("\n3) Εκτύπωση όλων των διαθέσιμων βιβλίων με όλη την σχετική πληροφορία\n=====================================================================")
    print(bs)

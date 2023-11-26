from market import *

# Χρήση της βιβλιοθήκης pickle για την αποθήκευση και ανάκληση
# των περιεχομένων του καλαθιού
import pickle 

class ShoppingCartStore():
    '''Κλάση αποθήκευσης περιεχομένων καλαθιού σε αρχείο pickle'''

    def __init__(self, filename):
        '''Αρχικοποίηση αποθήκης περιεχομένων καλαθιού.'''
        self.store = filename

    def save(self, data):
        # Υποερώτημα α
        # αποθήκευση σε αρχείο pickle, ανοιγμα αρχείου σε μορφή write binary, χρήση της Pickle dump για να γραφτούν τα περιεχόμενα του data στο αρχείο, 
        # τύπωμα μυνήματος σφάλματος σε περίπτωση αποτυχίας 
        try:
            with open(self.store, "wb") as f:
                pickle.dump(data, f)
            print("Επιτυχης αποθήκευση περιεχομένων καλαθιού.\n")
        except (IOError, OSError, ValueError, TypeError):
            print("\nΑποτυχία εγγραφής.\n")

    def load(self):
        # Υποερώτημα β
        #loading ενός αρχείου Pickle, άνοιγμα αρχείου σε μορφη read binary,αποθήκευση των περιεχομένων σε μεταβλητη με ονομα loaded_shopping_cart, και επιστροφη του αν γινει σωστα το loading,
        #αν προκληθει καποιο αλλο σφαλμα η το αρχείο δεν υπάρχει, επιστροφή κενής λίστας και τύπωμα μυνήματος σφάλματος        
        try:
            with open(self.store, "rb") as f:
                loaded_shopping_cart = pickle.load(f)
                print("\nΕπιτυχης ανάκληση περιεχομένων αποθηκευμένου καλαθιού.\n")
                return loaded_shopping_cart
        except (FileNotFoundError, IOError, OSError, ValueError, TypeError):
            loaded_shopping_cart = []
            print("\nΑποτυχία ανάκλησης.\n")
            return loaded_shopping_cart



class StorableShoppingCart(ShoppingCart):
    '''Κλάση καλαθιού αγορών που μπορεί να αποθηκευτεί.'''
    
    def __init__(self, market, filename):
        '''Δημιουργία (άδειου) καλαθιού που μπορεί να αποθηκευτεί.''' 
        # Υποερώτημα γ
        # δημιουργία αντικειμένου ShoppingCartStore με το filename που πήραμε απο τον constructor της StorableShoppingCart
        self.shopping_cart = ShoppingCartStore(filename)

        # Αρχικοποίηση των άλλων ιδιοτήτων με χρήση της γονικής __init__ 
        super().__init__(market)

    def shopping_cart_management(self):
        '''Χειρισμός λειτουργιών καλαθιού.'''
        while True:
            print("Επιλογές")
            print("========")
            print("1. Προσθήκη προϊόντων στο καλάθι, ", end="")
            print("2. Εμφάνιση περιεχομένου καλαθιού, ", end="")
            print("3. Αφαίρεση προϊόντος, ", end="")
            print("4. Πληρωμή, ", end="")
            print("5. Αποθήκευση καλαθιού, ", end="")
            print("6. Ανάκληση καλαθιού")
            choice = input("Εισάγετε την επιλογή σας: ")
            if choice == "1":
                self.add_products()
            elif choice == "2":
                self.display_basket()
            elif choice == "3":
                self.remove_product()
            elif choice == "4":
                self.buy_products()
                break
            elif choice == "5":
                #κλήση της μεθόδου save στο αντικείμενο self.shopping_cart με όρισμα τα περιεχόμενα του παρόν καλαθιού
                if self.contents:
                    self.shopping_cart.save(self.contents)
                else:
                    print("Δεν υπάρχουν περιεχόμενα στο καλάθι.\n")
            elif choice == "6":
               #κλήση της μεθόδου load, στο αντικείμενο self.shopping_cart, αναθέτωντας την τιμή που θα επιστραφεί (δηλαδή την αποθηκευμένη λίστα)
               #στο self.contents το οποίο είναι το παρόν καλάθι 
                self.contents = self.shopping_cart.load()
            else:
                print("Παρακαλώ εισάγετε έγκυρη επιλογή")


if __name__ == "__main__":
    mini_market_products = [
        ("ΓΑΛΑ 1LT", 1.5),
        ("ΓΙΑΟΥΡΤΙ ΣΤΡΑΓΓΙΣΤΟ 2%", 2.0),
        ("ΠΑΓΩΤΟ", 2.5),
        ("ΝΕΣ ΚΑΦΕ", 7.5),
        ("ΜΠΙΣΚΟΤΑ ΓΕΜΙΣΤΑ", 1.0),
        ("ΣΑΛΑΤΑ ΣΕΦ", 1.0),
        ("ΤΥΡΙ ΤΟΣΤ", 6.0),
        ("ΕΞ. ΠΑΡΘΕΝΟ ΕΛΑΙΟΛΑΔΟ", 8.0),
        ("ΚΑΦΕΣ ΦΙΛΤΡΟΥ", 7.0),
        ("ΨΩΜΙ ΤΟΣΤ", 1.5),
    ]
    mini_market = Market(*mini_market_products)
    cart_file = "mycart"
    StorableShoppingCart(mini_market, cart_file)


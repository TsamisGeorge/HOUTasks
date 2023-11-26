products = [("ΓΑΛΑ 1LT",1.5), ("ΓΙΑΟΥΡΤΙ ΣΤΡΑΓΓΙΣΤΟ 2%",2.0), ("ΠΑΓΩΤΟ", 2.5), ("ΝΕΣ ΚΑΦΕ", 7.5), ("ΜΠΙΣΚΟΤΑ ΓΕΜΙΣΤΑ", 1.0),
            ("ΣΑΛΑΤΑ ΣΕΦ", 1.0), ("ΤΥΡΙ ΤΟΣΤ", 6.0), ("ΕΞ. ΠΑΡΘΕΝΟ ΕΛΑΙΟΛΑΔΟ", 8.0), ("ΚΑΦΕΣ ΦΙΛΤΡΟΥ", 7.0), ("ΨΩΜΙ ΤΟΣΤ", 1.5)]
shopping_cart = []#αρχικοποίηση του shopping_cart
def add_products():
    print("\n")
    while True:
        for index,item in enumerate(products):#τυπωμα προιόντων
            print("Προϊον #{}: {}".format(index,item[0]))
        print("\n")
        product_number = int(input("Επιλέξτε αριθμό προϊόντος: "))
        quantity = int(input("Εισάγετε την επιθυμητή ποσότητα: "))
        found = False #αρχικοποιηση ως false
        for index, item in enumerate(shopping_cart): #ψαχνει αν υπαρχει ήδη το αντικείμενο 
            if item[0] == product_number: #αν υπαρχει εισάγει μονο την νεα ποσοτητα+την παλια
                t = (item[0], item[1] + quantity)
                shopping_cart[index] = t
                found = True
                break
        if not found: # αν δεν υπαρχει εισάγη και το προιόν και την ποσοτητα
            t = (product_number,quantity)
            shopping_cart.append(t)
        restart = "temp"
        while (restart != "ν" and restart != "ο"):
            restart=input("Επιθυμείτε να εισάγετε άλλο προϊόν(ν/ο): ")
            if (restart!= "ν" and restart !="ο"):
                print("Παρακαλώ εισάγετε μία επιλογή.")
        if restart == "ν":
            print("\n")
            continue
        else:
            break
    

def display_basket():
    total=0
    if not shopping_cart:
        print("\nΔεν υπάρχουν προϊόντα στο καλάθι.")
    else: #μορφοποιημένο τύπωμα προιόντων με f-string
        print(f"{'ΑΑ' : <4}{'ΕΙΔΟΣ' : <22}{'ΤΜΧ' : >8}{'ΤΙΜΗ ΤΜΧ' : >13}{'ΑΞΙΑ' : >9}")
        for i in range(0, len(shopping_cart)):
            product = products[shopping_cart[i][0]][0]
            items = shopping_cart[i][1]
            item_value = products[shopping_cart[i][0]][1]
            final_item_value = items*item_value
            total+=final_item_value
            print(f"{i+1 : <4}{product : <22}{items : >8}{item_value: >12}€{final_item_value : 8}€")    
        print(f"\n{'ΣΥΝΟΛΟ' : >49}{total : > 6}€")
    return total #επιστροφη του συνολου πληρωμης

def remove_product():
    display_basket()
    line = input("Επιλέξτε γραμμή προς αφαίρεση: ")
    line = int(line)-1 #αν ο χρηστης πχ βαλει 1,θελουμε την πρωτη γραμμη αρα 1-1=0
    confirmation = "temp"
    while (confirmation != "ν" and confirmation != "ο"):
        confirmation=input("Παρακαλώ επιβεβαιώστε την αφαίρεση(ν/ο): ")
        if (confirmation!= "ν" and confirmation !="ο"):
            print("Παρακαλώ εισάγετε μία επιλογή.")
    if confirmation =="ν":
        found = False
        for index,element in enumerate(shopping_cart): #αν βρεθει οντως η γραμμη
            if line == index:
                found = True
                break
        if found:
            del shopping_cart[line]
            print("\nΤο προϊόν αφεραίθηκε επιτυχώς από το καλάθι.")
        else:
            print("\nΗ γραμμή δεν βρέθηκε.")
        

def buy_products():
    if not shopping_cart:#αν δεν υπαρχει κατι στο καλαθι
        print("Το καλάθι είναι άδειο.")
    else: #αν υπαρχει
        price=display_basket()#εισάγη την επιστρεφομενη τιμη του display_basket στο price
        confirm = "temp"
        while (confirm != "ν" and confirm != "ο"):
            confirm=input("Παρακαλώ επιβεβαιώστε την αγορά(ν/ο): ")
            if (confirm!= "ν" and confirm !="ο"):
                print("Παρακαλώ εισάγετε μία επιλογή.")
        if confirm =="ν":#αν υπαρξει επιβεβαιωση
            member_card = "temp"
            while (member_card != "ν" and member_card != "ο"):
                member_card = input("Έχετε κάρτα μέλους(ν/ο): ")
                if (member_card!= "ν" and member_card !="ο"):
                    print("Παρακαλώ εισάγετε μία επιλογή.")
            if member_card == "ν":#αν εχει καρτα μελους
                discount = (7/100)*price
                final_price = price-discount
                print("Έκπτωση {:.2f}€".format(discount))
                print("Παρακαλούμε πληρώστε {:.2f}€".format(final_price))
                print("Σας ευχαριστούμε για την αγορά σας.")
            else:#αν δεν εχει καρτα μελους
                print("Παρακαλούμε πληρώστε {:.2f}€".format(price))
                print("Σας ευχαριστούμε για την αγορά σας.")

if __name__ == "__main__":
    while True:
        print("\nΕπιλογές")
        print("========")
        print("1. Προσθήκη προϊόντων στο καλάθι.\n2. Εμφάνιση περιεχομένου καλαθιού.\n3. Αφαίρεση προϊόντος.\n4. Πληρωμή.\n")
        choice = input("Εισάγετε την επιλογή σας: ")
        if choice == "1":
            add_products()
        elif choice == "2":
            display_basket()
        elif choice == "3":
             remove_product()
        elif choice == "4":
            buy_products()
            break
        else:
            print("\nΠαρακαλώ εισάγετε έγκυρη επιλογή.\n")

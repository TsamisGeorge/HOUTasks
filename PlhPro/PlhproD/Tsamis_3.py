import sqlite3

###  ΒΟΗΘΗΤΙΚΕΣ ΣΥΝΑΡΤΗΣΕΙΣ ΓΙΑ ΧΡΗΣΗ ΣΤΟ ΠΡΟΓΡΑΜΜΑ  ###
########################################################

#Συνάρτηση για να ανοίξουμε ενα connection στην βάση δεδομένων 
def open_connection():
    try:
        # Άνοιγμα του connection με χρήση της .connect() και όρισμα το .db αρχείο που θέλουμε να ανοίξουμε
        conn = sqlite3.connect("supermarket.db")
        # επιστροφή του connection, εκτός αν κάτι πάει λάθος τότε τυπώνεται μύνημα του λάθους
        return conn
    except sqlite3.Error as e:
        print(f"Error: {e}")

#Συνάρτηση για να κλείσουμε το connection της βάσης δεδομένων
def close_connection(connection):
    try:
        # χρήση της .close() στο αντικείμενο connection που δίνεται σαν όρισμα, αν οτιδήποτε πάει στραβα
        # τύπωμα του μυνήματος λάθους
        connection.close()
    except sqlite3.Error as e:
        print(f"Error: {e}")

#Συνάρτηση για να παίρνουμε τα ονόματα ενός συγκεκριμένου table σε μια βαση δεδομένων
def get_column_names(table):
    connection = open_connection()
    cursor = connection.cursor()
    # εκτέλεση του query PRAGMA table_info({table}) ώστε να φέρουμε την δομή του πίνακα
    cursor.execute(f"PRAGMA table_info({table})")
    # απο τα επιστρεφόμενo αποτελέσμα (λίστα με πλειάδες) θέλουμε μόνο την το δεύτερο στοιχείο κάθε πλειάδας (όνομα γνωρίσματος)
    # συνεπτιγμένη λίστα που κάνει ακριβώς αυτο που θέλουμε
    col_names = [col[1] for col in cursor.fetchall()]

    #κλείσημο του cursor και του connection, επιστροφή των ονομάτων γνωρίσματος
    cursor.close()
    close_connection(connection)
    return col_names



###  ΒΑΣΙΚΕΣ ΣΥΝΑΡΤΗΣΕΙΣ ΠΡΟΓΡΑΜΜΑΤΟΣ  ###
##########################################

#Συνάρτηση προβολής εγγραφών ενός πίνακα που δίνεται ως όρισμα
def show_records(table):

    '''Η συνάρτηση αυτή καλείται όταν θέλουμε να δείξουμε τις εγγραφές ενός πίνακα στη Β.Δ.'''
    # Υποερώτημα α

    # κλήση της get_column_names όρισμα το table που δόθηκε σαν όρισμα στην show records
    column_names = get_column_names(table)
    # ενδεικτικό γραφικό τύπωμα των ονομάτων
    print("="*len(column_names)*16)
    for field in column_names:
        print(f"{field:<16}",end="")
    print("")
    print("-"*len(column_names)*16)

    # ανοιγμα του connection, εκτέλεση του ερωτήματος με .format το παρον table και τύπωμα του
    connection = open_connection()
    sql = "SELECT * FROM {}"
    cursor = connection.cursor()
    cursor.execute(sql.format(table))
    results = cursor.fetchall()
    close_connection(connection)
    for entry in results:
        for field in entry:
            print(f"{field:<16}",end="")
        print("")
    print("="*len(column_names)*16)

  

'''Η συνάρτηση αυτή καλείται όταν θέλουμε να εισάγουμε νέα εγγραφή στον πίνακα Customers'''
def register_customer(name, surname,email):
    # Υποερώτημα β

    # άνοιγμα του connection και εκτέλεση του ερωτήματος sql με tuple όρισμα το query_parameters
    # ώστε τα ορίσματα της register_customer να μπουν στην σωστή θέση του ερωτήματος πριν την εκτέλεση
    sql = "INSERT INTO Customers (name, surname,email) VALUES (?,?,?)"
    connection = open_connection()
    try:
        cursor = connection.cursor()
        query_parameters = (name, surname, email)
        cursor.execute(sql, query_parameters)
        connection.commit()
        print(f"\nO πελάτης {name} {surname} καταχωρήθηκε επιτυχώς\n")
    except sqlite3.Error as e:
        print(f"Error: {e}")
    close_connection(connection)
    

'''Η συνάρτηση αυτή καλείται όταν θέλουμε να διαγράψουμε μία εγγραφή από τον πίνακα Customers'''
def delete_customer(code):
    # Υποερώτημα γ

    sql = "DELETE FROM Customers WHERE id == (?)" 
    connection = open_connection()
    try:
        cursor = connection.cursor()
        query_parameters = (code)
        cursor.execute(sql, query_parameters)
        connection.commit()
        print(f"\nΟ πελάτης με id {identification} διαγράφτηκε επιτυχώς.\n")
    except sqlite3.Error as e:
        print(f"Error: {e}")
    close_connection(connection)


    
'''Η συνάρτηση αυτή καλείται όταν θέλουμε να δούμε όλες τις εγγραφές ενός πίνακα της Β.Δ.'''
def hasRows(table):
    sql = "SELECT * FROM {}"
    try:
        with sqlite3.connect('supermarket.db') as conn: #Σύνδεση με τη Β.Δ. supermarket
            cursor = conn.cursor()
            cursor.execute(sql.format(table))#Εκτέλεση του ερωτήματος (query) 
            results = cursor.fetchall()
            return results
    except sqlite3.Error as err:
            print("Error: ",err) #Προβολή μηνύματος σφάλματος
            return False


# Κυρίως Πρόγραμμα
# Συμβολοσειρά με τις επιλογές του menu της εφαρμογής
supermarket_menu = '''Επιλογές συστήματος:
1. Προβολή Πελατών
2. Προβολή Προϊόντων
3. Προβολή Αγορών
4. Καταχώρηση Πελάτη
5. Διαγραφή Πελάτη
6. Έξοδος
Δώστε την επιλογή σας: '''

# Υλοποίηση ενεργειών του menu της εφαρμογής
while True:
    choice = input(supermarket_menu)
    if choice == '1':
        # Προβολή των πελατών
        show_records("Customers")
    elif choice == '2':
        # Προβολή των προϊόντων
        show_records("Products")
    elif choice == '3':
        # Προβολή των αγορών
        show_records("Purchases")
    elif choice == '4':
        # Καταχώρηση νέου πελάτη
        name = input("Καταχώρησε το όνομα του πελάτη: ")
        surname = input("Καταχώρησε το επώνυμο του πελάτη: ")
        email = input("Καταχώρησε το email του πελάτη: ")
        register_customer(name,surname,email)
    elif choice == '5':
        # Διαγραφή πελάτη βάση του id του, κατόπιν ελέγχου, εάν υπάρχουν
        # εγγραφές εντός του πίνακα
        check_entries = hasRows("Customers")
        if check_entries:
            identification = input("Δώσε το id του πελάτη προς διαγραφή: ")
            delete_customer(identification)
        else:
            print("\nΔεν υπάρχουν πελάτες για διαγραφή.\n")
    elif choice == '6':
        print("Τέλος Προγράμματος!")
        break
    else:
        # Μήνυμα λάθους σε περίπτω λανθασμένης επιλογή
        print("Λάθος επιλογή. Παρακαλώ επιλέξτε από 1 έως 6 \n") 


import hashlib
from getpass import getpass

user_password_dict = {}
failed_counts = {} #αποτυχημένες συνδεσεις
successful_counts = {} #επιτυχημένες συνδεσεις

def hash_password(plain_password):
    return hashlib.sha224(plain_password.encode("UTF-8")).hexdigest()


def new_user():
    #με χρήση try...except ανεβασμα errors σε περιπτωση που δωθει μη επιθυμητο Input η ο χρήστης που δωθει υπαρχει ηδη στο συστημα
    try:
        username = input("Εισάγετε το αναγνωριστικο χρήστη: ")
        if username in user_password_dict:
            raise ValueError("\nΟ χρήστης {} υπάρχει ήδη στο συστημα.\n".format(username))
        if len(username)<3:
            raise ValueError("\nΤο αναγνωριστηκό πρέπει να είναι τουλάχιστον 3 χαρακτήρες.\n")
        password = getpass("Εισάγετε το συνθηματικό: ")
        confirm_password = getpass("Επιβεβαίωση συνθηματικού: ")
        if len(password)<3 or len(confirm_password)<3:
            raise ValueError("\nΤο συνθηματικό πρέπει να είναι τουλάχιστον 3 χαρακτήρες.\n")
        if password != confirm_password:
            raise ValueError("\nΤα συνθηματικά δεν ταιριάζουν.\n")
        user_password_dict[username] = hash_password(password)
        print("\nΟ χρήστης {} εισήχθη στο σύστημα.\n".format(username))
    except ValueError as e:
        print(e)


def update_password():
    #με χρήση try...except ανεβασμα errors σε περιπτωση που δωθει μη επιθυμητο Input η ο χρήστης που δωθει δεν υπάρχει στο συστημα
    try:
        username = input("Εισάγετε το αναγνωριστικο χρήστη: ")
        if username not in user_password_dict:
            raise ValueError("\nΟ χρήστης {} δεν υπάρχει στο συστημα.\n".format(username))
        if len(username)<3:
            raise ValueError("\nΤο αναγνωριστηκό πρέπει να είναι τουλάχιστον 3 χαρακτήρες.\n")
        password = getpass("Εισάγετε το συνθηματικό: ")
        if hash_password(password) != user_password_dict[username]:
            raise ValueError("\nΛανθασμένο συνθηματικό.\n")
        new_pass = getpass("Εισάγετε το νέο συνθηματικό: ")
        confirm_new_pass = getpass("Επιβεβαίωση νέου συνθηματικού: ")
        if len(new_pass)<3 or len(confirm_new_pass)<3:
            raise ValueError("\nΤο συνθηματικό πρέπει να είναι τουλάχιστον 3 χαρακτήρες.\n")
        if new_pass != confirm_new_pass:
            raise ValueError("\nΤα συνθηματικά δεν ταιριάζουν.\n")
        user_password_dict[username] = hash_password(confirm_new_pass)
        print("\nΈγινε αλλαγή συνθηματικού γιά τον χρήστη {}.\n".format(username))
    except ValueError as e:
        print(e)


def login():
    #με χρήση try...except ανεβασμα errors σε περιπτωση που δωθει μη επιθυμητο Input η ο χρήστης που δωθει δεν υπάρχει στο συστημα
    try:
        username = input("Εισάγετε το αναγνωριστικο χρήστη: ")
        if username not in user_password_dict:
            raise ValueError("\nΟ χρήστης {} δεν υπάρχει στο συστημα.\n".format(username))
        password = getpass("Εισάγετε το συνθηματικό: ")
        if hash_password(password) != user_password_dict[username]:
            failed_counts[username] = failed_counts.get(username,0) + 1
            raise ValueError("\nΛάθος συνθηματικό.\n")
        successful_counts[username] = successful_counts.get(username,0) + 1
        print("\nΕπιτυχημένες προσπάθειες σύνδεσης: {}".format(successful_counts.get(username)))
        print("Αποτυχημένες προσπάθειες σύνδεσης: {}\n".format(failed_counts.get(username,0)))
    except ValueError as e:
        print(e)



def display_users():
    if not user_password_dict: # αν δεν υπαρχουν χρηστες στο συστημα ενημερώνει αναλόγως
        print("\nΔεν υπάρχουν χρήστες στο σύστημα.\n")
    else: # αν υπαρχουν τυπωνει τους χρηστες
        sorted(user_password_dict, key=str) #sort το λεξικο αλφαβητικα
        print(f"\n{'Αναγνωριστικά' : <15}{'Συνθηματικά' : <56}{'Επιτ. συνδέσεις' : >18}{'Αποτ. συνδέσεις' : >16}\n")
        for x,y in user_password_dict.items(): 
            print(f"{x : <15}{y : <56}{successful_counts.get(x,0) : >18}{failed_counts.get(x,0) : >16}")
        print("\n")


if __name__ == "__main__":
    while True:
        print("1. Εγγραφή\n2. Ενημέρωση συνθηματικού\n3. Είσοδος\n4. Λίστα χρηστών")
        choice = input("Εισάγετε την επιλογή σας(ENTER γιά τερματισμό): ")
        if choice == "":
            break
        elif choice == "1":
            new_user()
        elif choice == "2":
            update_password()
        elif choice == "3":
            login()
        elif choice == "4":
            display_users()

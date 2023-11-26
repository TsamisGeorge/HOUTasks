import sys
def dec_to_bin(num):
    lista= [] #αρχικοποίηση λίστας
    if num==0 or num==1: #περίπτωση όπου ο χρήστης βάλει 1 ή 0
        lista.append(num)
        return int(lista)
    while int(num)>0: #όλες οι υπόλοιπες περιπτώσεις
        lista.append(num % 2)
        num//=2 
    int_lista = [int(s) for s in lista]#μετατροπη στοιχείων λιστας σε ακεραίους
    return int_lista[::-1] #γυρνάει την λίστα στην σωστή φορά


def bin_to_dec(num):
    num_str=str(num)[::-1] #μετατροπη του num σε string και αντίστροφο
    sum=0
    for i in range(len(num_str)):
        sum+=int(num_str[i])*2**i #υπολογισμός κάθε αριθμού με την αντίστοιχη δύναμη του 2
    return int(sum)


def twos_comp(num):#μετατροπη του num σε λίστα απο string και αντίστροφο
    lista=list(str(num)[::-1])
    for index,element in enumerate(lista):
        if int(element)==1: #μόλις βρεί το πρώτο 1 στην αντίστροφη λίστα
            first_1=index   #κραταει την θέση του και φευγει απο αυτο το Loop
            break
    for i in range(first_1+1,len(lista)):#ξεκινάει από το πρώτο 1 και αντιστρέφει όλα τα ψηφία
        if lista[i]=='1':
            lista[i]='0'
        else :
            lista[i]='1'
        int_lista = [int(s) for s in lista]#μετατροπή στοιχείων της λίστας σε ακεραίους
    return int_lista[::-1]#γυρνάει την λίστα στην σωστή φορά
        

# ΜΕΝΟΥ
if __name__ == "__main__":
    while True:
        print("\nΕπιλογές\n{}".format(8*"="))
        print("1. Μετατροπή δεκαδικού αριθμού στο δυαδικό σύστημα.\n2. Μετατροπή δυαδικού αριθμού στο δεκαδικό σύστημα.\n3. Εύρεση συμπληρώματος δυαδικού αριθμού.\n")
        choice = input("Εισάγετε την επιλογή σας(ENTER για έξοδο): ")
        if choice == "": 
            print("\nΤέλος προγράμματος.")
            break
        try:
            #σηκώνει value error αν η επιλογή είναι <0 ή >3
            if int(choice) <= 0 or int(choice) > 3: 
                raise ValueError("\nΠαρακαλώ εισάγετε μία απο τις επιλογές.")
            int(choice,10)#σηκώνει error αν ο αριθμός δεν είναι ακέραιος με base 10
            if choice == "1":
                print("\nΔιαλέξατε να κάνετε μετατροπή ενός δεκαδικού στο διαδυκό.\n")
                while True:
                    dec = input("Εισάγετε τον δεκαδικό αριθμό(ENTER για έξοδο, '/' για αλλαγή επιλογής.): ")
                    if dec == "":
                        sys.exit()#κλείνει το πρόγραμμα
                    elif dec == "/":
                        print("\nΠοιά επιλογή επιθυμείτε;")
                        break 
                    try:
                        #συνθήκες γιά να δωθεί σωστό input
                        if int(dec,10)<0:
                            raise ValueError
                        int(dec,10)
                        #αφού περάσει τις συνθήκες καλεί την συνάρτηση
                        print("\nΟ δεκαδικός αριθμός {} σε δυαδική μορφή: ".format(dec),end="")
                        declist=dec_to_bin(int(dec))
                        for element in declist:
                            print(element,end="")
                        print("\n")
                        break
                    except ValueError: #αν δεν περάσει τις συνθήκες τυπώνει errors
                        print("\nΛάθος καταχώρηση.\nΠαρακαλώ εισάγετε έναν εγκυρο θετικό ακέραιο δεκαδικό αριθμό.\n")
            elif choice == "2":
                print("\nΔιαλέξατε να κάνετε μετατροπή ενός δυαδικού στο δεκαδικό.\n")
                while True:
                    bi = input("Εισάγετε τον δυαδικό αριθμό(ENTER για έξοδο, '/' για αλλαγή επιλογής.): ")
                    if bi == "":
                        print("\nΤέλος προγράμματος.")
                        sys.exit()
                    elif bi == "/":
                        print("\nΠοιά επιλογή επιθυμείτε;")
                        break
                    try:
                        if int(bi,2)<0:
                            raise ValueError
                        int(bi,2)
                        print("\nΟ δυαδικός αριθμός {} σε δεκαδικη μορφή ειναι: {}".format(bi,bin_to_dec(bi)))
                        break
                    except ValueError:
                        print("\nΛάθος καταχώρηση.\nΠαρακαλώ εισάγετε έναν εγκυρο ακέραιο δυαδικό αριθμό.\n")
            elif choice == "3":
                print("\nΔιαλέξατε την εύρεση συμπληρώματος δυαδικού αριθμού.\n")
                while True:
                    bi = input("Εισάγετε τον δυαδικό αριθμό(ENTER για έξοδο, '/' για αλλαγή επιλογής.): ")
                    if bi == "":
                        print("\nΤέλος προγράμματος.")
                        sys.exit()
                    elif bi == "/":
                        print("\nΠοιά επιλογή επιθυμείτε;")
                        break
                    try:
                        if int(bi,2)<0:
                            raise ValueError
                        int(bi,2)
                        bilist=twos_comp(bi)
                        print("\nΤο συμπλήρωμα του {} είναι: ".format(bi),end="")
                        for element in bilist:
                            print(element,end="")
                        print("\n")
                        break
                    except ValueError:
                        print("\nΛάθος καταχώρηση.\nΠαρακαλώ εισάγετε έναν εγκυρο ακέραιο δυαδικό αριθμό.\n")
        except ValueError as e: 
            if str(e) == "\nΠαρακαλώ εισάγετε μία απο τις επιλογές.":
                print(e)#αν έχει πέσει σε συνθήκη τυπώνει το περιεχομενό της
            else:
                print("\nΛάθος καταχώρηση.\nΕισάγετε έγκυρη επιλογή.")


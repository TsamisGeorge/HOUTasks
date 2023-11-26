# Όνομα, Επώνυμο, Φύλο, Ημερομηνία Γέννησης, Πτυχίο, Μετακίνηση, Νυχτερινή-Εργασία, Εργασιακό Καθεστώς
personnel = """Πίκος, Απίκος, m, 1983/01/01, y, y, n, Active
Μανόλης, Μανάβης, m, 1985/01/01, n, n, y, Active
Μάγια, Μέλισσα, f, 1975/04/01, y, y, y, Active
Ρόζα, Ροζαλία, f, 1980/12/31, y, n, y, Pending
Νταίζη, Ντακ, f, 1940/06/07, n, y, y, Archived
Μπίλμπο, Μπάγκινς, m, 1937/03/03, n, y, n, Archived
Μιχάλης, Καραμάνος, m, 1938/01/01, y, y, y, Archived
Έλενορ, Ρίγκμπι, f, 1966/08/04, n, n, n, Active"""

# βοηθητική συνάρτηση που εκτυπώνει τα στοιχεία ενός συνόλου
def print_set(set_to_be_printed):
    #τροποποιηση της συγκεκριμενης συναρτησης ωστε να τυπωνει τα συνολα
    #με βαση τον τροπο που ειναι φτιαγμενα
    counter = 0
    for elem in set_to_be_printed:
        if counter == len(set_to_be_printed)-1:
            print(elem[0]+elem[1])
        else:
            print(elem[0]+elem[1], end = ", ")
            counter+=1


# δημιουργία των συνόλων με βάση τα στοιχεία της συμβολοσειράς personnel
def create_sets():
    #δημιουργία των κενών συνόλων
    female = set()
    graduate = set()
    night_shift = set()
    mobile = set()
    active_staff = set()

    #διαχωρισμός του personnel ανα γραμμή
    lines = personnel.split("\n")

    #διαχωρισμός του lines σε πεδία ανά ","
    for line in lines:
        pedia = line.split(",")
        #εισαγωγή των στοιχείων κάθε πεδίου σε αντίστοιχη μεταβλητή
        name,surname,gender,DOB,degree,mobility,night_shift_ability,status = pedia
        
        #δημιουργία των συνόλών βάση των μεταβλητών με τα πεδία
        if gender == " f":
            female.add(tuple(pedia))
        if degree == " y":
            graduate.add(tuple(pedia))
        if night_shift_ability == " y":
            night_shift.add(tuple(pedia))
        if mobility == " y":
            mobile.add(tuple(pedia))
        if status == " Active":
            active_staff.add(tuple(pedia))
    
    return female,graduate,night_shift,mobile,active_staff

# επιστροφή υποσυνόλου μελών προσωπικού με ημερομηνία γέννησης από minDOB και μετά
def age_greater_or_equal(minDOB):
    minDOB = minDOB.split("/")
    dob_list = []
    lines = personnel.split("\n")
    for i in range (len(minDOB)):
        minDOB[i] = int(minDOB[i])
    for line in lines: #παρομοια διαχειριση με την συναρτηση create_sets()
        pedia = line.split(",")
        name,surname,gender,DOB,degree,mobility,night_shift_ability,status = pedia
        dob_list.append((name,surname,(DOB.split("/")))) #με διαφορα να βαζει στην dob_list μονο τα πεδια name,surname,και την ημερομηνία γεννησης σε μορφη λιστας χωρισμενη με το "/"
    returned_subset = set()
    for i in range(len(dob_list)):
        onoma, epitheto, hlhkia = dob_list[i] #εισαγωγη στοιχειων στις σωστες μεταβλητες
        year,month,day = map(int,hlhkia) #χρηση της map για να κανω int τα στοιχεια,και επισης να εισαγω καθε στοιχειο στην σωστη μεταβλητη
        if (year, month, day) >= tuple(map(int, minDOB)): #συγκριση των year month day με τα αντιστοιχα int στοιχεια του minDOB 
            returned_subset.add((onoma,epitheto)) #σε περίπτωση που η συγκεκριμενη ημερομηνια γεννησης ειναι μετα απο το minDOB εισαγει το ονομα και το επιθετο μεσα στην returned_subset
    return returned_subset
    

# ΑΠΑΝΤΗΣΕΙΣ ΣΤΑ ΕΡΩΤΗΜΑΤΑ

# γυναίκες που έχουν πτυχίο ή τη δυνατότητα νυχτερινής εργασίας (ή και τα δύο)
def women_graduate_night_shift():
    #χρηση των πραξεων μεταξυ συνολων για να επιστρεψουμε το επιθυμητο set
    temp = graduate.union(night_shift)
    women_graduate_OR_night_shift = female.intersection(temp)
    return women_graduate_OR_night_shift
    
# ενεργά μέλη του προσωπικού που έχουν τη δυνατότητα είτε νυχτερινής εργασίας ή μετακίνησης σε κοντινή πόλη, αλλά όχι και τα δύο
def active_night_shift_mobile():
    #χρηση των πραξεων μεταξυ συνολων για να επιστρεψουμε το επιθυμητο set
    temp = night_shift.symmetric_difference(mobile)
    active_night_shift_XOR_mobile = active_staff.intersection(temp)
    return active_night_shift_XOR_mobile


# μέλη του προσωπικού που έχουν πτυχίο αλλά δεν μπορούν να μετακινηθούν
def graduate_not_mobile():
    #χρηση των πραξεων μεταξυ συνολων για να επιστρεψουμε το επιθυμητο set
    graduate_NOT_mobile = graduate.difference(mobile)
    return graduate_NOT_mobile

# μέλη του προσωπικού που δεν είναι ενεργά
def inactive_staff():
    #χρηση των πραξεων μεταξυ συνολων για να επιστρεψουμε το επιθυμητο set
    temp = female.union(graduate,night_shift,mobile,active_staff)
    not_active_staff = temp.difference(active_staff)
    return not_active_staff


# μέλη του προσωπικού με ημερομηνία γέννησης από ημερομηνία που εισαγάγει ο χρήστης και μετά
def age_limit():
    inputDOB = input("\nΕισάγετε ημερομηνία σε μορφή ΕΕΕΕ/ΜΜ/ΗΗ: ")
    subset = age_greater_or_equal(inputDOB) #κληση και εισαγωγή τιμης της age_greater_or_equal στην μεταβλητη subset
    return subset #επιστροφη υποσυνολου που εχει DOB μετα απο minDOB

#### κυρίως πρόγραμμα ####
# εδώ αρχικοποιήστε τα σύνολα καλώντας τη συνάρτηση create_sets()
female,graduate,night_shift,mobile,active_staff = create_sets()
print("\nΠροσωπικό που είναι γυναίκες:")
print_set(female)
print("\nΠροσωπικό έχει πτυχίο:")
print_set(graduate)
print("\nΠροσωπικό που έχει δυνατότητα νυχτερινής εργασίας:")
print_set(night_shift)
print("\nΠροσωπικό που έχει δυνατότητα μετακίνησης:")
print_set(mobile)
print("\nΠροσωπικό που είναι ενεργό:")
print_set(active_staff)

print("\nΑΠΑΝΤΗΣΕΙΣ ΣΤΑ ΕΡΩΤΗΜΑΤΑ\n")
### κλήση συναρτήσεων απάντησης ερωτημάτων γ1 έως γ5
###γ1
night_shift_OR_graduate_women = women_graduate_night_shift()
print("Γυναίκες με πτυχίο ή δυνατότητα νυχτερινής εργασίας:")
print_set(night_shift_OR_graduate_women)
###γ2
night_XOR_mobile = active_night_shift_mobile()
print("\nΕνεργό προσωπικό με δυνατότητα νυχτερινής εργασίας ή μετακίνησης(όχι και τα 2):")
print_set(night_XOR_mobile)
###γ3
graduate_NOT_mobile_staff = graduate_not_mobile()
print("\nΠροσωπικό με πτυχίο αλλα όχι δυνατότητα μετακίνησης:")
print_set(graduate_NOT_mobile_staff)
###γ4
inactive_personnel = inactive_staff()
print("\nΠροσωπικό που είναι ανενεργό:")
print_set(inactive_personnel)
###γ5
personnel_equal_OR_after_minDOB = age_limit()
if not personnel_equal_OR_after_minDOB:
    print("\nΔεν υπάρχει προσωπικό μετά από την ημερομηνία που εισάγατε.")
else:
    print("\nΠροσωπικό μετά από την ημερομηνία που εισάγατε:")
    print_set(personnel_equal_OR_after_minDOB)

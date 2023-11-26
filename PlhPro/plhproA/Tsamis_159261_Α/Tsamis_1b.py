import random #Η random βιβλιοθηκη για την αυθαιρετη συμβολοσειρα
import sys #η sys βιβλιοθηκη για να κανει exit το προγραμμα
symbols = "" #το symbols ξεκιναει ως κενη συμβολοσειρα
for i in range(0,20): #θα γινουν οι απο κατω εντολες απο το 0 εως το 19 αρα 20 φορες
    possible_actions = ["Π","Ψ","Χ"] #Οι πιθανες επιλογες για την συμβολοσειρα
    computer_action = random.choice(possible_actions)
    symbols += computer_action #καθε φορα στο symbols προστιθεται το computer_action
turn = 0
while(True):
    j = (True)
    while (j):
        epilogh_xrhsth = input("Διάλεξε Π(πέτρα),Ψ(ψαλίδι) ή Χ(χαρτί),αλλιώς πάτα ENTER για τερματισμό: ")
        if(epilogh_xrhsth == "π" or "ψ" or "χ" or "Π" or "Ψ" or "Χ"): 
            j = False #φευγει απο την δευτερη while για να συνεχιστει το παιχνιδι
        if(epilogh_xrhsth == ""):
            print("\nΤέλος παιχνιδιού!")
            sys.exit() #κλεινει το προγραμμα
    if (epilogh_xrhsth.capitalize() == symbols[turn]): #symbols[turn] = επιλογη υπολογιστη στον συγκεκριμενο γυρο
        print("\nΚαι οι δύο διάλεξαν",epilogh_xrhsth.capitalize(),"\n\nΙσοπαλία!\n")
        #κανει κεφαλαιο το input του χρηστη μεσω του .capitalize,κοιταει αν
        #ειναι ιδιο με την επιλογη του υπολογιστη
    elif (epilogh_xrhsth.capitalize() == "Π"):
        if (symbols[turn] == "Ψ"):
            print("\nΔιαλεξα Ψαλιδι!\n\nΚερδισες!\n")
        else:
            print("\nΔιαλεξα Χαρτι!\n\nΕχασες!\n")
        #περιπτωσεις : πετρα νικαει ψαλιδι, χαρτι νικαει πετρα.
    elif (epilogh_xrhsth.capitalize() == "Ψ"):
        if (symbols[turn] == "Χ"):
            print("\nΔιαλεξα Χαρτι!\n\nΚερδισες!\n")
        else:
            print("\nΔιαλεξα Πετρα!\n\nΕχασες!\n")
        #περιπτωσεις : ψαλιδι νικαει χαρτι, πετρα νικαει ψαλιδι.
    elif (epilogh_xrhsth.capitalize)() == "Χ":
        if (symbols[turn] == "Π"):
            print("\nΔιαλεξα Πετρα!\n\nΚερδισες!\n")
        else:
            print("\nΔιαλεξα Ψαλιδι!\n\nΕχασες!\n")
        #περιπτωσεις : χαρτι νικαει πετρα, ψαλιδι νικαει χαρτι.
    turn += 1
    #ανεβαζει την μεταβλητη turn κατα 1 σε καθε
    #γυρο για να επιλεξει το επομενο συμβολο στην συμβολοσειρα
    if (turn == 20):
        turn = 0 #αν η μεταβλητη turn φτασει 20 τοτε παει ξανα 0 για να γινει
        #προσπελαση της συμβολοσειρας απο την αρχη
    

import sys
class Camera: # Κλάση Camera
    def __init__(self, location):
        #το καθε αντικειμενο καμερα εχει ως θεση οτι μπει σαν ορισμα στην αρχικοποιηση του
        self.location = location
        #καθε καμερα στην αρχη ειναι απενεργοποιημενη
        self.operation = False
        #καθε καμερα στην αρχη εχει 0 zoom
        self.zoom = 0
        #καθε καμερα στην αρχη εχει την νυχτερινη οραση απενεργοποιημενη
        self.night_vision = False
        


    ##μεθοδος ενεργοποιησης/απενεργοποιησης της καμερας
    def power(self, user_input):
        ##αν η καμερα ειναι ενεργοποιημενη και ο χρηστης δωσει σωστο input τοτε απενεργοποιειται
        if self.operation and "off" in user_input.lower():
            self.operation = False
        ##αν η καμερα ειναι απενεργοποιημενη και ο χρηστης δωσει σωστο Input τοτε ενεργοποιειται
        elif self.operation == False and "on" in user_input.lower():
            self.operation = True
        ##αν δωθει λάθος Input ενημερωνει αναλογα με το state του self.operation
        else:
            print(f"\nΗ κάμερα ασφαλείας είναι ήδη {'ενεργοποιημένη' if self.operation else 'απενεργοποιημένη'}.")

    ##μεθοδος για αυξηση του zoom της καμερας
    def zoomUp(self):
        #αν το zoom δεν ειναι 10 και η καμερα ειναι ενεργοποιημενη τοτε αυξανει το zoom κατα 1
        if self.zoom != 10 and self.operation:
            self.zoom += 1
        #σε οποιαδηποτε αλλη περιπτωση ενημερώνει αναλόγως
        elif self.operation == False:
             print("\nΗ κάμερα είναι απενεργοποιημένη.")
        else:
            print("\nΤο zoom δεν μπορεί να αυξηθεί παραπάνω.")
            
    ##Μεθοδος μείωσης του zoom της καμερας
    def zoomDown(self):
        #αν το zoom δεν ειναι 0 και η καμερα ειναι ενεργοποιημενη τοτε μειωνει το zoom κατα 1
        if self.zoom != 0 and self.operation:
            self.zoom -= 1
        #σε οποιαδηποτε αλλη περιπτωση ενημερωνει αναλογως
        elif self.operation == False:
            print("\nΗ κάμερα είναι απενεργοποιημένη.")
        else:
            print("\nΤο zoom δεν μπορεί να μειωθεί παραπάνω.")

    #μέθοδος που ενεργοποιεί ή απενεργοποιεί τη λειτουργία νυχτερινής όρασης της καμερας
    def nightVision(self, user_input):
        ##αν το night vision και η καμερα ειναι ενεργοποιημενα, και ο χρηστης δωσει σωστο Input, τοτε απενεργοποιηται το night vision
        if self.night_vision and self.power and "no" in user_input.lower():
            self.night_vision = False
        ##αν το night vision ειναι απενεργοποιημενο, η καμερα ενεργοποιημενη, και ο χρηστης δωσει σωστο input, τοτε ενεργοποιηται το night vision
        elif not self.night_vision and self.operation and "yes" in user_input.lower():
            self.night_vision = True
        ##αν η καμερα ειναι απενεργοποιημενη ενημερωνει αναλογως
        elif self.operation == False:
            print("\nΗ κάμερα είναι απενεργοποιημένη.")
        else: ## αν δωσει λαθος input ενημερωνει αναλογα με το state του self.night_vision
            print(f"\nΗ επιλογή νυχτερινής όρασης είναι ήδη {'ενεργοποιημένη' if self.night_vision else 'απενεργοποιημένη'}")

    def __str__(self):  #Μέθοδος αποτύπωσης των συγκεντρωτικών πληροφοριών για όλες τις λειτουργίες της Camera
        out = f'Στοιχεία Κάμερας:\n\tΤοποθεσία: {self.location}\n'
        out += f"\tΚατάσταση κάμερας: {'σε λειτουργία' if self.operation else 'απενεργοποιημένη'}\n"
        if self.operation:
            out += f"\tzoom: {self.zoom}\n"
            out += f"{'(νυχτερινή όραση)' if self.night_vision else ''}\n"
        return out


class Panel(): # Κλάση πίνακα ελέγχου
    def __init__(self):
        #δημιουργία λίστας αντικειμένων τυπου Camera()
        self.list_of_cameras = [Camera("Ταμείο"),Camera("Είσοδος"),Camera("Αποθήκη")]
        #self.camera είναι η καμερα στην οποια γινεται η διαχειριση, αρχικοποιηση με None
        self.camera = None

    ##Μέθοδος επιλογης σε ποια καμερα θα γινει διαχειριση
    def select_camera(self):
        while True:
            print("\nΟι κάμερες ασφαλείας είναι:\n")
            ##Τύπωμα του attribute 'location' καθε καμερας
            for i in range(len(self.list_of_cameras)):
                print(f"{i+1}. {self.list_of_cameras[i].location}")
            choice = input("Επιλέξτε κάμερα, <enter> για έξοδο: ")
            #αν το Input ειναι Enter κλεινει το προγραμμα
            if not choice:
                break
            
            #η επιλογη που δοθηκε αντιστοιχει στην choice - 1 θεση της λιστας
            self.camera = self.list_of_cameras[int(choice)-1]
            
            #κληση της μεθόδου control_panel() μεσα απο τη μεθοδο select_camera()
            self.control_panel()
            
    # Mέθοδος για έλεγχο της επιλεγμένης Camera (power, zoom, night_vision)
    def control_panel(self): 
        while True:
            print(f"\nΠανελ ελέγχου κάμερας {self.camera.location}")
            print(self.camera)
            sel = input('o(on/off), (z)oom (+/-), (n)(yes/no), <enter>: exit:').strip()
            if not sel: break
            if sel[0].lower() == "z":
                if sel[-1] == "+": self.camera.zoomUp()
                if sel[-1] == "-": self.camera.zoomDown()
            elif sel[0].lower() == "n":
                self.camera.nightVision(sel)
            elif sel[0].lower() == "o":
                self.camera.power(sel) 


#δημιουργια ενος αντικειμενου τυπου Panel() και μετα κλήση της μεθοδου select.camera() μεσω του αντικειμένου Panel()
p1 = Panel()
p1.select_camera()

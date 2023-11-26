class Component:
    def __init__(self,name):
        #το όνομα που δέχεται σαν όρισμα καταχωρείτε στο self.name του κάθε
        #Component() αντικειμένου
        self.name = name

        #το state αρχικοποιείται σε False γιατι στην αρχη τα Component()
        #αντικειμενα ειναι κλειστα
        self.state = False

        #λίστα συνδεδεμένων αντικειμένων που έχει κάθε Component(),η λίστα κάθε
        #Component() είναι μοναδικη καθηστώντας την σύνδεση των αντικειμένων μονόδρομη
        self.connected = []

    #Μέθοδος για την σύνδεση των αντικειμένων
    def connect(self, other):
        #βάζουμε στην λιστα του self αντικειμένου Component(), το other αντικείμενο Component() που μπαίνει ως όρισμα
        self.connected.append(other)

    #Μέθοδος ενεργοποίησης εξαρτήματος
    def start(self):
        #το attribute 'state' του εκάστοτε αντικειμένου γίνεται True, ενεργοποιώντας το εξάρτημα
        self.state = True
        #Τύπωμα οτι το εκάστοτε εξάρτημα ενεργοποιήθηκε
        print(f"Εξάρτημα {self.name}: έναρξη λειτουργίας")
        #Ενεργοποίηση κάθε αντικειμένου που είναι σε σύνδεση με το self αντικείμενο
        for component in self.connected:
            component.start()
            

    #Μέθοδος απενεργοποίησης εξαρτήματος
    def stop(self):
        #αν το εξάρτημα είναι ενεργοποιημένο
        if self.state:
            #Πριν απενεργοποιηθεί το παρόν εξάρτημα, παει στο τελευταίο συνδεδεμένο εξάρτημα και απενεργοποιεί αυτό πρώτα
            #και μετα αναδρομικά απενεργοποιεί και τα υπόλοιπα μέχρι να απενεργοποιηθεί το αντικείμενο που καλεί την .stop 
            for component in self.connected:
                component.stop()
            self.state = False
            print(f"Εξάρτημα {self.name}: παύση λειτουργίας")
        
            
            

    def status(self):
        # Εκτύπωση συνδεδεμένων εξαρτημάτων και κατάστασης εξαρτήματος 
        print(f"Κατάσταση: {self.name} {'σε λειτουργία' if self.state else 'εκτός λειτουργίας'}")
        for component in self.connected:
            component.status()

###Κλάσεις για κάθε εξάρτημα, οι οποίες κληρονομούν χαρακτηριστηκά και μεθόδους της Component() κλάσης
            
class Ignition(Component):
    #Κλήση του αρχικοποιητή της Ignition
    def __init__(self):
        #Κλήση του αρχικοποιητή της Parent κλάσης η οποία είναι η Component(),κάθε φορά που δημιουργείται ένα αντικείμενο τύπου
        #Ignition(), περνάει σαν όρισμα το όνομα 'Μίζα' στο attribute 'name' της Component()
        super().__init__("Μίζα")
        
class Battery(Component):
    def __init__(self):
        super().__init__("Μπαταρία")
        
class FuelPump(Component):
    def __init__(self):
        super().__init__("Αντλία καυσίμου")
        
class Engine(Component):
    def __init__(self):
        super().__init__("Κινητήρας")
        
class Car:
    def __init__(self):
        # Δημιουργία των εξαρτημάτων του αυτοκινήτου
        self.ignition = Ignition()
        self.battery = Battery()
        self.fuelPump = FuelPump()
        self.engine = Engine()

        # Σύνδεση των εξαρτημάτων μεταξύ τους
        self.ignition.connect(self.battery)

        self.battery.connect(self.fuelPump)
        self.battery.connect(self.engine)
        

    def status(self):
        print('=========================')
        self.ignition.status()
        print('=========================')

if __name__=="__main__":
    car = Car()
    car.status()
    car.ignition.start()
    car.status()
    car.ignition.stop()
    car.status()


    ##ενδεικτική εκτύπωση των συνδέσεων
    
    #συνδέσεις μίζας:
    #print("Συνδέσεις μίζας: "+str(car.ignition.connected[0].name))

    #συνδέσεις μπαταρίας
    #print("\nΣυνδέσεις μπαταρίας: "+str(car.battery.connected[0].name)+", "+str(car.battery.connected[1].name))

import turtle as tr


class Pen(tr.Turtle):
    #κλαση πέννα
    def __init__(self):
        #καλουμε τον αρχικοποιητη της Turtle κλασης, και οριζουμε το object να εχει
        #την μορφή χελώνας
        tr.Turtle.__init__(self, "turtle")
        #οριζουμε την ταχυτητα που ακολουθεί η χελώνα το ποντίκι να είναι στο μέγιστο
        self.speed("fastest")
        #κανουμε κληση της draw καθε φορα που κουνιέται ένα αντικείμενο τύπου Pen()
        self.ondrag(self.draw)
        #αρχικοποίηση κενής λίστας για να μπουν οι ιχνηλάτες
        self.traces = []
        
        #####ΑΠΑΝΤΗΣΗ ΣΕ ΕΡΩΤΗΣΗ Α:
        #self.traces.append(Tracer(1,-1,1,1,1,'red'))
        
        #####ΕΠΟΜΕΝΑ TRACE:
        #trace συμμετριας προς τον y αξονα:
        self.traces.append(Tracer(-1,1,1,1,1,'blue'))
        
        #trace συμμετριας ως προς τον x και y αξονα:
        self.traces.append(Tracer(-1,-1,1,1,1,'yellow'))
        
        #trace συμμετρίας ως προς τον x αξονα:
        self.traces.append(Tracer(1,-1,1,1,1,'purple'))

        ##traces με διαφορετικα attributes
        self.traces.append(Tracer(1,1,15,15,10,'green'))
        self.traces.append(Tracer(-1,1,-15,-15,10,'magenta'))
        
        

    #μέθοδος για να ζωγραφίζει το object της Pen() οπως και οι ιχνηλάτες 
    def draw(self, x,y):
        #καλουμε την ondrag με None σαν ορισμα ωστε στιγμιαια μέχρι να κάνει τις
        #επομενες κινήσεις να μην δεχεται input απο την κινηση του Pen() object
        self.ondrag(None)
        
        self.goto(x,y)#κίνηση του Pen() object στις  x,y συντεταγμένες της οθόνης 

        ##κώδικας για κίνηση των trace που εχουν υλοποιηθει
        for trace in self.traces:
            #κλήση της moveto μεθοδου για το καθε trace μεσα στην λιστα με τα
            #trace 'self.traces'
            trace.moveto(x,y)

        #κληση της ondrag με ορισμα την self.draw για να συνεχισει να δεχεται
        #input καθε φορα που ο χρηστης κουναει το Pen() object 
        self.ondrag(self.draw)
        
class Tracer(tr.Turtle):
    #κλάση ιχνηλάτης

    #κλήση του αρχικοποιητη της Tracer
    def __init__(self, dx, dy, a=0, b=0, width=1, color='red'):
        #Κλήση του αρχικοποιητη της Turtle ωστε τα αντικειμενα τυπου tracer να
        #εχουν τις μεθόδους της Turtle κλάσης του turtle module
        tr.Turtle.__init__(self)
        
        #χρηση μεθόδου της Turtle για να κρύψουμε τα Tracer() objects ωστε
        #να φαινεται μονο το tracing που κανουν
        self.hideturtle()

        #Κλήση μεθόδων .color Και .width για εισαγωγή χρώματος και πλάτους των Trace
        self.color(color)
        self.width(width)

        #εκχώρηση του a,b,dx,dy που παιρνουμε σαν ορισμα στις instance μεταβλητές
        #self.a, self.b, self.dx, self.dy
        self.a = a
        self.b = b
        self.dx = dx
        self.dy = dy
        
    def moveto(self, x,y):
        #στο attribute screen της κλασης Turtle, χρησιμοποιούμε την μέθοδο .tracer
        #της κλάσης Screen() του module turtle,παιρνάμε False σαν παραμετρο
        #για να σβήσουμε το animation
        #της κίνησης των αντικειμένων Pen() και Tracer() προσωρηνά
        #ώστε να μην χρειάζεται να κανει συνεχώς refresh την οθόνη καθε φορά
        #που γινεται μια κίνηση, με αυτον τον τροπο αποφεύουμε το lag που
        #υπάρχει όταν υπάρχουν αρκετά Objects Pen() η Tracer()
        self.screen.tracer(False)

        #Κλήση της goto στο αντικείμενο Tracer(), ωστε να παει το αντικείμενο
        #στο επιθυμητό σημείο με βάση την κίνηση που εγινε απο το Pen()
        #αντικείμενο και τα attributes του Tracer() αντικειμενου
        self.goto(x * self.dx + self.a, y * self.dy + self.b)

        #επανέναρξη του animation της κίνησης των object αφού "τελειώσει"
        #η κίνηση τους
        self.screen.tracer(True)

#δημιουργία ενός Pen() αντικειμένου
p = Pen()

#χρήση της mainloop μεθοδου του turtle module για "έναρξη" του προγραμματος και
#εκκίνηση του παραθύρου
tr.mainloop()

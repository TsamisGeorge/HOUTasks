import sys
while (True):
    print("ENTER για έξοδο.\n")
    diastash = input("Παρακαλώ δώστε την διάσταση που θα κινείται το ρομπότ: ")
    if (diastash.isdigit() and int(diastash) > 0): #συνθηκη για αν η μεταβλητη
        #diastash ειναι ακεραιος αριθμος μεγαλυτερος του 0
        print ("\nΤο ρομπότ θα κινείται σε διάσταση",diastash,"x",diastash,".\nΚαι σε άξονα x,y .\nΠάνω και κάτω αλλάζει το x, δεξιά και αριστερά αλλάζει το y .\n")
        break #φευγει απο αυτη την while και συνεχιζει το προγραμμα
    elif (diastash == ""):
        sys.exit() #αν πατησει απλα ENTER κλεινει το προγραμμα
    else: #αν βαλει οτιδηποτε αλλο που δεν ειναι αποδεκτο σαν απαντηση
        print("\nΣφάλμα, λάθος καταχώρηση.\n")
x = 0
y = 0 #x και y ειναι οι δυο διαστασεις
j =(True)
while (j):
    kinhsh = input("Παρακαλώ δώστε κίνηση (r,l,u,d) και βήματα, πχ r4 για 4 βήματα δεξιά: ")
    if (kinhsh == ""):
        sys.exit() #αν πατησει απλα ENTER κλεινει το προγραμμα
    elif (not kinhsh[1:].isdigit()): #αν απο 1 εως το τελος της μεταβλητης
        #δεν ειναι αριθμος τοτε ειναι λαθος καταχωρηση
        print ("\nΣφάλμα, λάθος καταχώρηση.\n")
    elif (kinhsh[0] == "r" and int(kinhsh[1:]) + y <= int(diastash) - 1):
        print("\n(x:",x,")\n(y:",int(kinhsh[1:]) + y,")\n")
        y += int(kinhsh[1:]) #ολη η συνθηκη για την δεξια κινηση,χωρις να
        #φευγει απο τα ορια και αποθηκευοντας στο y την κινηση που εκανε
    elif (kinhsh[0] == "l" and y - int(kinhsh[1:]) >= 0):
        print("\n(x:",x,")\n(y:",y - int(kinhsh[1:]),")\n")
        y -= int(kinhsh[1:]) #ολη η συνθηκη για την αριστερη κινηση,χωρις να
        #φευγει απο τα ορια και αποθηκευοντας στο y την κινηση που εκανε
    elif (kinhsh[0] == "u" and x - int(kinhsh[1:]) >= 0):
        print("\n(x:",x - int(kinhsh[1:]),")\n(y:",y,")\n")
        x -= int(kinhsh[1:])#ολη η συνθηκη για την αριστερη κινηση,χωρις να
        #φευγει απο τα ορια και αποθηκευοντας στο x την κινηση που εκανε
    elif (kinhsh[0] == "d" and int(kinhsh[1:]) + x <= int(diastash) - 1):
        print("\n(x:",int(kinhsh[1:]) + x,")\n(y:",y,")\n")
        x += int(kinhsh[1:])#ολη η συνθηκη για την αριστερη κινηση,χωρις να
        #φευγει απο τα ορια και αποθηκευοντας στο y την κινηση που εκανε
    else:
        if (kinhsh[0] == "r" or kinhsh[0] == "l" or kinhsh[0] == "u" or kinhsh[0] == "d"):
            print ("\nΣφάλμα, κίνηση εκτός ορίων.\n")
        else:
            print("\nΣφάλμα, λάθος καταχώρηση.\n")
            #συνθηκες για αμυντικο προγραμματισμο για να αποφευχθουν τα
            #runtime error
        
    

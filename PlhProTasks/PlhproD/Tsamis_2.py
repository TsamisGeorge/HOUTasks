# Εισαγωγή χρήσιμων αρθρωμάτων (modules) της python #
#####################################################
import pandas as pd
import matplotlib.pyplot as plt
import time
import datetime
from datetime import date

'''Εισαγωγή χρονικής περιόδου για την οποία θα φορτωθούν τα δεδομένα. Επιστρέφει πλειάδα από δύο ημερομηνίες, της μορφής (τελική, αρχική).'''
def ts_timeperiod():
    # Υποερώτημα 1
    t = True
    while t:
        #Input για την τελευταια ημέρα
        while True:
            try:
                last_date = input("Εισάγετε την τελευταία ημέρα της χρονικής περιόδου για την οποία θα φορτωθούν τα δεδομένα (format dd/mm/yyyy): ")
                #μετατροπη του last_date που δόθηκε σαν συμβολοσειρα στο last_date, σε 3 μεταβλητές δεδομένου integer, με χρήση
                #της συνάρτησης map, με όρισμα το int, για να το εφαρμόσει και στα τρία στοιχεία της λίστας last_date.split("/")
                day, month, year = map(int, last_date.split("/"))
                #μετατροπή των μεταβλητών σε datetime().date() αντικείμενου δίνωντας σαν όρισμα τις τρείς μεταβλητές που υπολογίστηκαν πάνω
                #σε περίπτωση αποτυχίας της συγκεκριμένης μετατροπής για οποιονδήποτε λόγο βγάζει μύνημα λάθους καταχώρησης
                end_date = datetime.datetime(year, month, day).date()
                print(f"Τελευταία ημέρα της χρονικής περιόδου: {end_date}")
                break
            except ValueError:
                print("\nΛάθος καταχώρηση\n")
        #input για την πρώτη ημέρα
        while True:
            try:
                first_date = input("Εισάγετε την πρώτη ημέρα της χρονικής περιόδου για την οποία θα φορτωθούν τα δεδομένα (format dd/mm/yyyy): ")
                day, month, year = map(int, first_date.split("/"))
                start_date = datetime.datetime(year,month,day).date()

                #αν η πρώτη ημέρα είναι μεταγενέστερη της τελευταίας, σηκώνουμε ValueError, και τυπώνεται το αντίστοιχο error
                #αν δεν ισχύει αυτή η συνθήκη αλλά έχουμε οποιοδήποτε άλλο error τότε δεν τυπώνεται το παρόν
                if start_date > start_date:
                    raise ValueError("Η πρώτη ημέρα της χρονικής περιόδου δεν μπορεί να είναι μετά την τελευταία ημέρα της χρονικής περιόδου.\n")
                
                print(f"Πρώτη ημέρα της χρονικής περιόδου: {start_date}")

                #εφόσον πάνε όλα καλά θέτεται το t να είναι False ώστε να κλείσει ο ατέρμων βρόγχος και να συνεχίσει στην επιστροφή των τιμών
                #το πρόγραμμα
                t = False
                break

            except ValueError as e:
                print("\nΛάθος καταχώρηση\n")
                if str(e) == "Η πρώτη ημέρα της χρονικής περιόδου δεν μπορεί να είναι μετά την τελευταία ημέρα της χρονικής περιόδου.\n":
                    print(e)

    return (end_date, start_date)
            
'''Στατιστικά μέτρα τιμών μετοχής'''
def ts_statistics(df):
    print("\nΣτατιστικά μέτρα τιμών μετοχής")
    stat=True
    while stat:
        # Επιλογή χρονοσειράς/στήλης
        df_col=select_ts(df)

        # Υποερώτημα 2:
        # χρήση fstring με float formatting ώστε να τυπωθεί το επιθυμητό αποτέλεσμα, χρήση των συναρτήσεων που έχουν τα dataframe
        # αντικείμενα όπως .min, .max, .std κλπ. 
        print(f"Min = {df[f'{df_col}'].min():.4f}")
        print(f"Max = {df[f'{df_col}'].max():.4f}")
        print(f"Mean = {df[f'{df_col}'].mean():.4f}")
        print(f"Standard Deviation = {df[f'{df_col}'].std():.4f}")
        print(f"Variance = {df[f'{df_col}'].std() ** 2:.4f}")
        # Ερώτημα για συνέχιση
        stat = confirm_continuation("Θέλετε να υπολογίσετε Στατιστικά Μέτρα και για άλλη Τιμή (Στήλη)?")

'''Γραφική παράσταση τιμών μετοχής'''
def ts_plot(df):
    print("\nΓραφική παράσταση τιμών μετοχής")
    plt_flag=True
    while plt_flag:
        # Επιλογή στήλης
        df_col=select_ts(df)
        # Υποερώτημα 3
        # Χρήση της συνάρτησης .plot με όρισμα στον x άξονα το df.index που στην συγκεκριμένη περίπτωση είναι η πρώτη στήλη
        # του dataframe αντικειμένου η οποία είναι οι ημερομηνίες, και όρισμα στον y άξονα το df[df_col] που επιλέχθηκε απο
        # τον χρήστη το οποίο είναι η εκάστοτε στήλη, πχ Low κλπ
        plt.plot(df.index, df[df_col])
        #x και y labels για τα ονόματα στον x και y άξονα, οπως και τίτλος της γραφικής αναπαράστασης
        plt.xlabel('Dates') 
        plt.ylabel(f"{df_col} values")
        plt.title("Graphical Representation")
        plt.show()
        # Ερώτημα για συνέχιση
        plt_flag = confirm_continuation("Θέλετε να σχεδιάσετε και άλλη Τιμή (Στήλη)?")


# Βοηθητικές συναρτήσεις για εισόδους επιλογών - δίνονται έτοιμες
def select_ticker():
    '''Επιλογή μετοχής'''
    print("Επιλογή εταιρικής μετοχής")
    ticker_list = ["MMM","ADBE","AAPL","AMZN","AMD","AMAT","T","CAT","HPE","IBM","MSFT"] #λίστα με τα ticker (συντομογραφίες ονομάτων μετοχών) εταιριών του Χρημ. της Νέας Υόρκης
    print("Tickers εταιριών:", *ticker_list, sep=', ')
    ticker = input("Εισάγετε ένα από τα παραπάνω ticker μετοχής: ").upper()
    while ticker not in ticker_list:
        ticker = input("Λάθος Ticker. Εισάγετε ένα από τα παραπάνω: ").upper()
    return ticker

def select_ts(df):
    '''Επιλογή χρονοσειράς/στήλης από dataframe'''
    col_list = list(df.columns)
    print("Xρονοσειρές της μετοχής (στήλες δεδομένων)", *col_list[1:], sep=', ')
    df_col = input("Εισάγετε χρονοσειρά (στήλη δεδομένων) από τις παραπάνω): ").capitalize()
    while df_col not in col_list:
        df_col = input("Λάθος χρονοσειρά/στήλη! Εισάγετε μία από τις παραπάνω: ").capitalize()
    return df_col

def confirm_continuation(msg):
    '''Λήψη απάντησης για συνέχιση ή όχι'''
    cont = input(msg+"(Y/N): ")
    while cont not in ["Y","y","N","n"]:
        cont = input("Εισάγετε (Y)es ή (N)o: ")
    return True if cont.upper() == "Y" else False


# Κυρίως πρόγραμμα
if __name__=="__main__":
    # Επιλογή μετοχής (ticker)
    ticker = select_ticker()
    # Εισαγωγή/μετατροπή ημερομηνιών έναρξης/λήξης για τα δεδομένα μετοχής   
    end_date, start_date = ts_timeperiod()
    period1 = int(time.mktime(start_date.timetuple()))
    period2 = int(time.mktime(end_date.timetuple()))
    # Φόρτωση χρονοσειρών μετοχής από το yahoo finance
    interval = '1d' # 1d (one Day). Θα μπορούσαμε να χρησιμοποιήσουμε και 1m (one Month)
    query_string = f'https://query1.finance.yahoo.com/v7/finance/download/{ticker}?period1={period1}&period2={period2}&interval={interval}&events=history&includeAdjustedClose=true'
    stock = pd.read_csv(query_string) # φορτώνει την χρονοσειρά των τιμών των μετοχών σαν data frame
    # Αποθήκευση των τιμών της μετοχής, τοπικά, σε αρχείο τύπου csv
    stock.to_csv(f"{ticker}.csv")
    # Εμφάνιση στατιστικών
    ts_statistics(stock)
    # Εμφάνιση γραφικών παραστάσεων
    ts_plot(stock)

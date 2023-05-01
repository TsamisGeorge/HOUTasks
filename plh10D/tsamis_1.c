#include <stdio.h>
#define N 4
#define True 1
#define False 0


//Προτώτυπα συναρτήσεων που θα χρειαστουμε για την διεξαγωγή των υπολογισμών.
int elem_exists(int elem, int (*arr)[N]);
void init_2d_array(int (*arr)[N]);
void init_1d_array(int *arr);
void print_lines(int (*arr)[N]);
void copy_array(int (*source)[N], int (*dest)[N]);
void calc_transpose(int (*transpose)[N]);
int diagonal_sum(int (*arr)[N]);
int max_absolute_diff(int *arr, int primes);


int main(void)
{
	
	system("chcp 1253 > nul");
	//όσες δηλώσεις και αρχικοποιήσεις των πινάκων χρειαζόμαστε
	int num, i = 0, j = 0;
	
	int pinakas[N][N];
	int transpose_pin[N][N];
	
	int prime[N*N];
	
	init_2d_array(pinakas);
	init_2d_array(transpose_pin);
	init_1d_array(prime);
	
	printf("Εισάγετε μοναδικούς ακεραίους θετικούς αριθμούς.\n");
	for(i=0;i<N;i++)
	{
		for(j=0;j<N;j++)
		{
			//χρήση εμφωλευμένου for βρόχου μαζι με αμυντικό προγραμματισμο ως προς την τιμή αλλά και τον τύπο της μεταβλητής
			printf("Θέση %d, %d: ",i+1,j+1);
			while(scanf("%d", &num) != 1 || elem_exists(num, pinakas) || num < 1)
			{
				printf("\nΛάθος καταχώρηση\nΕισάγετε έναν μοναδικό θετικό ακέραιο αριθμό.\nΘέση %d, %d: ", i+1, j+1);
				//διάβασμα των χαρακτήρων μέχρι να πετύχουμε ένα newline χαρακτήρα, διαφορετικός τρόπος πέραν απο την fflush(stdin)
				while (getchar() != '\n');	
			}
			//Αν περάσει το input απο τον αμυντικο προγραμματισμο σημαινει ότι έχουμε μια έγκυρη καταχώρηση οπότε το αποθηκεύουμε στο pinakas[i][j]
			pinakas[i][j] = num;
		}
	}
	//τύπωμα του πρώτου πίνακα
	printf("\nΟ πίνακας είναι ο παρακάτω.\n");
	print_lines(pinakas);
	
	//αντιγραφή του πίνακα στον transpose_pin και μετα χρήση της calc_transpose ωστε να μετατραπεί σε ανάστροφο
	copy_array(pinakas, transpose_pin);
	calc_transpose(transpose_pin);
	
	//τύπωμα του αναστρόφου
	printf("\nΟ ανάστροφος πίνακας είναι ο παρακατω.\n");
	print_lines(transpose_pin);
	
	//τύπωμα των αρθροισμάτων με το τελικό συμπέρασμα για τα στοιχεία στην κύρια διαγώνιο και των 2 πινάκων
	printf("\nΤο άρθροισμα των στοιχείων της κύριας διαγωνίου του πίνακα είναι %d\n",diagonal_sum(pinakas));
	printf("\nΤο άρθροισμα των στοιχείων της κύριας διαγωνίου του ανάστροφου είναι %d\n",diagonal_sum(transpose_pin));
	printf("\nΤο άρθροισμα των στοιχείων της κύριας διαγωνίου των πινάκων είναι ίσο.\n\n");
	
	//μεταβλητή μετρητής των πρώτων αριθμών
	int primes_found = 0;
	for(i=0;i<N;i++)
	{
		for(j=0;j<N;j++)
		{
			//βλεπουμε για κάθε στοιχείο μέσα στον pinakas πόσοι αριθμοί είναι πρώτοι με χρήση της is_prime σε κάθε στοιχείο
			if(is_prime(pinakas[i][j]))
			{
				prime[primes_found] = pinakas[i][j];
				primes_found++;
			}
		}
	}
	
	//αν έχουν βρεθεί πρώτοι αριθμοί
	if(primes_found)
	{
		//τύπωμα των πρώτων αριθμών του πίνακα prime
		printf("Ο πίνακας των πρώτων αριθμών είναι:\n");
		for(i=0;i<primes_found;i++)
			printf("%-8d", prime[i]);
	}
	else//αν δεν βρεθούν πρώτοι αριθμοί
		printf("\nΔεν υπάρχουν πρώτοι αριθμοί.\n");
	
	//αν έχουν βρεθεί πρώτοι αριθμοί
	if(primes_found)
	{
		printf("\n\nΗ μέγιστη απόλυτη διαφορά των παραπάνω πρώτων αριθμών είναι %d", max_absolute_diff(prime, primes_found));
	}
	
	
	return 0;
}

/*έλεγχος αν υπάρχει καποιο στοιχείο μέσα σε έναν δυδιάστατο πίνακα
  η συνάρτηση σαν παράμετρο παίρνει έναν δείκτη σε έναν πίνακα με n στοιχεία, ωστε να μπορούμε να περάσουμε
  έναν διδιαστατο πίνακα σαν όρισμα*/
int elem_exists(int elem, int (*arr)[N])
{
	int i,j;
	
	for(i=0;i<N;i++)
	{
		for(j=0;j<N;j++)
		{
			if(arr[i][j] == elem)
			{
				return True;
			}
		}
	}	
	return False;
}


/*Συνάρτηση για το Initialization ενός διδιαστατου πίνακα με μηδενικά για αποφυγή λάθους λόγω άγνωστων τιμών κατά την χρήση του πίνακα*/
void init_2d_array(int (*arr)[N])
{
	int i,j;
	for(i=0;i<N;i++)
	{
		for(j=0;j<N;j++)
		{
			arr[i][j] = 0;
		}
	}
}

/* Συνάρτηση για τύπωμα ενός διδιάστατου πίνακα σε γραμμές */
void print_lines(int (*arr)[N])
{
	int i,j;
	for(i=0;i<N;i++)
	{
		for(j=0;j<N;j++)
		{
			printf("%-8d",arr[i][j]);
		}
		printf("\n");
	}
}

/*Συνάρτηση για αντιγραφή ενός διδιάστατου πίνακα σε έναν άλλον*/
void copy_array(int (*source)[N], int (*dest)[N])
{
	int i,j;
	for(i=0;i<N;i++)
	{
		for(j=0;j<N;j++)
		{
			dest[i][j] = source[i][j];
		}
	}
}

/*Συνάρτηση μετατροπής ενός πίνακα στον ανάστροφο του */
void calc_transpose(int (*arr)[N])
{
	int i,j;
	int temp[N][N];
	for(i=0;i<N;i++)
	{
		for(j=i+1;j<N;j++)
		{
			temp[i][j] = arr[i][j];
			arr[i][j] = arr[j][i];
			arr[j][i] = temp[i][j];
		}
	}
}

/*Συνάρτηση μέτρησης αρθροίσματος της διαγωνίου ενός πίνακα*/
int diagonal_sum(int (*arr)[N])
{
	int i,j;
	int sum = 0;
	for(i=0;i<N;i++)
	{
		for(j=0;j<N;j++)
		{
			if(i == j)
				sum += arr[i][j];
		}
	}
	return sum;
}

/*Συνάρτηση ελέγχου αν ένας αριθμός είναι πρώτος η όχι*/
int is_prime(number)
{
	int i = 2;
	if(number == 1)
	{
		return False;
	}
	else
	{
		while(i<= number/2)
		{
			if(number % i  == 0)
			{
				return False;
			}
			i++;
		}
	}
	return True;
}

/*Συνάρτηση αρχικοποίησης ενός μονοδιάστατου πίνακα*/
void init_1d_array(int *arr)
{
	int i;
	for(i=0;i<N*N;i++)
	{
		arr[i] = 0;
	}
}


/*Συνάρτηση μέτρησης της μέγιστης απόλυτης διαφοράς */
int max_absolute_diff(int *arr, int primes)
{
	int diff;
	int max_abs_diff = 0;
	int i,j;
	for(i=0;i<primes - 1;i++)
	{
		for(j=i+1;j<primes;j++)
		{
			diff = arr[i] - arr[j];
			if(diff < 0)
				diff *= -1;
			if(diff > max_abs_diff)
				max_abs_diff = diff;
		}
	}
	return max_abs_diff;
}


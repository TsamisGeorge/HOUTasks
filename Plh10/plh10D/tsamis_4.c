#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define L 30   		/* Πλήθος χαρακτήρων ονόματος υποψηφίων */ 
#define M 5     	/* Πλήθος ψηφοφοριών */
#define N 4		    /* Πλήθος υποψηφίων */

typedef struct node			/* Κόμβος λίστας ψηφοφορίας */
{
	char name[L+1];			/* Όνομα υποψηφίου */
	struct node * next;		/* Επόμενος στη λίστα ψηφοφορίας */
} node;


typedef struct candidate	/* Δομή υποψηφίου */
{
	char name[L+1];			/* Όνομα υποψηφίου */
	int  points;			/* Σύνολο βαθμών υποψηφίου */
} candidate;

candidate 	candidates_table[N];	/* Πίνακας Ν υποψηφίων */

/* Συνάρτηση που ζητεί από τον χρήστη τα ονόματα ενός συνόλου υποψηφίων, που το πλήθος τους δίνεται από την παράμετρο count. */
void Entercandidates(candidate candidates_table[], int count)
{
	//Δηλώσεις που θα χρειαστουν για την χρήση της συνάρτησης 
	int i, j, exists, c;
	char buffer[L+1];
	
	//Αρχικοποίηση του πεδίων points του κάθε υποψηφίου σε 0
	for(i = 0;i<count;i++)
	{
		candidates_table[i].points = 0;
	}
	
	printf("Δώστε τα ονόματα των 4 υποψηφιών.\n");
	for(i = 0;i<count;i++)
	{
		while(1)
		{
			//boolean(int 0 ή 1) μεταβλητή για να δούμε άν ένα όνομα υπάρχει μέσα στα ήδη υπάρχον ονόματα
			exists = 0;
			
			//ζητάμε Input και με την χρήση της fgets το αποθηκεύουμε σε ένα buffer για να μπορέσουμε να
			//κάνουμε τους απαραίτητους ελέγχους
			printf("\nΥποψήφιος %d: ", i+1);
			fgets(buffer, L+1, stdin);
			//χρήση της strcspn για να αφαιρέσουμε το '\n' πο αποθηκεύει στο προτελευταίο μέρος της η fgets οταν 
			//παίρνει Input, και αντικαταστασή του με το '\0' ώστε να μην υπάρχει το \n στο buffer για
			//να λειτουργήσουν σωστά οι συγκρίσεις
			buffer[strcspn(buffer, "\n")] = '\0';
			
			//έλεγχος αν υπάρχει το buffer που έδωσε ο χρήστης ήδη στο candidates_table[].name
			for(j = 0;j<i;j++)
			{
				if(strcmp(candidates_table[j].name, buffer) == 0)
					exists = 1;
			}
			//Αν υπάρχει τυπώνουμε αναλόγως
			if(exists)
			{
				printf("\nΑυτός ο υποψήφιος υπάρχει ήδη.");	
			}
			//αλλιώς γίνεται αποθήκευση του buffer στο candidates_table[i].name
			else
			{
				strcpy(candidates_table[i].name, buffer);
				break;	
			}
		}
	}
}

/* Συνάρτηση που διαβάζει τα στοιχεία για μία ψηφοφορία,  το πλήθος των ψηφοφόρων και στη συνέχεια 
τα αποτελέσματα της ψηφοφορίας.  Η συνάρτηση θα πρέπει να υπολογίζει το πλήθος βαθμών του κάθε υποψηφίου 
από την ψηφοφορία και να ενημερώνει κατάλληλα  τον πίνακα candidates_table που περιέχει στοιχεία για count σε πλήθος υποψήφιους. */
void Entervotes(candidate candidates_table[], int count)
{
	//αρχικοποίηση των απαραίτητων δεικτών για την συνάρτηση
	node *head = NULL, *current = NULL, *new_node = NULL , *temp = NULL;
	//αρχικοποίηση των απαραίτητων μεταβλητών για την συνάρτηση
	int i, j, votes, exists_in_table, exists_in_list, c;
	char buffer[L+1];
	
	//Ζητάμε για εισαγωγή του αριθμού και χρήση του while ((c = getchar()) != EOF && c != '\n') για εκκαθάρηση της stdin
	printf("Δώστε αριθμό ψήφων: ");
	scanf("%d", &votes);
	while ((c = getchar()) != EOF && c != '\n');
	
	printf("Δώστε αποτέλεσμα ψηφοφορίας σε φθίνουσα σειρά εκλογής.\n");
	for(i = 0; i < count; i++)
	{
		while(1)
		{
			//Δηλώσεις boolean τύπου μεταβλητών για να δούμε αν ένα όνομα υπάρχει στο candidates_table/ στην λίστα των ονομάτων
			exists_in_list = 0;
			exists_in_table = 0;
			
			//Ζητάμε για εισαγωγή ονόματος και το αποθηκεύουμε στο buffer προσωρηνα για να γίνουν οι ελέγχοι
			printf("\n%dος υποψήφιος: ", i+1);
			fgets(buffer, L+1, stdin);
			buffer[strcspn(buffer, "\n")] = '\0';
			
			//Βλέπουμε αν το buffer είναι ίδιο με κάποιο από τα ονόματα που υπάρχουν στο candidates_table(στην συγκεκριμένη
			//περίπτωση θέλουμε το exists_in_table να γίνει 1 για κάθε εισαγωγή ονόματος που γίνεται)
			for(j = 0; j < count; j++)
			{
				if(strcmp(candidates_table[j].name, buffer) == 0)
					exists_in_table = 1;
			}
			
			//Βλέπουμε αν το buffer είναι ίδιο με οποιοδήποτε από τα ονόματα μέσα στην λίστα.
			//Αν το current είναι NULL σημαίνει πως ο χρήστης δεν έχει εισάγει ονόματα ακόμα σε αυτη την επανάληψη του i
			if(current != NULL)
			{
				//θέτουμε το temp να δείχνει στο head
				temp = head;
				
				//Ενόσω το temp δεν είναι NULL τοτε κάνουμε την σύγκριση του buffer με το temp -> name, αν είναι ίδια σημαίνει πως υπάρχει
				//το ίδιο όνομα, κατι που είναι invalid οπότε το exists_in_list γινεται 1 και μετά φευγουμε απο τον βρόχο
				while(temp != NULL)
				{
					if(strcmp(temp->name, buffer) == 0)
					{
						exists_in_list = 1;
						break;
					}
					temp = temp -> next;
				}
			}

			//Αν το στοιχείο υπάρχει στο candidates_table και δεν υπάρχει στην προσωρινή λίστα
			if(exists_in_table && !exists_in_list)
			{	
				//Κάνουμε δεύσμευση χώρου για τον νέο κόμβο
				new_node = (node *)malloc(sizeof(node));
				if(!new_node)
				{
					printf("Error: Memory allocation failed.");
					exit(1);
				}
				
				//Κανουμε αντιγραφή του buffer στο πεδίο name του new_node και θέτουμε τον επόμενο δείκτη του να είναι NULL
				strcpy(new_node -> name, buffer);
				new_node -> next = NULL;
				
				//Αν είναι ο πρώτος κόμβος, βάζουμε το head να δείχνει στο new_node και το current να δείχνει στο head
				if(current == NULL)
				{
					head = new_node;
					current = head;
				}
				
				//Αν δεν είναι ο πρώτος κόμβος, αρχικά βάζουμε το current -> next να δείχνει στον νέο κόμβο, αυτο σημαινει πως ο κόμβος μπαίνει στο σωστο σημείο
				//Μετα βάζουμε το current να είναι ο νεος κόμβος, οπότε στην επόμενη επανάληψη ο current δείκτης δείχνει στον παρόν κόμβο
				else
				{
					current -> next = new_node;
					current = new_node;
				}
				break;	
			}
			else
			{
				printf("\nΑυτός ο υποψήφιος δεν υπάρχει ή υπάρχει ήδη στην παρούσα εκλογή.\n");
			}
		}
	}
	
	//Στο τέλος της επανάληψης αφού έχουν εισαχθεί όλοι οι υποψήφιοι με descending order
	//γίνεται μία διαπέραση της συνδεδεμένης λίστας μαζί με χρήση counter μεταβλητής για να 
	//βάλουμε την αντίστοιχη τιμή των πόντων στο εκάστοτε όνομα
	temp = head;
	int cnt = 0;
	while(temp != NULL)
	{
		for(j=0;j<count;j++)
		{
			if(strcmp(temp->name , candidates_table[j].name) == 0)
			{
				candidates_table[j].points += votes * (count - cnt);
				break;
			}
		}
		temp = temp->next;
		cnt++;
	}

	
	//Αποδεύσμευση της μνήμης κάθε φορά πριν φύγουμε από την συνάρτηση
	current = head;
	while (current != NULL) 
	{
	    temp = current;
	    current = current->next;
	    free(temp);
	}
}


/*Κυρίως πρόγραμμα που τεστάρει τις συναρτήσεις με τη σειρά που δόθηκαν */
int main()
{
	system("chcp 1253>nul"); /* Εισαγωγή Ελληνικών χαρακτήρων */
	int max_points; /* To πλήθος βαθμών του νικητή */
	int i;
	
	Entercandidates(candidates_table, N);				/* Εισαγωγή ονομάτων υποψηφίων */
	printf("\n");
	/* Διάβασμα ψηφοφοριών και υπολογισμός πλήθους βαθμών με χρήση Borda Count */
	for (i=0; i<M; i++)
	{
				printf("Δώστε στοιχεία για την %dη ψηφοφορία. \n", i+1);
				Entervotes(candidates_table, N);  /* Διάβασμα λίστας ψηφοφορίας */
	}

	
    /* Ακολουθεί η εύρεση του υποψήφιου (των υποψηφίων) με το μεγαλύτερο πλήθος βαθμών. */
	max_points=candidates_table[0].points;
	for(i=1;i<N;i++) if (max_points<candidates_table[i].points) max_points=candidates_table[i].points;

	printf("O ΥΠΟΨΗΦΙΟΣ ΜΕ ΤΟΥΣ ΠΕΡΙΣΣΟΤΕΡΟΥΣ ΒΑΘΜΟΥΣ ΣΤΗΝ ΨΗΦΟΦΟΡΙΑ ΕΙΝΑΙ:\n");
	for (i=0; i<N; i++)
	   if (candidates_table[i].points==max_points)
	        printf("Όνομα: %s  Βαθμοί:%d \n", candidates_table[i].name, candidates_table[i].points);
	system("pause");
   	return 0;
}

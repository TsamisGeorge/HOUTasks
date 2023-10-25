#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define N 30  			

struct StackNode {       /*Δήλωση κόμβου στοίβας */
	char address[N];      
	struct StackNode *next;
};
		
typedef struct StackNode *stack;    

void push(stack *sp, char address_string[N])
{
	//Φτιάχνουμε έναν δείκτη σε δομή StackNode και κάνουμε δεύσμευση της μνήμης που θα χρειαστεί
	stack new_node = (stack)malloc(sizeof(struct StackNode));
	
	//Αμυντικός προγραμματισμός σε περίπτωση αδυναμίας δεύσμευσης μνήμης
	if(!new_node)
	{
		printf("\nΑποτυχία δεύσμευσης μνήμης.");
		exit(0);
	}
	//Αναθέτουμε την τιμή του address_string που δόθηκε από έξω στο new_node -> address
	strcpy(new_node->address, address_string);
	//Βαζουμε το next του καινουργιου κομβου να δείχνει στο στοιχείο που δείχνει ο head δείκτης
	new_node -> next = *sp;
	//Βάζουμε τον δείκτη head να δείχνει στον νεο κόμβο, άρα πλέον είναι το πρώτο στοιχείο στην στοίβα
	*sp = new_node;
}


int pop (stack *sp, char address[N])
{
	//Αν η στοίβα είναι άδεια δεν θα κάνει το pop και θα επιστρέψει -1
	if(*sp == NULL)
	{
		return -1;
	}
	//Αν η στοίβα δεν είναι άδεια, τοτε φτιάχνουμε έναν προσωρινό δείκτη σε δομή StackNode και τον βάζουμε να δείχνει στον Head δεικτη(sp)
	//που δώθηκε στην κλήση της συνάρτησης
	stack temp_node = *sp;
	//αντιγραφή τιμών απο το address του temp_node στο address που πήραμε απο έξω ώστε να μην χάσουμε την διέυθυνση
	//που θέλουμε να βγάλουμε απο το την στοίβα
	strcpy(address, temp_node -> address);
	//βάζουμε το sp που πήραμε απο την κλήση της συνάρτησης να δείχνει στο επόμενο στοιχείο πριν κάνουμε αποδεύσμευση του temp_node
	*sp = (*sp) -> next;
	free(temp_node);
	//εφόσον αυτά πετύχουν επιστροφή του 0
	return 0;
}


void empty_stack(stack *sp)
{
	//Φτιάχνουμε 2 δείκτες για τον παρόν και προηγούμενο κόμβο
	stack current, prev;
	//Βαζουμε τον παρόν κόμβο να δείχνει στο head δεικτη
	current = *sp;
	//Αν η στοίβα δεν είναι άδεια
	if(current != NULL)
	{
		//Όσο ο παρόν δείκτης δεν είναι NULL
		while(current != NULL)
		{
			//Θέτουμε τον προηγούμε να είναι ο παρόν
			prev = current;
			//Θέτουμε τον παρόν να είναι το επόμενο στοιχείο
			current = current -> next;
			//Αποδεσμεύουμε την μνήμη του προηγούμενου κόμβου
			free(prev);
		}		
	}
	//βάζουμε το head να δείχνει σε null ώστε να μην υπάρχουν προβλήματα κατα την χρήση του προγράμματος
	*sp = NULL;
}



void print_stack (stack sp)
{
	//temporary δεικτης σε δομη StackNode, και ανάθεση να δείχνει όπου και το head
	stack current;
	current = sp;
	
	//Τύπωμα αναλόγως αν δεν υπάρχουν στοιχεία
	if(current == NULL)
		printf("\nΔεν υπάρχουν διευθύνσεις.");	
	else//Τύπωμα μέχρι το current να δειχνει σε NULL
	{
		while(current != NULL)
		{
			printf("%s\t", current -> address);
			//Αλλαγή του current σε current -> next ώστε να συνεχιστεί ο βρόχος
			current = current -> next;
		}
	}
}

int main() { 
	int choice;
	char address[N];
	stack s1 = NULL;           
	stack s2 = NULL;         
	system("chcp 1253>nul");
	do{
        printf("\nΔιαθέσιμες Επιλογές:\n");
		printf("1. Εισαγωγή διεύθυνσης\n");
        printf("2. Πίσω (στην προηγούμενη διεύθυνση)\n");
        printf("3. Εμφάνιση περιεχομένων στοίβας διευθύνσεων s1 (αντίστροφη σειρά)\n");
        printf("4. Εμπρός (στη διεύθυνση από την οποία επιστρέψαμε)\n");
        printf("5. Έξοδος\n");
        printf("Εισάγετε επιλογή:");
		scanf("%d", &choice);
		switch (choice) 
		{
			case 1:  
				printf("Εισάγετε διεύθυνση: ");
				scanf("%s", address);
				push(&s1, address);
				empty_stack(&s2);
			break;
			case 2:  
				if (pop(&s1, address)==0)
				{			
					push(&s2, address);
					if (s1!=NULL)
						printf("%s\n",s1->address);
				}
				else
					printf("\nΗ στοίβα είναι άδεια!\n");
			break;
			
			case 3:  
				print_stack(s1);
				printf("\n\n"); 
			break;
			
			case 4:  
				if (pop(&s2, address)==0)
				{
					printf("%s\n\n",address);
					push(&s1,address);
				}
				else
					printf("\nH στοίβα είναι άδεια!");
			break;
		}
    }while (choice != 5);
	return (0);
}

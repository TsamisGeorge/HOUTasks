#include <stdio.h>
#define DATA_SIZE 5
#define RANGE 150
main()
{	
	system("chcp 1253>nul");
	int pin[DATA_SIZE],pinaux[RANGE+1];
	int min,max,counter,i;
	printf("Εισάγετε 5 ακεραίους αριθμούς περιορισμένου εύρους R=150.\n");
	for(i=0;i<DATA_SIZE;i++)
	{
		printf("%dος αριθμός: ",i+1);
		scanf("%d",&pin[i]);
	}
	for(i=0;i<=RANGE;i++)
		pinaux[i]=0;
	min=pin[0];
	for(i=1;i<DATA_SIZE;i++)
	{
		if(pin[i]<min)
			min=pin[i];
	}
	max=pin[0];
	for(i=1;i<DATA_SIZE;i++)
	{
		if(pin[i]>max)
			max=pin[i];
	}
	if((max-min)<RANGE)
	{
		for(i=0;i<DATA_SIZE;i++)
			pinaux[pin[i]-min]=1;
		counter=0;
		for(i=0;i<RANGE;i++)
		{
			if(pinaux[i]==1)
			{
				pin[counter]=i+min;
				counter+=1;
			}
		}
		printf("Ταξινομημένος πίνακας:");
		for(i=0;i<DATA_SIZE;i++)
			printf("[%d]",pin[i]);
	}
	else
		printf("Πίνακας δεδομένων εκτος του περιορισμένου εύρους.\nΔεν μπορεί να γίνει ταξινόμηση.\nΤέλος προγράμματος.");
}

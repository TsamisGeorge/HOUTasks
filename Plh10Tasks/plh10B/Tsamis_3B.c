#include <stdio.h>
#define N 10
main()
{	
	system("chcp 1253>nul");
	int a,i,counter;
	int pinakas_A[N],pinakas_B[N];
	//υποπρογραμμα 1
	do
	{
		printf("Εισάγετε έναν αριθμό απο 1 έως 5: ");
		scanf("%d",&a);
		if(a<1 || a>5)
			printf("Λάθος καταχώρηση.\n");
	}
	while(a<1 || a>5);
	pinakas_A[0]=a;
	pinakas_A[1]=a+1;
	for(i=2;i<N;i++)
		pinakas_A[i]=(pinakas_A[i-1]+pinakas_A[i-2]);
	printf("\nΈγινε εισαγωγή στοιχείων στον πίνακα Α.\n\n");
	//υποπρογραμμα 2
	printf("Εμφάνιση πίνακα A:\n");
	for(i=0;i<N;i++)
	{
		printf("[%d]:%d\t",i+1,pinakas_A[i]);
	}
	//υποπρογραμμα 3
	printf("\n\nΘέσεις που περιέχουν άρτιους ακεραίους:");
	counter=0;
	for(i=0;i<N;i++)
	{
		if(pinakas_A[i]%2==0)
		{
			printf("[%d]",i+1);
			counter+=1;
		}
	}
	printf("\n\nΠλήθος άρτιων στον πίνακα: %d\n\n",counter);
	for(i=0;i<N;i++)
		pinakas_B[i]=0;
	for(i=0;i<N;i++)
	{
		if(pinakas_A[i]%N==0)
			pinakas_B[9]+=1;
		else
			pinakas_B[(pinakas_A[i]%N)-1]+=1;
	}
	printf("Εμφάνιση πίνακα Β:\n");
	for(i=0;i<N;i++)
	{
		printf("[%d]:%d\t",i+1,pinakas_B[i]);
	}
}

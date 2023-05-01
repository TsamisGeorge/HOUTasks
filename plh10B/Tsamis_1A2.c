#include <stdio.h>
main()
{
	system("chcp 1253>nul");
	int i,j,n,sum,fact;
	do
	{
		printf("Εισάγετε τον αριθμό N(1..9): ");
		scanf("%d",&n);
		if(n<1 || n>9)
			printf("Λάθος καταχώρηση.\n");
	}
	while(n<1 || n>9);
	sum=0;
	for(i=1;i<=n;i++)
	{
		fact=1;
		for(j=2;j<=i;j++)
		{
			fact*=j;
		}
		sum+=fact;
	}
	printf("Άρθροισμα παραγοντικών: %d",sum);
}

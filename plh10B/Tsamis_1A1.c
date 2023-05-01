#include <stdio.h>
main()
{
	system("chcp 1253>nul");
	int i,n,sum,sign;
	do
	{
		printf("Εισάγετε τον αριθμό N(1..9): ");
		scanf("%d",&n);
		if(n<1 || n>9)
			printf("Λάθος καταχώρηση.\n");
	}
	while(n<1 || n>9);
	sum=0;
	sign=1;
	for(i=1;i<=n;i++)
	{
		sum+=sign*i;
		sign*=(-1);
	}
	printf("Άρθροισμα: %d",sum);
}

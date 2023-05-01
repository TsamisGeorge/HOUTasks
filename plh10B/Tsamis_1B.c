#include <stdio.h>
#define size 10
main()
{
	system("chcp 1253>nul");
	float pin[size];
	float sum,avg,min,max;
	int i;
	sum=0;
	for(i=0;i<size;i++)
	{
		printf("Εισάγετε τον %dο βαθμό: ",i+1);
		scanf("%f",&pin[i]);
		sum+=pin[i];
	}
	avg=sum/size;
	printf("\nΜέσος όρος βαθμών: %f\n",avg);
	min=pin[0];
	for(i=1;i<size;i++)
	{
		if(pin[i]<min)
			min=pin[i];
	}
	printf("Διαφορά ελαχίστου βαθμού απο τον μέσο όρο: %f\n",avg-min);
	max=pin[0];
	for(i=1;i<=size;i++)
	{
		if(pin[i]>max)
			max=pin[i];
	}
	printf("Διαφορά μεγίστου βαθμού απο τον μέσο όρο: %f\n",max-avg);
}

#include <stdio.h>
#define N 10
main()
{	
	system("chcp 1253>nul");
	int a,i,counter;
	int pinakas_A[N],pinakas_B[N];
	//������������ 1
	do
	{
		printf("�������� ���� ������ ��� 1 ��� 5: ");
		scanf("%d",&a);
		if(a<1 || a>5)
			printf("����� ����������.\n");
	}
	while(a<1 || a>5);
	pinakas_A[0]=a;
	pinakas_A[1]=a+1;
	for(i=2;i<N;i++)
		pinakas_A[i]=(pinakas_A[i-1]+pinakas_A[i-2]);
	printf("\n����� �������� ��������� ���� ������ �.\n\n");
	//������������ 2
	printf("�������� ������ A:\n");
	for(i=0;i<N;i++)
	{
		printf("[%d]:%d\t",i+1,pinakas_A[i]);
	}
	//������������ 3
	printf("\n\n������ ��� ��������� ������� ���������:");
	counter=0;
	for(i=0;i<N;i++)
	{
		if(pinakas_A[i]%2==0)
		{
			printf("[%d]",i+1);
			counter+=1;
		}
	}
	printf("\n\n������ ������ ���� ������: %d\n\n",counter);
	for(i=0;i<N;i++)
		pinakas_B[i]=0;
	for(i=0;i<N;i++)
	{
		if(pinakas_A[i]%N==0)
			pinakas_B[9]+=1;
		else
			pinakas_B[(pinakas_A[i]%N)-1]+=1;
	}
	printf("�������� ������ �:\n");
	for(i=0;i<N;i++)
	{
		printf("[%d]:%d\t",i+1,pinakas_B[i]);
	}
}

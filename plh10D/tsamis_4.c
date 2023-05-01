#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define L 30   		/* ������ ���������� �������� ��������� */ 
#define M 5     	/* ������ ���������� */
#define N 4		    /* ������ ��������� */

typedef struct node			/* ������ ������ ���������� */
{
	char name[L+1];			/* ����� ��������� */
	struct node * next;		/* �������� ��� ����� ���������� */
} node;


typedef struct candidate	/* ���� ��������� */
{
	char name[L+1];			/* ����� ��������� */
	int  points;			/* ������ ������ ��������� */
} candidate;

candidate 	candidates_table[N];	/* ������� � ��������� */

/* ��������� ��� ����� ��� ��� ������ �� ������� ���� ������� ���������, ��� �� ������ ���� ������� ��� ��� ��������� count. */
void Entercandidates(candidate candidates_table[], int count)
{
	//�������� ��� �� ���������� ��� ��� ����� ��� ���������� 
	int i, j, exists, c;
	char buffer[L+1];
	
	//������������ ��� ������ points ��� ���� ��������� �� 0
	for(i = 0;i<count;i++)
	{
		candidates_table[i].points = 0;
	}
	
	printf("����� �� ������� ��� 4 ���������.\n");
	for(i = 0;i<count;i++)
	{
		while(1)
		{
			//boolean(int 0 � 1) ��������� ��� �� ����� �� ��� ����� ������� ���� ��� ��� ������� �������
			exists = 0;
			
			//������ Input ��� �� ��� ����� ��� fgets �� ������������ �� ��� buffer ��� �� ���������� ��
			//������� ���� ������������ ��������
			printf("\n��������� %d: ", i+1);
			fgets(buffer, L+1, stdin);
			//����� ��� strcspn ��� �� ����������� �� '\n' �� ���������� ��� ������������ ����� ��� � fgets ���� 
			//������� Input, ��� ������������� ��� �� �� '\0' ���� �� ��� ������� �� \n ��� buffer ���
			//�� ������������� ����� �� ����������
			buffer[strcspn(buffer, "\n")] = '\0';
			
			//������� �� ������� �� buffer ��� ����� � ������� ��� ��� candidates_table[].name
			for(j = 0;j<i;j++)
			{
				if(strcmp(candidates_table[j].name, buffer) == 0)
					exists = 1;
			}
			//�� ������� ��������� ��������
			if(exists)
			{
				printf("\n����� � ��������� ������� ���.");	
			}
			//������ ������� ���������� ��� buffer ��� candidates_table[i].name
			else
			{
				strcpy(candidates_table[i].name, buffer);
				break;	
			}
		}
	}
}

/* ��������� ��� �������� �� �������� ��� ��� ���������,  �� ������ ��� ��������� ��� ��� �������� 
�� ������������ ��� ����������.  � ��������� �� ������ �� ���������� �� ������ ������ ��� ���� ��������� 
��� ��� ��������� ��� �� ���������� ���������  ��� ������ candidates_table ��� �������� �������� ��� count �� ������ ����������. */
void Entervotes(candidate candidates_table[], int count)
{
	//������������ ��� ����������� ������� ��� ��� ���������
	node *head = NULL, *current = NULL, *new_node = NULL , *temp = NULL;
	//������������ ��� ����������� ���������� ��� ��� ���������
	int i, j, votes, exists_in_table, exists_in_list, c;
	char buffer[L+1];
	
	//������ ��� �������� ��� ������� ��� ����� ��� while ((c = getchar()) != EOF && c != '\n') ��� ���������� ��� stdin
	printf("����� ������ �����: ");
	scanf("%d", &votes);
	while ((c = getchar()) != EOF && c != '\n');
	
	printf("����� ���������� ���������� �� �������� ����� �������.\n");
	for(i = 0; i < count; i++)
	{
		while(1)
		{
			//�������� boolean ����� ���������� ��� �� ����� �� ��� ����� ������� ��� candidates_table/ ���� ����� ��� ��������
			exists_in_list = 0;
			exists_in_table = 0;
			
			//������ ��� �������� �������� ��� �� ������������ ��� buffer ��������� ��� �� ������ �� �������
			printf("\n%d�� ���������: ", i+1);
			fgets(buffer, L+1, stdin);
			buffer[strcspn(buffer, "\n")] = '\0';
			
			//�������� �� �� buffer ����� ���� �� ������ ��� �� ������� ��� �������� ��� candidates_table(���� ������������
			//��������� ������� �� exists_in_table �� ����� 1 ��� ���� �������� �������� ��� �������)
			for(j = 0; j < count; j++)
			{
				if(strcmp(candidates_table[j].name, buffer) == 0)
					exists_in_table = 1;
			}
			
			//�������� �� �� buffer ����� ���� �� ����������� ��� �� ������� ���� ���� �����.
			//�� �� current ����� NULL �������� ��� � ������� ��� ���� ������� ������� ����� �� ���� ��� ��������� ��� i
			if(current != NULL)
			{
				//������� �� temp �� ������� ��� head
				temp = head;
				
				//����� �� temp ��� ����� NULL ���� ������� ��� �������� ��� buffer �� �� temp -> name, �� ����� ���� �������� ��� �������
				//�� ���� �����, ���� ��� ����� invalid ����� �� exists_in_list ������� 1 ��� ���� �������� ��� ��� �����
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

			//�� �� �������� ������� ��� candidates_table ��� ��� ������� ���� ��������� �����
			if(exists_in_table && !exists_in_list)
			{	
				//������� ��������� ����� ��� ��� ��� �����
				new_node = (node *)malloc(sizeof(node));
				if(!new_node)
				{
					printf("Error: Memory allocation failed.");
					exit(1);
				}
				
				//������� ��������� ��� buffer ��� ����� name ��� new_node ��� ������� ��� ������� ������ ��� �� ����� NULL
				strcpy(new_node -> name, buffer);
				new_node -> next = NULL;
				
				//�� ����� � ������ ������, ������� �� head �� ������� ��� new_node ��� �� current �� ������� ��� head
				if(current == NULL)
				{
					head = new_node;
					current = head;
				}
				
				//�� ��� ����� � ������ ������, ������ ������� �� current -> next �� ������� ���� ��� �����, ���� �������� ��� � ������ ������� ��� ����� ������
				//���� ������� �� current �� ����� � ���� ������, ����� ���� ������� ��������� � current ������� ������� ���� ����� �����
				else
				{
					current -> next = new_node;
					current = new_node;
				}
				break;	
			}
			else
			{
				printf("\n����� � ��������� ��� ������� � ������� ��� ���� ������� ������.\n");
			}
		}
	}
	
	//��� ����� ��� ���������� ���� ����� �������� ���� �� ��������� �� descending order
	//������� ��� ��������� ��� ������������ ������ ���� �� ����� counter ���������� ��� �� 
	//������� ��� ���������� ���� ��� ������ ��� �������� �����
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

	
	//������������ ��� ������ ���� ���� ���� ������� ��� ��� ���������
	current = head;
	while (current != NULL) 
	{
	    temp = current;
	    current = current->next;
	    free(temp);
	}
}


/*������ ��������� ��� �������� ��� ����������� �� �� ����� ��� ������� */
int main()
{
	system("chcp 1253>nul"); /* �������� ��������� ���������� */
	int max_points; /* To ������ ������ ��� ������ */
	int i;
	
	Entercandidates(candidates_table, N);				/* �������� �������� ��������� */
	printf("\n");
	/* �������� ���������� ��� ����������� ������� ������ �� ����� Borda Count */
	for (i=0; i<M; i++)
	{
				printf("����� �������� ��� ��� %d� ���������. \n", i+1);
				Entervotes(candidates_table, N);  /* �������� ������ ���������� */
	}

	
    /* ��������� � ������ ��� ��������� (��� ���������) �� �� ���������� ������ ������. */
	max_points=candidates_table[0].points;
	for(i=1;i<N;i++) if (max_points<candidates_table[i].points) max_points=candidates_table[i].points;

	printf("O ��������� �� ���� ������������� ������� ���� ��������� �����:\n");
	for (i=0; i<N; i++)
	   if (candidates_table[i].points==max_points)
	        printf("�����: %s  ������:%d \n", candidates_table[i].name, candidates_table[i].points);
	system("pause");
   	return 0;
}

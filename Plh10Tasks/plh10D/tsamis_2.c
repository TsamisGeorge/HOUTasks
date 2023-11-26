#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define N 30  			

struct StackNode {       /*������ ������ ������� */
	char address[N];      
	struct StackNode *next;
};
		
typedef struct StackNode *stack;    

void push(stack *sp, char address_string[N])
{
	//���������� ���� ������ �� ���� StackNode ��� ������� ��������� ��� ������ ��� �� ���������
	stack new_node = (stack)malloc(sizeof(struct StackNode));
	
	//��������� ��������������� �� ��������� ��������� ���������� ������
	if(!new_node)
	{
		printf("\n�������� ���������� ������.");
		exit(0);
	}
	//���������� ��� ���� ��� address_string ��� ������ ��� ��� ��� new_node -> address
	strcpy(new_node->address, address_string);
	//������� �� next ��� ����������� ������ �� ������� ��� �������� ��� ������� � head �������
	new_node -> next = *sp;
	//������� ��� ������ head �� ������� ���� ��� �����, ��� ����� ����� �� ����� �������� ���� ������
	*sp = new_node;
}


int pop (stack *sp, char address[N])
{
	//�� � ������ ����� ����� ��� �� ����� �� pop ��� �� ���������� -1
	if(*sp == NULL)
	{
		return -1;
	}
	//�� � ������ ��� ����� �����, ���� ���������� ���� ��������� ������ �� ���� StackNode ��� ��� ������� �� ������� ���� Head ������(sp)
	//��� ������ ���� ����� ��� ����������
	stack temp_node = *sp;
	//��������� ����� ��� �� address ��� temp_node ��� address ��� ������ ��� ��� ���� �� ��� ������� ��� ���������
	//��� ������� �� �������� ��� �� ��� ������
	strcpy(address, temp_node -> address);
	//������� �� sp ��� ������ ��� ��� ����� ��� ���������� �� ������� ��� ������� �������� ���� ������� ������������ ��� temp_node
	*sp = (*sp) -> next;
	free(temp_node);
	//������ ���� �������� ��������� ��� 0
	return 0;
}


void empty_stack(stack *sp)
{
	//���������� 2 ������� ��� ��� ����� ��� ����������� �����
	stack current, prev;
	//������� ��� ����� ����� �� ������� ��� head ������
	current = *sp;
	//�� � ������ ��� ����� �����
	if(current != NULL)
	{
		//��� � ����� ������� ��� ����� NULL
		while(current != NULL)
		{
			//������� ��� ��������� �� ����� � �����
			prev = current;
			//������� ��� ����� �� ����� �� ������� ��������
			current = current -> next;
			//������������� ��� ����� ��� ������������ ������
			free(prev);
		}		
	}
	//������� �� head �� ������� �� null ���� �� ��� �������� ���������� ���� ��� ����� ��� ������������
	*sp = NULL;
}



void print_stack (stack sp)
{
	//temporary ������� �� ���� StackNode, ��� ������� �� ������� ���� ��� �� head
	stack current;
	current = sp;
	
	//������ �������� �� ��� �������� ��������
	if(current == NULL)
		printf("\n��� �������� �����������.");	
	else//������ ����� �� current �� ������� �� NULL
	{
		while(current != NULL)
		{
			printf("%s\t", current -> address);
			//������ ��� current �� current -> next ���� �� ���������� � ������
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
        printf("\n���������� ��������:\n");
		printf("1. �������� ����������\n");
        printf("2. ���� (���� ����������� ���������)\n");
        printf("3. �������� ������������ ������� ����������� s1 (���������� �����)\n");
        printf("4. ������ (��� ��������� ��� ��� ����� �����������)\n");
        printf("5. ������\n");
        printf("�������� �������:");
		scanf("%d", &choice);
		switch (choice) 
		{
			case 1:  
				printf("�������� ���������: ");
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
					printf("\n� ������ ����� �����!\n");
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
					printf("\nH ������ ����� �����!");
			break;
		}
    }while (choice != 5);
	return (0);
}

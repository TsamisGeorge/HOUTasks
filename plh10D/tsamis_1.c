#include <stdio.h>
#define N 4
#define True 1
#define False 0


//��������� ����������� ��� �� ����������� ��� ��� ��������� ��� �����������.
int elem_exists(int elem, int (*arr)[N]);
void init_2d_array(int (*arr)[N]);
void init_1d_array(int *arr);
void print_lines(int (*arr)[N]);
void copy_array(int (*source)[N], int (*dest)[N]);
void calc_transpose(int (*transpose)[N]);
int diagonal_sum(int (*arr)[N]);
int max_absolute_diff(int *arr, int primes);


int main(void)
{
	
	system("chcp 1253 > nul");
	//���� �������� ��� �������������� ��� ������� ������������
	int num, i = 0, j = 0;
	
	int pinakas[N][N];
	int transpose_pin[N][N];
	
	int prime[N*N];
	
	init_2d_array(pinakas);
	init_2d_array(transpose_pin);
	init_1d_array(prime);
	
	printf("�������� ���������� ��������� �������� ��������.\n");
	for(i=0;i<N;i++)
	{
		for(j=0;j<N;j++)
		{
			//����� ������������ for ������ ���� �� �������� �������������� �� ���� ��� ���� ���� ��� ��� ���� ��� ����������
			printf("���� %d, %d: ",i+1,j+1);
			while(scanf("%d", &num) != 1 || elem_exists(num, pinakas) || num < 1)
			{
				printf("\n����� ����������\n�������� ���� �������� ������ ������� ������.\n���� %d, %d: ", i+1, j+1);
				//�������� ��� ���������� ����� �� ��������� ��� newline ���������, ������������ ������ ����� ��� ��� fflush(stdin)
				while (getchar() != '\n');	
			}
			//�� ������� �� input ��� ��� �������� �������������� �������� ��� ������ ��� ������ ���������� ����� �� ������������ ��� pinakas[i][j]
			pinakas[i][j] = num;
		}
	}
	//������ ��� ������ ������
	printf("\n� ������� ����� � ��������.\n");
	print_lines(pinakas);
	
	//��������� ��� ������ ���� transpose_pin ��� ���� ����� ��� calc_transpose ���� �� ���������� �� ���������
	copy_array(pinakas, transpose_pin);
	calc_transpose(transpose_pin);
	
	//������ ��� ����������
	printf("\n� ���������� ������� ����� � ��������.\n");
	print_lines(transpose_pin);
	
	//������ ��� ������������ �� �� ������ ���������� ��� �� �������� ���� ����� �������� ��� ��� 2 �������
	printf("\n�� ��������� ��� ��������� ��� ������ ��������� ��� ������ ����� %d\n",diagonal_sum(pinakas));
	printf("\n�� ��������� ��� ��������� ��� ������ ��������� ��� ���������� ����� %d\n",diagonal_sum(transpose_pin));
	printf("\n�� ��������� ��� ��������� ��� ������ ��������� ��� ������� ����� ���.\n\n");
	
	//��������� �������� ��� ������ �������
	int primes_found = 0;
	for(i=0;i<N;i++)
	{
		for(j=0;j<N;j++)
		{
			//�������� ��� ���� �������� ���� ���� pinakas ����� ������� ����� ������ �� ����� ��� is_prime �� ���� ��������
			if(is_prime(pinakas[i][j]))
			{
				prime[primes_found] = pinakas[i][j];
				primes_found++;
			}
		}
	}
	
	//�� ����� ������ ������ �������
	if(primes_found)
	{
		//������ ��� ������ ������� ��� ������ prime
		printf("� ������� ��� ������ ������� �����:\n");
		for(i=0;i<primes_found;i++)
			printf("%-8d", prime[i]);
	}
	else//�� ��� ������� ������ �������
		printf("\n��� �������� ������ �������.\n");
	
	//�� ����� ������ ������ �������
	if(primes_found)
	{
		printf("\n\n� ������� ������� ������� ��� �������� ������ ������� ����� %d", max_absolute_diff(prime, primes_found));
	}
	
	
	return 0;
}

/*������� �� ������� ������ �������� ���� �� ���� ���������� ������
  � ��������� ��� ��������� ������� ���� ������ �� ���� ������ �� n ��������, ���� �� �������� �� ���������
  ���� ���������� ������ ��� ������*/
int elem_exists(int elem, int (*arr)[N])
{
	int i,j;
	
	for(i=0;i<N;i++)
	{
		for(j=0;j<N;j++)
		{
			if(arr[i][j] == elem)
			{
				return True;
			}
		}
	}	
	return False;
}


/*��������� ��� �� Initialization ���� ����������� ������ �� �������� ��� ������� ������ ���� �������� ����� ���� ��� ����� ��� ������*/
void init_2d_array(int (*arr)[N])
{
	int i,j;
	for(i=0;i<N;i++)
	{
		for(j=0;j<N;j++)
		{
			arr[i][j] = 0;
		}
	}
}

/* ��������� ��� ������ ���� ����������� ������ �� ������� */
void print_lines(int (*arr)[N])
{
	int i,j;
	for(i=0;i<N;i++)
	{
		for(j=0;j<N;j++)
		{
			printf("%-8d",arr[i][j]);
		}
		printf("\n");
	}
}

/*��������� ��� ��������� ���� ����������� ������ �� ���� �����*/
void copy_array(int (*source)[N], int (*dest)[N])
{
	int i,j;
	for(i=0;i<N;i++)
	{
		for(j=0;j<N;j++)
		{
			dest[i][j] = source[i][j];
		}
	}
}

/*��������� ���������� ���� ������ ���� ��������� ��� */
void calc_transpose(int (*arr)[N])
{
	int i,j;
	int temp[N][N];
	for(i=0;i<N;i++)
	{
		for(j=i+1;j<N;j++)
		{
			temp[i][j] = arr[i][j];
			arr[i][j] = arr[j][i];
			arr[j][i] = temp[i][j];
		}
	}
}

/*��������� �������� ������������ ��� ��������� ���� ������*/
int diagonal_sum(int (*arr)[N])
{
	int i,j;
	int sum = 0;
	for(i=0;i<N;i++)
	{
		for(j=0;j<N;j++)
		{
			if(i == j)
				sum += arr[i][j];
		}
	}
	return sum;
}

/*��������� ������� �� ���� ������� ����� ������ � ���*/
int is_prime(number)
{
	int i = 2;
	if(number == 1)
	{
		return False;
	}
	else
	{
		while(i<= number/2)
		{
			if(number % i  == 0)
			{
				return False;
			}
			i++;
		}
	}
	return True;
}

/*��������� ������������� ���� ������������� ������*/
void init_1d_array(int *arr)
{
	int i;
	for(i=0;i<N*N;i++)
	{
		arr[i] = 0;
	}
}


/*��������� �������� ��� �������� �������� �������� */
int max_absolute_diff(int *arr, int primes)
{
	int diff;
	int max_abs_diff = 0;
	int i,j;
	for(i=0;i<primes - 1;i++)
	{
		for(j=i+1;j<primes;j++)
		{
			diff = arr[i] - arr[j];
			if(diff < 0)
				diff *= -1;
			if(diff > max_abs_diff)
				max_abs_diff = diff;
		}
	}
	return max_abs_diff;
}


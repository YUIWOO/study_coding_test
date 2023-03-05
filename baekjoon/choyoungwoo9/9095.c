#include <stdio.h>

int answer;

int ar[11];

void make_table()
{
	for(int i = 1; i <= 11; i ++)
	{
		if(i == 1)
			ar[i] = 1;
		else if(i == 2)
			ar[i] = 2;
		else if(i == 3)
			ar[i] = 4;
		else
		{
			ar[i] = ar[i-1] + ar[i-2] + ar[i-3];
		}
	}
}

void solution()
{
	int n;
	scanf("%d", &n);
	printf("%d\n", ar[n]);
}

int main()
{
	int T;
	scanf("%d", &T);
	for(int i = 0; i < T; i ++)
	{
		make_table();
		solution();
	}
}
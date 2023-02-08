#include <stdio.h>

int is_prime(int num)
{
	for(int i = 2; i * i <= num; i ++)
	{
		if(num % i == 0)
			return 0;
	}
	return 1;
}

int main()
{
	int M, N;
	scanf("%d %d", &M, &N);
	for(int i = M; i <= N; i ++)
	{
		if(i != 1 && is_prime(i))
			printf("%d\n", i);
	}
}
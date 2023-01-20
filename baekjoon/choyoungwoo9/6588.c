#include <stdio.h>
#include <stdlib.h>

int is_prime(int num)
{
	int i = 2;
	while(i * i <= num)
	{
		if(num % i == 0)
			return 0;
		i ++;
	}
	return 1;
}


int N;
void algo()
{
	int tmp = N - 1;
	while(--tmp >= N/2)
	{
		if(is_prime(tmp))
		{
			if(is_prime(N-tmp))
			{
				break;
			}
		}
	}
	if(tmp < N/2)
	{
		printf("Goldbach's conjecture is wrong.\n");
	}
	else
	{
		printf("%d = %d + %d\n", N, N - tmp, tmp);
	}
}

int main()
{
	while(1)
	{
		scanf(" %d", &N);
		if(N == 0)
		
		algo();
	}
}
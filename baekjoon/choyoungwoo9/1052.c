#include <stdio.h>
#include <stdlib.h>

int N, K;

int get_bit_digit(int num)
{
	int count = 0;
	while(1)
	{
		if(num == 0)
			return count;
		num = num / 2;
		count ++;
	}
	return count;
}

int is_move(int oasis)
{
	int bit_digit = get_bit_digit(oasis);
	for(int i = 0; i < bit_digit - K; i ++)
	{
		if(oasis & (1 << i))
			return 0;
	}
	return 1;
}

void solution()
{
	int answer = 0;
	if(N <= K)
	{
		printf("%d", K - N);
			return ;
	}
	int bit_digit = get_bit_digit(N);
	if(bit_digit - K < 0)
	{
		int tmp = N;
		while(1)
		{
			if(tmp == 0)
			{
				printf("-1");
				return ;
			}
			if(tmp == K)
			{
				printf("0");
				return ;
			}
			tmp = tmp / 2;
		}
	}
	while(1)
	{
		if(is_move(answer + N))
			break;
		answer ++;
	}
	printf("%d", answer);
}

int main()
{
	scanf("%d %d", &N, &K);
	solution();
}
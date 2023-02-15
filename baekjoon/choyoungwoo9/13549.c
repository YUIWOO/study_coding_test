#include <stdio.h>
#include <unistd.h>

int N, K;

void fill_table(int *dp_table, int index, int time)
{
	//printf("index : %d time : %d, index : %d\n", index, time, dp_table[index]);
	if(index < 0 || index > 100001)
		return ;
	if(dp_table[index] != -1 && dp_table[index] <= time)
		return;
	//printf("index : %d time : %d\n", index, time);
	//usleep(1000 * 300);
	dp_table[index] = time;
	fill_table(dp_table, index * 2, time);
	fill_table(dp_table, index + 1, time + 1);
	fill_table(dp_table, index + -1, time + 1);
}

int main()
{
	int dp_table[100001] = { -1, };
	for(int i = 0; i < 100001; i ++)
		dp_table[i] = -1;
	scanf("%d %d", &N, &K);
	fill_table(dp_table, N, 0);
	printf("%d\n", dp_table[K]);
}

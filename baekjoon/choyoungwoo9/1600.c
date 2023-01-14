#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int K;
int W;
int H;
int max = 2147483647;

typedef struct s_point
{
	int x;
	int y;
}	t_point;

int **copy_map(int **map)
{
	int **copied_map;
	copied_map = malloc(sizeof(int *) * H);
	for(int i = 0; i < H; i ++)
		copied_map[i] = malloc(sizeof(int) * W);
	for(int i = 0; i < H; i ++)
	{
		for(int j = 0; j < W; j ++)
			copied_map[i][j] = map[i][j];
	}
	return copied_map;
}

int is_valid_point(int **map, int x, int y)
{
	if(x < 0 || x >= W || y < 0 || y >=H)
		return 0;
	if(map[y][x] == 1)
		return 0;
	return 1;
}

void print_map(int **map, int count)
{
	printf("count : %d\n", count);
	for(int i = 0; i < H; i ++)
	{
		for(int j = 0; j < W; j ++)
			printf("%d ", map[i][j]);
		printf("\n");
	}
}
int dfs(int x, int y, int **map, int count, int ult_move)
{
	int ret;
	ret = -1;
	if(!is_valid_point(map, x, y) || ult_move > K)
		return -1;
	map = copy_map(map);
	if(x == W - 1 && y == H - 1)
		return count;
	map[y][x] = 1;
	ret = dfs(x + 1, y, map, count + 1, ult_move);
	if(ret != -1)
	{
		if(ret < max)
			max = ret;
	}
	ret = dfs(x, y + 1, map, count + 1, ult_move);
	if(ret != -1)
	{
		if(ret < max)
			max = ret;
	}
	ret = dfs(x - 1, y, map, count + 1, ult_move);
	if(ret != -1)
	{
		if(ret < max)
			max = ret;
	}
	ret = dfs(x, y - 1, map, count + 1, ult_move);
	if(ret != -1)
	{
		if(ret < max)
			max = ret;
	}
	ret = dfs(x + 2, y - 1, map, count + 1, ult_move + 1);
	if(ret != -1)
	{
		if(ret < max)
			max = ret;
	}
	ret = dfs(x + 2, y + 1, map, count + 1, ult_move + 1);
	if(ret != -1)
	{
		if(ret < max)
			max = ret;
	}
	ret = dfs(x - 2, y - 1, map, count + 1, ult_move + 1);
	if(ret != -1)
	{
		if(ret < max)
			max = ret;
	}
	ret = dfs(x - 2, y + 1, map, count + 1, ult_move + 1);
	if(ret != -1)
	{
		if(ret < max)
			max = ret;
	}
	ret = dfs(x + 1, y + 2, map, count + 1, ult_move + 1);
	if(ret != -1)
	{
		if(ret < max)
			max = ret;
	}
	ret = dfs(x + 1, y - 2, map, count + 1, ult_move + 1);
	if(ret != -1)
	{
		if(ret < max)
			max = ret;
	}
	ret = dfs(x - 1, y + 2, map, count + 1, ult_move + 1);
	if(ret != -1)
	{
		if(ret < max)
			max = ret;
	}
	ret = dfs(x - 1, y + 2, map, count + 1, ult_move + 1);
	if(ret != -1)
	{
		if(ret < max)
			max = ret;
	}
	return ret;
}

int main()
{
	int **map;
	scanf("%d", &K);
	scanf("%d %d", &W, &H);
	map = malloc(sizeof(int *) * H);
	for(int i = 0; i < H; i ++)
		map[i] = malloc(sizeof(int) * W);
	for(int i = 0; i < H; i ++)
	{
		for(int j = 0; j < W; j ++)
			scanf("%d", &map[i][j]);
	}
	dfs(0, 0, map, 0, 0);
	if(max == 2147483647)
		printf("-1");
	else
		printf("%d", max);
}
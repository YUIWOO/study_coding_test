#include <stdio.h>
#include <stdlib.h>

int N, L, R;
int **map;
int **map_union;

int union_num= 0;

void initialize_map_union()
{
	for(int i = 0; i < N; i ++)
	{
		for(int j = 0; j < N; j ++)
			map_union[i][j] = -1;
	}
}



int find_my_union(int i, int j)
{
	if(map_union != -1)
		return 0;
	
}

void merge_union()
{

}

void game()
{
	int flag = 0;
	for(int i = 0; i < N; i ++)
	{
		for(int j = 0; j < N; j ++)
		{
			find_my_union(i, j);
		}
	}
	merge_union();
	return ;
}

void game_start()
{
	int game_count = 0;
	while(1)
	{
		initialize_map_union();
		game();
		if(check_map_union())
			break;
		game_count ++;
	}
	printf("game_count : %d\n", game_count);
}

int main()
{
	scanf("%d %d %d", &N, &L, &R);
	map = malloc(sizeof(int *) * N);
	for(int i = 0; i < N; i ++)
	{
		map[i] = malloc(sizeof(int) * N);
	}
	map_union = malloc(sizeof(int *) * N);
	for(int i = 0; i < N; i ++)
	{
		map_union[i] = malloc(sizeof(int) * N);
	}
	for(int i = 0; i < N; i ++)
	{
		for(int j = 0; j < N; j ++)
			scanf(" %d", &map[i][j]);
	}
	game_start();
	// for(int i = 0; i < N; i ++)
	// {
	// 	for(int j = 0; j < N; j ++)
	// 	{
	// 		printf("%d ", map[i][j]);
	// 	}
	// 	printf("\n");
	//}
}
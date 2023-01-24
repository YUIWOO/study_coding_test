
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int map_valid_check(char *map)
{
	printf("%s", strstr(map, "AA"));
	while((strstr(map, "AA") || strstr(map, "BB")) )
	{
		printf("%s", strstr(map, "AA"));
	}

	return 1;
}

int main()
{
	int num;
	int answer = 0;
	scanf("%d", &num);
	char *map;
	for(int i = 0; i < num; i ++)
	{
		map = (char *)malloc(100000);
		scanf("%s", map);
		if(map_valid_check(map))
			answer ++;
	}
	printf("%d", answer);
}
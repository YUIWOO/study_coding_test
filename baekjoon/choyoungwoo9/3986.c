
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int map_valid_check(char *map)
{
	int a_count = 0;
	int b_count = 0;
	for(int i = 0; *(map + i); i ++)
	{
		if(*(map + i) == 'A')
			a_count ++;
		if(*(map + i) == 'B')
			b_count ++;
	}
	if(a_count%2 || b_count%2)
		return 0;
	if(strstr(map, "ABA"))
		return 0;
	if(strstr(map, "BAB"))
		return 0;
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
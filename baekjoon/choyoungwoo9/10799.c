#include <stdio.h>
#include <stdlib.h>
#include <string.h>



int main()
{
	char *str;
	str = malloc(sizeof(char) * 100001);
	//scanf("%s", str);
	char c;
	int i = 0;
	while(1)
	{
		scanf("%c", &c);
		if(c == '\n')
			break;
		*(str + i) = c;
		i ++;
	}
	*(str + i) = 0;
	//printf("%s\n", str);
	int answer;
	int stick_count;
	stick_count = 0;
	answer = 0;
	for(int i = 0; *(str + i); i++)
	{
		if(*(str + i) == '(' && *(str + i + 1) == ')')
		{
			answer = answer + stick_count;
			i ++;
		}
		else if(*(str + i) == '(')
		{
			stick_count ++;
			answer ++;
		}
		else if(*(str + i) == ')')
		{
			stick_count --;
		}
		// else
		// {
		// 	printf("??\n");
		// }
	}
	printf("%d\n", answer);
	//printf("%d\n", stick_count);
}

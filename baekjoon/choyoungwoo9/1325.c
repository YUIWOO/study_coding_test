#include <stdio.h>
#include <stdbool.h>

int N, M;


typedef struct relation
{
	int num;
	struct relation *next;
}	relation;

relation index_ar[10001];
relation relation_pool[100000];
int count = 0;
int trustee_count[10001];
relation *get_from_pool(int num)
{
	relation_pool[count].num = num;
	relation_pool[count].next = NULL;

	return &relation_pool[count ++];
}

void push_index_B(int A, int B)
{
	relation *truster = &index_ar[B];
	while(truster->next)
		truster = truster->next;
	truster->next = get_from_pool(A);
}

void dfs(int truster_num, int num, bool *visited)
{
	relation *tmp = &index_ar[num];
	tmp = tmp->next;
	while(tmp)
	{
		if(visited[tmp->num] == false)
		{
			visited[tmp->num] = true;
			trustee_count[truster_num] ++;
			dfs(truster_num, tmp->num, visited);
		}
		tmp = tmp->next;
	}
}

void set_trustee_num(int index)
{
	bool visited[10001] = {false, };
	visited[index] = true;
	dfs(index, index, visited);
}

int main()
{
	scanf("%d %d", &N, &M);
	for(int i = 0; i < M; i ++)
	{
		int A, B;
		scanf(" %d %d", &A, &B);
		push_index_B(A, B);
	}
	int max = -1;
	for(int i = 1; i <= N; i ++)
	{
		set_trustee_num(i);
		if(trustee_count[i] > max)
			max = trustee_count[i];
	}
	for(int i = 1; i <= N; i ++)
	{
		if(trustee_count[i] == max)
			printf("%d ", i);
	}
}

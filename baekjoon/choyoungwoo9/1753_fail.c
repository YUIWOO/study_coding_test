#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int V, E;
int ROOT;

int min;

typedef struct node
{
	int num;
	int weight;
	struct node *next;
}	node;

node node_pool[600000];
node index_node[20001];
int tmp_node = 0;

node *get_node(int num, int weight)
{
	node_pool[tmp_node].num = num;
	node_pool[tmp_node].weight = weight;
	node_pool[tmp_node].next = NULL;
	return &node_pool[tmp_node ++];
}

node *add_relation(int v1, int v2, int weight)
{
	node *tmp = index_node[v1].next;
	while(tmp->next)
		tmp = tmp->next;
	tmp->next = get_node(v2, weight);
	tmp = index_node[v2].next;
	while(tmp->next)
		tmp = tmp->next;
	tmp->next = get_node(v1, weight);
}

void dfs(int curr, int dest)
{
	int visited[20001] = {0, };
	int Queue[20002];
	int Front = -1;
	int Rear = -1;
	Queue[++Rear] = curr;
	visited[curr] = 1;
	while(Front != Rear)
	{
		int curr = Queue[++Front];
		for(node *tmp = index_node[curr].next; tmp; tmp = tmp->next)
		{
			if(!visited[tmp->num])
		}
	}
}

int main()
{
	scanf("%d %d", &V, &E);
	scanf(" %d", &ROOT);
	for(int i = 0; i < E; i ++)
	{
		int v1, v2, weight;
		scanf(" %d %d %d", &v1, &v2, &weight);
		add_relation(v1, v2, weight);
	}
	for(int i = 1; i <= V; i ++)
	{
		min = 2147483647;
		dfs(ROOT, i);
		if(min == 2147483647)
			printf("INF\n");
		else
			printf("%d\n", min);
	}
}










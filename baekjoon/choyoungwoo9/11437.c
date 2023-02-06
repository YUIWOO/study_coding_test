#include <stdio.h>

typedef struct node_relation
{
	int vertex_num;
	struct node_relation *relate;
}	relation;

typedef struct vertex_info
{
	int parent;
	int depth;
}	vertex_info;

relation vertex_index[50001];
relation vertex_pool[100000];
int count = 0;

relation *get_node(int vertex_num)
{
	vertex_pool[count].vertex_num = vertex_num;
	vertex_pool[count].relate = NULL;
	return &vertex_pool[count ++];
}

vertex_info info[50001];

void set_node(int vertex_1, int vertex_2)
{
	relation *tmp;
	tmp = &vertex_index[vertex_1];
	while(tmp->relate)
		tmp = tmp->relate;
	tmp->relate = get_node(vertex_2);
	tmp = &vertex_index[vertex_2];
	while(tmp->relate)
		tmp = tmp->relate;
	tmp->relate = get_node(vertex_1);
}

void dfs(int parent, int depth)
{
	relation *parent_relation = &vertex_index[parent];
	while(parent_relation->relate)
	{
		parent_relation = parent_relation->relate;
		if(info[parent_relation->vertex_num].parent == 0)
		{
			info[parent_relation->vertex_num].parent = parent;
			info[parent_relation->vertex_num].depth = depth + 1;
			dfs(parent_relation->vertex_num, depth + 1);
		}
	}
}

void print_common_ancestor(int vertex_1, int vertex_2)
{
	int high_vertex, low_vertex;
	if(info[vertex_1].depth >= info[vertex_2].depth)
	{
		high_vertex = vertex_2;
		low_vertex = vertex_1;
	}
	else
	{
		high_vertex = vertex_1;
		low_vertex = vertex_2;
	}
	while(info[high_vertex].depth != info[low_vertex].depth)
	{
		//printf("here\n");
		low_vertex = info[low_vertex].parent;
	}
	while(high_vertex != low_vertex)
	{
		//printf("here\n");
		high_vertex = info[high_vertex].parent;
		low_vertex = info[low_vertex].parent;
	}
	printf("%d\n", high_vertex);	
}

void make_tree()
{
	info[1].parent = -1;
	info[1].depth = 0;
	dfs(1, 0);
}

int main()
{
	int N, M;
	scanf("%d", &N);
	for(int i = 1; i < N; i ++)
	{
		int vertex_1, vertex_2;
		scanf(" %d %d", &vertex_1, &vertex_2);
		set_node(vertex_1, vertex_2);
	}
	make_tree();
	scanf("%d", &M);
	for(int i = 0; i < M; i ++)
	{
		int vertex_1, vertex_2;
		scanf(" %d %d", &vertex_1, &vertex_2);
		print_common_ancestor(vertex_1, vertex_2);
	}
	// for(int i = 1; i < 16; i ++)
	// {
	// 	printf("%d parrent : %d\n", i, info[i].parent);
	// }
}
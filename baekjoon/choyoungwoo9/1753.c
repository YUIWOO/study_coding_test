#include <stdio.h>
#define parent (tmp >> 1)
#define left (tmp << 1)
#define right (tmp << 1 | 1)

int N;

typedef struct var
{
	int id;
	int distance;
}	var;

var heap[400001];
int count = 0;

void swap(int index_a, int index_b)
{
	int tmp;
	tmp = heap[index_a].distance;
	heap[index_a].distance = heap[index_b].distance;
	heap[index_b].distance = tmp;
	tmp = heap[index_a].id;
	heap[index_a].id = heap[index_b].id;
	heap[index_b].id = tmp;
}

void push(int num, int id)
{
	count ++;
	heap[count].distance = num;
	heap[count].id = id;
	int tmp = count;
	while(tmp != 1&&heap[parent].distance < heap[tmp].distance)
	{
		swap(tmp, parent);
		tmp = parent;
	}
}

var pop()
{
	var ret;
	ret.id = -1;
	if(count == 0)
		return ret;
	ret.distance = heap[1].distance;
	ret.id = heap[1].id;
	heap[1] = heap[count];
	count --;
	int tmp = 1;
	while(1)
	{
		if(left > count)
		{
			break;
		}
		else if(right > count)
		{
			if(heap[tmp].distance < heap[left].distance)
			{
				swap(tmp, left);
				tmp = left;
			}
			else
				break;
		}
		else
		{
			int max;
			if(heap[left].distance < heap[right].distance)
				max = right;
			else
				max = left;
			if(heap[tmp].distance < heap[max].distance)
			{
				swap(tmp, max);
				tmp = max;
			}
			else
				break;
		}
	}
	return ret;
}

#define INF 1000000000

int V, E;

typedef struct pointer
{
	int dest_id;
	int weight;
	struct pointer *next;
}	pointer;

pointer pointer_pool[300000];
pointer vertex_ar[20001];
int pool_count = 0;
pointer *get_pointer(int dest_id, int weight)
{
	pointer_pool[pool_count].dest_id = dest_id;
	pointer_pool[pool_count].weight = weight;
	pointer_pool[pool_count].next = NULL;
	return &pointer_pool[pool_count ++];
}

int distance[20001];

void dijkstra(int start_node)
{
	push(0, start_node);
	while(1)
	{
		var select_info = pop();
		if(select_info.id == -1)
			break;
		if(select_info.distance > distance[select_info.id])
			continue;
		distance[select_info.id] = select_info.distance;
		pointer *tmp = vertex_ar[select_info.id].next;
		while(tmp)
		{
			int tmp_dest_id = tmp->dest_id;
			int tmp_dest_distance = distance[select_info.id] + tmp->weight;
			if(distance[tmp_dest_id] > tmp_dest_distance)
			{
				push(tmp_dest_distance, tmp_dest_id);
			}
			tmp = tmp->next;
		}		
	}
}

pointer vertex_ar[20001];

int main()
{
	scanf("%d %d", &V, &E);
	int start_node;
	scanf("%d", &start_node);
	for(int i = 0; i < E; i ++)
	{
		int node1, node2, weight;
		scanf("%d %d %d", &node1, &node2, &weight);
		pointer *start_tmp = vertex_ar[node1].next;
		int break_flag = 0;
		while(start_tmp)
		{
			if(start_tmp->dest_id == node2)
			{
				if(start_tmp->weight >= weight)
				{
					start_tmp->weight = weight;
					break_flag = 1;
				}
			}
			start_tmp = start_tmp->next;
		}
		if(break_flag)
			continue;
		pointer *tmp_pointer = get_pointer(node2, weight);
		tmp_pointer->next = vertex_ar[node1].next;
		vertex_ar[node1].next = tmp_pointer;
	}
	for(int i = 1; i <= V; i ++)
		distance[i] = INF;
	dijkstra(start_node);
	for(int i = 1; i <= V; i ++)
	{
		if(distance[i] == INF)
			printf("INF\n");
		else
			printf("%d\n", distance[i]);
	}
}
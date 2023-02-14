#include <stdio.h>
#define parent (tmp >> 1)
#define left (tmp << 1)
#define right (tmp << 1 | 1)

int N;

unsigned int heap[100001];
int count = 0;

void swap(int index_a, int index_b)
{
	unsigned int tmp;
	tmp = heap[index_a];
	heap[index_a] = heap[index_b];
	heap[index_b] = tmp;
}

void push(unsigned int num)
{
	count ++;
	heap[count] = num;
	int tmp = count;
	while(tmp != 1&&heap[parent] < heap[tmp])
	{
		swap(tmp, parent);
		tmp = parent;
	}
}

unsigned int pop()
{
	if(count == 0)
		return 0;
	unsigned int ret = heap[1];
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
			if(heap[tmp] < heap[left])
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
			if(heap[left] < heap[right])
				max = right;
			else
				max = left;
			if(heap[tmp] < heap[max])
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

int main()
{
	scanf("%d", &N);
	for(int i = 0; i < N; i ++)
	{
		unsigned int num;
		scanf(" %u", &num);
		if(!num)
			printf("%d\n", pop());
		else
			push(num);
	}
}
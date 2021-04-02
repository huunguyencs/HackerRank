#include <stdio.h>
#include <stdlib.h>
#include <math.h>

struct triangle
{
	int a;
	int b;
	int c;
};

typedef struct triangle triangle;

double area2(triangle tr){
    double p = (tr.a + tr.b + tr.c);
    return p*(p-2*tr.a)*(p-2*tr.b)*(p-2*tr.c);
}
int compare(const void* a, const void* b)
{
    return area2(*(triangle*)a) - area2(*(triangle*)b);
}

void sort_by_area(triangle* tr, int n) {
    /**
    * Sort an array a of the length n
    */
    qsort(tr, n, sizeof(triangle), compare);
}
int main()
{
	int n;
	scanf("%d", &n);
	triangle *tr = malloc(n * sizeof(triangle));
	for (int i = 0; i < n; i++) {
		scanf("%d%d%d", &tr[i].a, &tr[i].b, &tr[i].c);
	}
	sort_by_area(tr, n);
	for (int i = 0; i < n; i++) {
		printf("%d %d %d\n", tr[i].a, tr[i].b, tr[i].c);
	}
	return 0;
}
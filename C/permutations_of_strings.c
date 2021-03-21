// Link: https://www.hackerrank.com/challenges/permutations-of-strings/problem

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void reverse(char** s, int f, int n){
	for(int low = f, high = n - 1; low < high; low++,high--){
		char* tmp = s[low];
		s[low] = s[high];
		s[high] = tmp;
	}
}

int next_permutation(int n, char **s)
{
	/**
	* Complete this method
	* Return 0 when there is no next permutation and 1 otherwise
	* Modify array s to its next permutation
	*/
    int k = n - 2;
	while(k >=0 && strcmp(s[k],s[k + 1]) >= 0){
		k--;
	}
	if(k < 0 || strcmp(s[k], s[k+1]) >= 0) return 0;
	int l = n - 1;
	while(strcmp(s[k], s[l]) >= 0){
		l--;
	}
	char* tmp = s[k];
	s[k] = s[l];
	s[l] = tmp;
	reverse(s, k + 1, n);
	return 1;
}



int main()
{
	char **s;
	int n;
	scanf("%d", &n);
	s = calloc(n, sizeof(char*));
	for (int i = 0; i < n; i++)
	{
		s[i] = calloc(11, sizeof(char));
		scanf("%s", s[i]);
	}
	do
	{
		for (int i = 0; i < n; i++)
			printf("%s%c", s[i], i == n - 1 ? '\n' : ' ');
	} while (next_permutation(n, s));
	for (int i = 0; i < n; i++)
		free(s[i]);
	free(s);
	return 0;
}
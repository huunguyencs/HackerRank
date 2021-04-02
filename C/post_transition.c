// Link: https://www.hackerrank.com/challenges/post-transition/problem

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define MAX_STRING_LENGTH 6

struct package
{
	char* id;
	int weight;
};

typedef struct package package;

struct post_office
{
	int min_weight;
	int max_weight;
	package* packages;
	int packages_count;
};

typedef struct post_office post_office;

struct town
{
	char* name;
	post_office* offices;
	int offices_count;
};

typedef struct town town;



void print_all_packages(town t) {
	printf("%s:\n", t.name);
	for(int i = 0; i < t.offices_count; i++){
		printf("\t%d:\n", i);
		post_office curr_office = t.offices[i];
		for(int j = 0; j < curr_office.packages_count; j++){
			printf("\t\t%s\n", curr_office.packages[j].id);
		}
	}
}

void send_all_acceptable_packages(town* source, int source_office_index, town* target, int target_office_index) {
	post_office* sourceOffice = &(source->offices[source_office_index]);
	package* sourceList = sourceOffice->packages;
	post_office* targetOffice = &(target->offices[target_office_index]);
	package* targetList = targetOffice->packages;
	int maxWeight = targetOffice->max_weight;
	int minWeight = targetOffice->min_weight;

	package* returnSource = malloc(sizeof(package));
	int countReturn = 0;
	for(int i = 0; i < sourceOffice->packages_count; i++){
		package curr = sourceList[i];
		if(curr.weight >= minWeight && curr.weight <= maxWeight){
			targetList = realloc(targetList, sizeof(package)*(targetOffice->packages_count + 1));
			targetList[targetOffice->packages_count] = curr;
			targetOffice->packages_count++;
		}
		else{
			countReturn++;
			returnSource = realloc(returnSource, sizeof(package)*(countReturn));
			returnSource[countReturn - 1] = curr;
		}
	}

	target->offices[target_office_index].packages = targetList;

	sourceOffice->packages_count = countReturn;
	free(sourceList);
	source->offices[source_office_index].packages = returnSource;


}

town town_with_most_packages(town* towns, int towns_count) {
	int maxPackage = 0;
	int indexMaxPackage = -1;
	for(int i = 0; i < towns_count; i++){
		int currNumPackage = 0;
		town currTown = towns[i];
		for(int j = 0; j < currTown.offices_count; j++){
			currNumPackage += currTown.offices[j].packages_count;
		}

		if(currNumPackage > maxPackage){
			maxPackage = currNumPackage;
			indexMaxPackage = i;
		}
	}
	return towns[indexMaxPackage];
}

town* find_town(town* towns, int towns_count, char* name) {
	for(int i = 0; i < towns_count; i++){
		if(strcmp(name, towns[i].name) == 0){
			return &towns[i];
		}
	}
}

int main()
{
	int towns_count;
	scanf("%d", &towns_count);
	town* towns = malloc(sizeof(town)*towns_count);
	for (int i = 0; i < towns_count; i++) {
		towns[i].name = malloc(sizeof(char) * MAX_STRING_LENGTH);
		scanf("%s", towns[i].name);
		scanf("%d", &towns[i].offices_count);
		towns[i].offices = malloc(sizeof(post_office)*towns[i].offices_count);
		for (int j = 0; j < towns[i].offices_count; j++) {
			scanf("%d%d%d", &towns[i].offices[j].packages_count, &towns[i].offices[j].min_weight, &towns[i].offices[j].max_weight);
			towns[i].offices[j].packages = malloc(sizeof(package)*towns[i].offices[j].packages_count);
			for (int k = 0; k < towns[i].offices[j].packages_count; k++) {
				towns[i].offices[j].packages[k].id = malloc(sizeof(char) * MAX_STRING_LENGTH);
				scanf("%s", towns[i].offices[j].packages[k].id);
				scanf("%d", &towns[i].offices[j].packages[k].weight);
			}
		}
	}
	int queries;
	scanf("%d", &queries);
	char town_name[MAX_STRING_LENGTH];
	while (queries--) {
		int type;
		scanf("%d", &type);
		switch (type) {
		case 1:
			scanf("%s", town_name);
			town* t = find_town(towns, towns_count, town_name);
			print_all_packages(*t);
			break;
		case 2:
			scanf("%s", town_name);
			town* source = find_town(towns, towns_count, town_name);
			int source_index;
			scanf("%d", &source_index);
			scanf("%s", town_name);
			town* target = find_town(towns, towns_count, town_name);
			int target_index;
			scanf("%d", &target_index);
			send_all_acceptable_packages(source, source_index, target, target_index);
			break;
		case 3:
			printf("Town with the most number of packages is %s\n", town_with_most_packages(towns, towns_count).name);
			break;
		}
	}
	return 0;
}
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define FLAGFILE "flag.txt"

void mania(void)
{
	puts("WELCOME TO THE RING!");
	
	char flag[40];
	FILE *fp = fopen(FLAGFILE, "r");
	
	if (fp == NULL)
	{
		perror(FLAGFILE);
		return;
	}
	
	fgets(flag, sizeof(flag), fp);
	fclose(fp);
	
	printf("%s\n", flag);
}

void welcome(void)
{
	char key[10];
	puts("Welcome to WrestleMania! Type in key to get access.");
	printf("addr of welcome(): %p\n", welcome);
	scanf("%s", key); // Unbounded SCANF(3)
}

int main(void)
{
	welcome();
	puts("Sadly, as a result Captn Overflow won't be entering the ring yet...");
	return 0;
}

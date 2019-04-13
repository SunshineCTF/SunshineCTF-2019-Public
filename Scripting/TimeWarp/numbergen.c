// James Simmons
// 3/21/2019
// Number factory for "Time Warp" CTF challenge solution for SunshineCTF 2019
// Since the chall is written in C, I figured I had to use C to create the numbers,
// because each language seeds its generators differently even with the same seed.

#include <stdio.h>
#include <stdlib.h>

int main(void)
{
	srand(301570435);
	while(!feof(stdout)) {
		printf("%d\n", rand() % 1000);
	}
	return 0;
}

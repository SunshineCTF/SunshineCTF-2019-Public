#include <stdio.h>
#include <stdlib.h>

// Access code: sun{Hu1k4MaN1a-ruNs-W1l4-0n-U}
/*
Shifted s by 5: 3680
Shifted u by 3: 936
Shifted n by 6: 7040
Shifted { by 5: 3936
Shifted H by 2: 288
Shifted u by 5: 3744
Shifted 1 by 3: 392
Shifted k by 3: 856
Shifted 4 by 3: 416
Shifted M by 5: 2464
Shifted a by 2: 388
Shifted N by 4: 1248
Shifted 1 by 6: 3136
Shifted a by 5: 3104
Shifted - by 5: 1440
Shifted r by 2: 456
Shifted u by 2: 468
Shifted N by 5: 2496
Shifted s by 2: 460
Shifted - by 6: 2880
Shifted W by 5: 2784
Shifted 1 by 1: 98
Shifted l by 3: 864
Shifted 4 by 4: 832
Shifted - by 5: 1440
Shifted 0 by 3: 384
Shifted n by 4: 1760
Shifted - by 6: 2880
Shifted U by 6: 5440
Shifted } by 5: 4000

*/

// This function recreates the seed array into the m_seed array with a for loop
void process(char* code, int* seed, int** m_seed) {
	int i = 0;

	(*m_seed) = malloc(sizeof(int) * 30);

	for(i = 0; i < 30; i++) {
		(*m_seed)[i] = 0;
	}

	for(i = 0; i < 30; i++) {
		while(seed[i] != 0) {
			(*m_seed)[i]++;
			seed[i]--;
		}
	}
}

// does nothing of importance
int verify(char* code) {
	int i = 0;
	int j = 5;
	int k = 25;

	while(k != 0) {

		if(code[i] == '-') {
			j = j & 3;
		}
		i++;
		k--;
	}

	if (j == 92) {
		return 0;
	}
	else {
		return 1;
	}
}

// bit shifts the input by given bit shift amount and saves into m_seed
void format(char* code, int** m_seed) {
	int i = 0;
	int* n_seed;

	n_seed = malloc(sizeof(int) * 30);

	for(i = 0; i < 30; i++) {
		(*m_seed)[i] = code[i] << (*m_seed)[i];
	}

	free(n_seed);
}

void prepare(char* code, int** m_seed) {
	int i = 0;
	FILE* fp = fopen("/dev/null", "w");

	for(i = 0; i < 30; i++) {
		switch(code[i]) {
			case 's':
				fprintf(fp, "%s", "Try");
				break;
			case 'u':
				fprintf(fp, "%s", "harder");
				break;
			case 'n':
				fprintf(fp, "%s", "comrade");
				break;
			case '{':
				fprintf(fp, "%s", "you're");
				break;
			case '}':
				fprintf(fp, "%s", "almost");
				break;
			default :
				fprintf(fp, "%s", "there");
				break; 
		}
	}
}

// compares input with correct values
int checkResult(int* m_seed) {
	int i;
	int resArr[30] = {3680, 936, 7040, 3936, 288, 3744, 392, 856, 416, 2464, 388, 1248, 3136, 3104, 1440, 456, 468, 2496, 460, 2880, 2784, 98, 864, 832, 1440, 384, 1760, 2880, 5440, 4000};

	// compare each element
	for(i = 0; i < 30; i++) {
		if (resArr[i] != m_seed[i]) {
			return 0;
		}
	}
	return 1;

}

int checkAccessCode(char* code) {
	int access = 0;
	int seed[30];
	int* m_seed;
	int* res;

	// set up right bit-shift amounts
	seed[0] = 5;
	seed[1] = 3;
	seed[2] = 6;
	seed[3] = 5;
	seed[4] = 2;
	seed[5] = 5;
	seed[6] = 3;
	seed[7] = 3;
	seed[8] = 3;
	seed[9] = 5;
	seed[10] = 2;
	seed[11] = 4;
	seed[12] = 6;
	seed[13] = 5;
	seed[14] = 5;
	seed[15] = 2;
	seed[16] = 2;
	seed[17] = 5;
	seed[18] = 2;
	seed[19] = 6;
	seed[20] = 5;
	seed[21] = 1;
	seed[22] = 3;
	seed[23] = 4;
	seed[24] = 5;
	seed[25] = 3;
	seed[26] = 4;
	seed[27] = 6;
	seed[28] = 6;
	seed[29] = 5;

	// does nothing
	process(code, seed, &m_seed);

	// does nothing
	prepare(code, &m_seed);

	// does nothing
	access = verify(code);

	format(code, &m_seed);

	if (checkResult(m_seed) == 1)
		return 1;
	else
		return 0;
}

int main(int argc, char* argv[]) {
	char buffer[31];
	int i;

	printf("WRESTLE-O-MANIA! We bring your wrestling bets to the internet.\n");
	printf("All rights reserved, 1991.\n");
	printf("Beginning your installation");
	fflush(stdout);

	for(i = 0; i < 5; i++) {
		printf(".");
		fflush(stdout);
		//sleep(1);
	}

	printf("\n\nPlease enter your access code: ");
	if(fgets(buffer, 31, stdin) != NULL){
		if(checkAccessCode(buffer) == 1){
			printf("Thank you for registering!\n");
		}
		else {
			printf("ERROR: Access code invalid.\n");
		}
	}
	else {
		printf("ERROR: Access code not recognized.\n");
		return -1;
	}

}



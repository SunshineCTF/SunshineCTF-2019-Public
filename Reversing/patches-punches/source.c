/* 
 * Patches' Punches
 * Basic binary patching / debugging challenge
 *
 * Spring 2019
 */

#include <stdio.h>

int array[32] = {7, 4, 3, 1, 4, 6, 3, 8, 9, 10, 11, 12, 13, 14, 15, 16, 1, 1, 1, 2, 2, 2, 3, 4, 5, 2,5,2,2,2,2,2};
char string[] = "zyq|Xu3Px~_{Uo}TmfUq2E3piVtJ2nf!}";

int main(void){

	int x = 1;

	if(x == 0)
    {
		for(int i = 0;i < 31; i++)
        {
			string[i] = string[i] - array[i];
		}
		printf("Hurray the flag is %s\n", string);
	}
    else
    {
		printf("Woah there! you jumped over the flag.");
	}
}

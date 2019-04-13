/* 
 * generate_pcap.c
 * Generates a challenge pcap for Sonar
 * Alexander Cote 
 * 10/29/2018
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char** argv)
{
	FILE *f = fopen(argv[1],"r");
	if(f==NULL){
		puts("please give me a file. thanks bye");
		return 0;
	}
	
	// working is the charecter we are working on right now
	int working =1;
	// base command is the command including everything besides the size
	static char basecommand[]="ping www.rohwrestling.com -c 5 -s ";
	char runcommand[100];
	char number[256];
	for(;working!=EOF;working=getc(f)){
		//loop intill we hit the end of file
		working+=8;
		//the ping command lies and needs to offset the  char by 8  for it to match up
		sprintf(number,"%i",working);
		//make a string that contains the charecter we will be sending  in number form
		strcpy(runcommand,basecommand);
		//make a temp command string
		strcat(runcommand,number);
		//cat the 2 strings 

		//run the command
		system(runcommand);
		system("sleep 5");
	}
	return 0;
}

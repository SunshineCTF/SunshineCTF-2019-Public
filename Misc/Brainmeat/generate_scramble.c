/***************************************
 * Alexander Cote
 * Spring 2019
 * C Program to "shuffle" alphanumerics
 * into a brainfuck source file.
 **************************************/

// These are the two multiples (modulos)
// used to choosing random characters from
// the RANDOM_FILE
#define FIRST_MULTIPLE 30
#define SECOND_MULTIPLE 3

#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[]) {

    if(argc < 3)
    {
        printf("Usage: %s BRAINFUCK_SOURCE RANDOM_FILE\n", argv[0]);
        return 1;
    }

    // Read in Files and ensure they exist
    FILE *brainfuck= fopen(argv[1],"r");
    if(brainfuck == NULL)
    {
        printf("Brainfuck file not found. Problem...\n");
        return 1;
    }

    FILE *random_file= fopen(argv[2],"r");
    if(random_file == NULL)
    {
        printf("Random file not found. Problem...\n");
        return 1;
    }

    char current;
    int rand;
    srand(28282882);  // Seeding Random

    // Iterate through the random file and scramble
    // it into the brainfuck source file.
    while(current!=EOF)
    {
        rand = random();

        if ((rand % FIRST_MULTIPLE) == 0)
        {
            current = fgetc(brainfuck);

            while(current == EOF || current == '\n')
            {
                if(current == EOF){
                    return 0;
                }
                current = fgetc(brainfuck);
            }

            printf("%c", current);
        }

        else if ((rand % SECOND_MULTIPLE) == 0)
        {
            current = fgetc(brainfuck);

            while(current == EOF || current == '\n')
            {
                if(current == EOF){
                    return 0;
                }
                current = fgetc(brainfuck);
            }

            printf("%c", current);
        }
    }
    printf("\n");
    return 0;
}

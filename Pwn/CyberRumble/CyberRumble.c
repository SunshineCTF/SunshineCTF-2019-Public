#include <stddef.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#include <sys/mman.h>
#include <stdarg.h>
#include <unistd.h>


#define HAS_PREFIX(string, prefix) (strncmp((string), (prefix), sizeof(prefix) - 1) == 0)

// The UNDERTAKER_DEBUG environment variable is not expected to ever be set.
// As such, this is just a convenient way to embed hint strings in the program.
static void debug_printf(const char* format, ...) {
    const char* debug = getenv("UNDERTAKER_DEBUG");
    if(debug) {
        va_list ap;
        va_start(ap, format);
        vprintf(format, ap);
        va_end(ap);
    }
}

static void input_line(char* buffer, size_t buffer_size) {
    char line[100];
    if(!fgets(line, sizeof(line), stdin)) {
        abort();
    }
    
    // Trim off trailing newline
    char* end = strchr(line, '\n');
    if(end) {
        *end = '\0';
    }
    
    // Copy input string w/o newline to buffer (this is safe)
    strcpy(buffer, line);
}


static void do_chokeslam(const char* args) {
    printf("Undertaker C2 v0.0.1\n");
}

static void do_tombstone_piledriver(const char* args) {
    FILE* fp = fopen(args, "r");
    if(!fp) {
        printf("Failed to open file '%s'\n", args);
        abort();
    }
    
    char buffer[100] = {};
    
    // Using scanf() with %s will read until the first whitespace. The flag.txt
    // file strategically has a space early on to prevent reading the entire flag
    // with this function.
    if(fscanf(fp, "%99s", buffer) != 1) {
        printf("Reading from file failed!\n");
        abort();
    }
    
    fclose(fp);
    
    debug_printf("TODO: why does this only show the first word in the file?\n");
    printf("File contents: '%s'\n", buffer);
}

static void do_old_school(const char* args) {
    size_t args_len = strlen(args);
    if(!args_len) {
        printf("No shellcode given.\n");
        abort();
    }
    
    void* map = mmap(NULL, args_len, PROT_READ | PROT_WRITE, MAP_ANONYMOUS | MAP_PRIVATE, -1, 0);
    if(map == MAP_FAILED) {
        abort();
    }
    
    // Copy "shellcode" into place
    memcpy(map, args, args_len);
    
    // Intentionally change permissions to read-only instead of read + execute
    debug_printf("TODO: what's the flag for making memory executable?\n");
    mprotect(map, args_len, PROT_READ);
    
    printf("Shellcode written to %p.\n", map);
    printf("Jump to shellcode?\n[y/n] ");
    
    char choice[4];
    input_line(choice, sizeof(choice));
    
    if(tolower(choice[0]) == 'y') {
        // This will crash because read-only memory is jumped to
        void (*fp)(void);
        memcpy(&fp, &map, sizeof(fp));
        fp();
        abort();
    }
    else if(tolower(choice[0]) == 'n') {
        // This is a trap, it will unmap the memory. The player should pick a character other than y/n
        // to leak the memory and leave it mapped. They can then use this memory as the command to run.
        munmap(map, args_len);
    }
}

static void do_last_ride(const char* args) {
    size_t args_len = strlen(args);
    if(args_len >= 20) {
        printf("Shell command too long!\n");
        abort();
    }
    
    // Intentionally leaked
    char* command = malloc(20);
    if(!command) {
        abort();
    }
    
    debug_printf("TODO: why does the shell command not work? i wish i knew pointers better...\n");
    
    // Intentionally copy the first <pointer-size> bytes from args to the command pointer.
    // The player will have to place a real command at a known address to use this properly.
    // ASLR is enabled, so they will need to leak some address.
    memcpy(&command, args, 20);
    system(command);
    abort();
}


int main(void) {
    char line[100];
    
    debug_printf("TODO: fix the bugs and test this code more to make sure it works...\n");
    
    printf("Undertaker Ready\n");
    
    do {
        printf("Move?\n> ");
        input_line(line, sizeof(line));
        
        if(HAS_PREFIX(line, "chokeslam ")) {
            // Just prints the version number
            do_chokeslam(line + strlen("chokeslam "));
        }
        else if(HAS_PREFIX(line, "tombstone_piledriver ")) {
            // Reads a file but with an important bug: only reads up until the first whitespace character
            do_tombstone_piledriver(line + strlen("tombstone_piledriver "));
        }
        else if(HAS_PREFIX(line, "old_school ")) {
            // Maps and reads shellcode but doesn't set it to executable
            do_old_school(line + strlen("old_school "));
        }
        else if(HAS_PREFIX(line, "last_ride ")) {
            // Reads a shell command but accidentally copies the bytes over the char pointer
            do_last_ride(line + strlen("last_ride "));
        }
        else if(strcmp(line, "i_am_a_hacker_just_give_me_the_flag") == 0) {
            // The flag is actually in "flag.txt", not "flag".
            // This is mainly to troll players but also gives a hint.
            system("cat flag");
            abort();
        }
        else {
            printf("Hey, that's an illegal move! You're disqualified!\n");
            abort();
        }
    } while(strcmp(line, "forfeit"));
    
    return 0;
}

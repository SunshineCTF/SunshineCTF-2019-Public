# [Pwn 200] CyberRumble

Overwriting a pointer with a known address containing a shell command to run with `system()`.

## How It Works

There are various functions that seem to the player like they should work to do things like read a file from disk, allocate some shellcode and run it, or run a shell command with `system()`. However, each of these commands has a major flaw that prevent them from working as intended. The player needs to figure out a way to chain the flawed functionality of these commands in a way that allows them to get proper code execution. The intended solution is as follows:

1. Use the `old_school` command to map some memory with controlled contents and learn its location.
2. When asked whether to jump to the shellcode y/n, the player should answer with a character other than y/n, such as x. This will avoid unmapping the memory or jumping there, which would crash as the memory isn't marked as executable.
3. Depending on whether there are embedded NUL bytes in the memory address, the player may need to use one or more `chokeslam` commands that don't do anything just to place controlled bytes in the command string after the NUL(s).
4. Use the `last_ride` command with an argument string consisting of bytes that represent the memory address of the mapped region.

## Deployment

PwnableHarness

## Maintenance

PwnableHarness

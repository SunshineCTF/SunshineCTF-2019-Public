# Brainmeat

*Author*: Alexander Cote

## Deploy

No extra deployment is necessary. Just upload `brainmeat.txt`.

## How to build (Not necessary for deployment)

1. Compile `generate_scramble.c`. `generate_scramble.c` is a C file made to scramble brainfuck code in with a file of random alphanumerics.
2. Run the compiled program with the brainfuck code and a file containing random alphanumerics. Scrambled code will be printed to `stdout`.

## Solution

Use `grep(1)` to remove all alphanumerics `[a-zA-Z0-9]`. That will leave you with a brainfuck-compatible file. Use a brainfuck interpreter to run it and the result is the flag.

## Note

Brainfuck interpreter comes from [here](https://github.com/fabianishere/brainfuck). It is included as a submodule of the repository and is build inside of the `solve.sh` script.

## Description

Just some brainfuck hidden in some alphanumeric text. Remove the alphanumeric text and you have runnable brainfuck that will spit you out a flag.

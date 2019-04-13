#!/bin/bash

#######################################################################
## Compiles Brainfuck interpreter and runs it against `brainmeat.txt` #
#######################################################################

## Clone the brainfuck repository
git clone https://github.com/fabianishere/brainfuck.git

## Compile BRAINFUCK
cd ./brainfuck
rm -rf build
mkdir build
cd build

cmake .. >/dev/null
make >/dev/null

cp ./brainfuck ../../brainfuck-cli
rm -rf ../brainfuck
cd ../../

## Grep the brainfuck code
grep -e "[^a-zA-Z0-9]" brainmeat.txt -o | tr -d "\n" | ./brainfuck-cli
rm ./brainfuck-cli

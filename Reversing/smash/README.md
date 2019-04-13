# Smash - 000

## Explanation

This challenge contains a main function and 6 helper functions that "analyze" a given access code to match it to the correct access code.
The program bit shifts each character a predetermined amount of times and compares the result to an array of predetermined number it should equal.

### main():
	1. Prints out strings that set the theme
	2. Asks user for access code and receives input
	3. Passes input to checkAccessCode()

### checkAccessCode():
	1. Creates an array and stores the respective left bit shift that will be applied to each character
	2. Calls process()
	3. Calls two functions--prepare() and verify()--that do nothing of important, just make the challenge a bit more confusing
	4. Calls format()
	5. Calls checkResult() and returns 1 if the input is correct

### process():
	1. Takes in the seed array, which contains the bit shifts
	2. Takes in m_seed array, which contains all zeros
	3. A while loop subtracts one from the first element of the seed array and adds one to m_seed array until the element is zero. Repeated for each element.
	So, this basically switches seed with m_seed

### format(): 
	1. Allocates space for a new array, this won't be used
	2. Bit shifts each character of the input by the corresponding amount and saves into m_seed
	3. Frees the unused new array

### checkResult():
	1. Sets up integer array with predetermined values that the bit shift should make each charater equal to
	2. Compares m_seed with integer array
	3. Return 1 if input is correct, 0 otherwise


## Solution
	The goal is to figure out the link between the bit shift amounts and the array of integers.
	Enter the correct flag when asked for the access code and the program will thank you for registering.

## Build
	There is a makefile within the repository. Run `make` to build the binary.

## Deploy
	S3 upload the binary file.

## Maintenance
	None needed.


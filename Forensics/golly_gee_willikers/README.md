# [Forensics 100] Golly Gee Willikers

RLE format for Conway's Game of Life state file, edited.

## How It Works

RLE files are pretty well [documented](http://www.conwaylife.com/wiki/Run_Length_Encoded). I encoded ASCII text into the game of life as live cells and exported that from this [online game of life](https://copy.sh/life/) website as an RLE file. I then wrote a small Python script to convert an image of every character in that font into the RLE format. Taking these two RLE files, I put the flag text at the end of the font image. I then added a few empty rows in between the two and, critically, I added a single character: `!`. This character is used to mark the end of the RLE file. Everything after this character is considered a comment and is ignored.

## Intended Solution

1. Open the file, see some weird header setting variables `x`, `y`, and `rule`, along with a bunch of strange text.
2. Either already know what `B3/S23` means or Google that (maybe in combination with the text `rule`) and learn that this file has to do with Conway's Game of Life.
3. Search online for file formats for Conway's Game of Life. RLE encoding will be either first or second in the search results.
4. Try importing this file into copy.sh/life.
5. See all of ASCII text represented as living cells but no flag.
6. Determine that there must be additional data hidden in the file.
7. Read the [RLE format documentation](http://www.conwaylife.com/wiki/Run_Length_Encoded).
8. Learn that the `!` character ends the input data and everything after that is ignored.
9. Modify the file to remove the early `!` character.
10. Load the modified file into copy.sh/life.
11. Read the flag and submit it.

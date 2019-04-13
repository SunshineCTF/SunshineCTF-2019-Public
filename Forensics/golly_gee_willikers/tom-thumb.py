# Tom Thumb
# hackucf_kcolley
# SunshineCTF 2019

import sys
from PIL import Image

im = Image.open("tom-thumb.png").convert("L")

left, top, right, bottom = im.getbbox()
cell_size = 4
row_limit = 70

line_pos = 0
def write_chunk(chunk):
	global line_pos
	if line_pos + len(chunk) > row_limit:
		sys.stdout.write("\n")
		line_pos = 0
	sys.stdout.write(chunk)
	line_pos += len(chunk)

def make_rle(count, alive):
	c = "o" if alive else "b"

	if count == 0:
		return ""
	elif count == 1:
		return c
	else:
		return "%d%c" % (count, c)

def rle(count, alive):
	write_chunk(make_rle(count, alive))

def rle_endrow():
	write_chunk("$")

print("x = %d, y = %d" % (left, top))
for y in range(top, bottom, cell_size):
	row = []
	last_state = False
	last_start = left
	for x in range(left, right, cell_size):
		cell = im.getpixel((x, y)) == 0
		if cell != last_state:
			rle((x - last_start) // cell_size, last_state)
			last_state = cell
			last_start = x
	if last_state:
		rle((right - last_start) // cell_size, last_state)
	rle_endrow()
print("")

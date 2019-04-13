#The code I used to encode the bitstring into the image
from PIL import Image

filename = 'BigBad'
extension = '.bmp'

def main():
	im = Image.open(filename + extension)

	sequence = "000 0010 10010 11010 000 10011 010 0010 10100 0110 10101 0011 0010 1000 10110 0110 0011 10111 11100 1100 11101 11110 000 0011 1100 010 010 1100 1100 11111 010 1000 1100 0111 11011"
	#            s    u    n    {     s    h    0   u    l     d     a    _    u     5    e     d    _   b      r    1      c    k    s   _    1   0    0    1    1    3   0    5    1     9    }
	sequence = sequence.replace(" ", "")
	print(sequence)

	width, height = im.size

	for j in range(height):
		for i in range(len(sequence)):

			r, g, b = im.load()[i, j]
			r = r - (r % 2)
			g = g - (g % 2)
			b = b - (b % 2)

			if sequence[i] == "1":
				im.load()[i, j] = (r+1, g+1, b+1)
			else:
				im.load()[i, j] = (r, g, b)

	im.save('attachments/' + filename + '.png')
	del im

def test():
	im = Image.open(filename + extension)
	width, height = im.size
	for x in range(height):
		im.load()[x, x] =  (0, 0, 0)
	im.save("test" + extension)
	del im

main()

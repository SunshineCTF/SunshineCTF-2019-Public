# This only retrieves the sequence. You still have to go through the tree
# either by hand, or copy it into some digital tree structue to get the flag
from PIL import Image

class node:
	def __init__(self, ch=""):
		self.left = None
		self.right = None
		self.ch = ch
		if ch == "":
			self.isLeaf = 0
		else:
			self.isLeaf = 1

	def printSequence(self, sequence):
		temp = self
		output = ""

		for ch in sequence:
			if ch == "0":
				temp = temp.left
			elif ch == "1":
				temp = temp.right
			else:
				print("Nonbinary sequence in printSequence()")

			if temp.isLeaf == 1:
				output += temp.ch
				temp = self

		return output

	def insert(self, sequence, character):
		temp = self
		for i in range(len(sequence)):
			if sequence[i] == "0":
				if i == len(sequence) - 1:
					if temp.left == None:
						temp.left = node(character)
					else:
						print("Attempted Overwrite in insert()")
				else:
					if temp.left == None:
						temp.left = node()
					temp = temp.left
			elif sequence[i] == "1":
				if i == len(sequence) - 1:
					if temp.right == None:
						temp.right = node(character)
				else:
					if temp.right == None:
						temp.right = node()
					temp = temp.right

def getSequence():
	filename = 'attachments/BigBad'
	extension = '.png'

	im = Image.open(filename + extension)
	sequence = ""

	for i in range(200):
		r, g, b = im.load()[i, i]
		sequence += str(r % 2)

	return sequence

def buildTree():
	root = node()
	root.insert("000", "s")
	root.insert("0010", "u")
	root.insert("0011", "_")
	root.insert("010", "0")
	root.insert("0110", "d")
	root.insert("0111", "9")
	root.insert("1000", "5")
	root.insert("10010", "n")
	root.insert("10011", "h")
	root.insert("10100", "l")
	root.insert("10101", "a")
	root.insert("10110", "e")
	root.insert("10111", "b")
	root.insert("1100", "1")
	root.insert("11010", "{")
	root.insert("11011", "}")
	root.insert("11100", "r")
	root.insert("11101", "c")
	root.insert("11110", "k")
	root.insert("11111", "3")

	return root


def main():
	root = buildTree()
	sequence = getSequence()
	flag = root.printSequence(sequence)
	print(flag)

main()

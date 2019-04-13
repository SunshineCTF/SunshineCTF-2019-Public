import sys

for line in sys.argv:
   if line=="solve.py":
       print(line)
   else:
        line=int(line)
        line=line-50
        print(chr(line))

exit()

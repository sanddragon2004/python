#this file opens a file called f.txt and prints the contents in a loop (multiple lines)

from sys import argv

#creates a var called bj, opens a file and defines contents of file to bj
bj = open("f.xt","r")

#for loop prints out contents of each line in the var bj
for line in bj:
  print "alot of stuff in this file %s" % bj

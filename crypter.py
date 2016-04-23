import crypt
import sys

try:
	hasha = sys.argv[1]
	wordlist = sys.argv[2]
except:
	print "Usage: python %s [hash] [wordlist]"%(sys.argv[0])
	sys.exit()

words = open(wordlist).readlines()

for word in words:
	word = word.strip()
	hashb = crypt.crypt(word,hasha)
	
	if hashb == hasha:
		print "Found: %s = %s"%(hasha, word)
		break
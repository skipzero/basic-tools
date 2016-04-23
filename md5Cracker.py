import hashlib
import sys

try:
	h = sys.argv[1]
	wordlist = sys.argv[2]
except:
	print "Usage: python %s [hash] [wordlist]" %(sys.argv[0])
	sys.exit()

words = open(wordlist).readlines()


for word in words:
	word = word.strip()
	ha = hashlib.md5(word).hexdigest()
	
	if ha == h:
		print "Found: %s = %s" %(h, word)
		break

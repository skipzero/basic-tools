def binTostr(binary):
	letter = binary.split(" ")
	text = ""

	for let in letter:
		c = int(let, 2)
		c = chr(c)
		text += c

	return text
	

def strTobin(string):
	text = ""
	for s in string:
		c = ord(s)
		c = bin(c)[2:]
		text += c + " "
	
	return text

	


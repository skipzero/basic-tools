from PIL import Image
import struct
import sys

try:
	cpbitmap = sys.argv[1]
	outputfile = sys.argv[2]
except:
	print "Usage: python %s test.cpbitmap output.png"%(cpbitmap)
	sys.exit()

with open(cpbitmap) as f:
    contents = f.read()


unk1, width, height, unk2, unk3, unk4 = struct.unpack('<6i', contents[-24:])
im = Image.frombytes('RGBA', (width,height), contents, 'raw', 'RGBA', 0, 1)
im.save(outputfile)

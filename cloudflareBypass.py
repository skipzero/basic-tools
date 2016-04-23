import dns.resolver as d
import socket
import sys

try:
	domain = sys.argv[1]
except:
	print "Usage: python %s domain.com"%(sys.argv[0])
	sys.exit(0)

mxRec = d.query(domain, 'MX')
mxDomain = str(mxRec[0].exchange)

ip = socket.gethostbyname(mxDomain)
print "%s : %s"%(domain, ip)
import sys

port = 8000
for i in range(len(sys.argv)):
	if sys.argv[i] == "--port":
		port = sys.argv[i+1]
		


if "static" in sys.argv:
	f = open("urls.txt",'w')
	for i in range(100,501):
		f.write("http://localhost:%s/static/images/image_%s.png\n" % (port,i))
	f.close()
else:
	f = open("urls.txt",'w')
	for i in range(1,51):
		f.write("http://localhost:%s/campaigns/%s/\n" % (port,i))
	f.close()

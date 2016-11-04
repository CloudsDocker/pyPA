wwwlog=open('weblog.debug')
bytecolumn=(line.rsplit(None,1)[1] for line in wwwlog)
bytes=(int(x) for x in bytecolumn if x!='-')
print "total:", sum(bytes)

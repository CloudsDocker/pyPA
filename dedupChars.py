# Authoer Todd Zhang @ 2016-10-08 15:19 in PuDong Library

# char_chars.txt is one sample file that contains string with duplicate chinese characters, 
import codecs

strLine=unicode(open("chn_chars.txt","r").read(),"utf-8")
preChar="-1"

# open file for write chinese characters
with codecs.open("dedup_output.txt","w","utf-8-sig") as out:

for currChar in strLine:
	if currChar != preChar:
		print currChar
		out.write(currChar)
		preChar=currChar

out.close()
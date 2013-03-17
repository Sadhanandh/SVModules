def readlist(filename):
	fp = open(filename)
	mydic = {}
	for line in fp.readlines():
		line = line.strip("\n")
		mid = line.find(":")
		if mid != -1:
			front = line[:mid].strip(" ")
			back = line[mid+1:].strip(" ")
			front = [w.capitalize() for w in front.split(" ")]
			front = "".join(front)

		if front != "":
			mydic[front.lower()]=back
	fp.close()

	return mydic

def writelist(filename,data):
	fp = open(filename,"w")
	strfull = ""
	for x,y in data.items():
		x = x.lower()
		string = str(x).capitalize() + " : " +str(y) + "\n"
		strfull+=string

	fp.write(strfull)
	fp.close()





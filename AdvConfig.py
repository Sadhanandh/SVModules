#
#	Eg usage->
#
#	 bulkconfig("test","Tag Name","","Tag Num",0,"Tag__point",0.0,raiseexcept=True)
#   or use without exception 
#
#	 bulkconfig("test","Tag Name","","Tag Num",0,"Tag__point",0.0)
#
#
#
#		All the __ is replaced to " "by default
#
#	To change the character -> use

#   bulkconfig("test","Tag Name","","Tag Num",0,"Tag___point",0.0,raiseexcept=True,delim="___")

#
#	bulkconfigwrite("onetest1","Tag___name","HelloWorld","Tag___Num",20,delim="___")
#
#
#	bulkconfigwritetest("onetest",Tag___name="HelloWorld",Tag___Num=20,delim="___")
#
#
import re
import os

settingsfile = "config.ini"

class NotFound(Exception):
	def __init__(self, value=""):
		if value!="":
			self.value = value
		else:
			self.value="Tag not found in the given file."
	def __str__(self):
		return repr(self.value)

class ArgError(Exception):
	def __str__(self):
		return "Arguments arn't  correct. Please check the docs."

def configreader(settingsfile,tagname,tagformat,tagre=r"",istagformat=True,isfile=False,raiseexcept=False):

	if tagre !=r"":
		iscustom =True
	else:
		iscustom = False


	if isfile == True:
		if os.path.isfile(settingsfile):
			fr = open(settingsfile)
			data = fr.read()
			fr.close()
	else:
		data = settingsfile

	if not iscustom:
		if tagformat is int or tagformat is long:
			tagre = "(\d*)"
		elif tagformat is float:
			tagre = "([\d.]*)"
		elif tagformat is str:
			tagre = "(\S*)"
	else:
		pass
		#custom regexp -> dont do anything.

	tagname = r"\s*".join(tagname.split())
	ma = re.findall(tagname+"\s*:\s*"+tagre,data,re.IGNORECASE)
	if ma !=[]:
		ret_val = ma[0]
		if istagformat==True :
			if ret_val != "":
				ret_val = tagformat(ret_val)
			elif (not tagformat is str ) or ( not iscustom):
				ret_val =0
	else:
		#either exception or None
		if raiseexcept:
			raise NotFound()
		else :
			ret_val = None

	return ret_val

def bulkconfigtest(filename,**kwargs):
	ret_out = []
	delim = "__"
	if "delim" in kwargs:
		delim = kwargs["delim"]
		del(kwargs["delim"])
	fp = open(filename)
	filename = fp.read()
	fp.close()
	for x,y in kwargs.items():
		x = x.replace(delim," ")
		ret_out.append(configreader(filename,x,type(y)))
	return ret_out

def bulkconfig(filename,*args,**kwargs):
	if (len(args)%2==0):
		ret_out = []
		delim = "__"
		if "delim" in kwargs:
			delim = kwargs["delim"]

		fp = open(filename)
		filename = fp.read()
		fp.close()
		for i in range(0,len(args),2):
			x = args[i]
			x = x.replace(delim," ")
			y = args[i+1]
			if "raiseexcept" in kwargs and kwargs["raiseexcept"]==True:
				ret_out.append(configreader(filename,x,type(y),raiseexcept=True))
			else:
				ret_out.append(configreader(filename,x,type(y)))
		return ret_out
	else:
		raise ArgError()
		return None


def configwriter(settingsfile,tagname,tagvalue,isfile=False):

	tagname = [w.capitalize() for w in tagname.split(" ")]
	tagname = "".join(tagname)
	data = tagname+" : "+str(tagvalue)+"\n"

	if isfile == True:
		if os.path.isfile(settingsfile):
			fr = open(settingsfile,"a")
			fr.write(data)
			fr.close()
	else:
		settingsfile.write(data)

def bulkconfigwrite(filename,*args,**kwargs):
	if (len(args)%2==0):
		ret_out = []
		delim = "__"
		if "delim" in kwargs:
			delim = kwargs["delim"]
		filename = open(filename,'w')
		for i in range(0,len(args),2):
			x = args[i]
			x = x.replace(delim," ")
			y = args[i+1]
			ret_out.append(configwriter(filename,x,y))
		filename.close()
		return ret_out
	else:
		raise ArgError()
		return None


def bulkconfigwritetest(filename,**kwargs):
	ret_out = []
	delim = "__"
	if "delim" in kwargs:
		delim = kwargs["delim"]
		del(kwargs["delim"])
	filename = open(filename,'w')
	for x,y in kwargs.items():
		x = x.replace(delim," ")
		ret_out.append(configwriter(filename,x,y))
	filename.close()
	return ret_out

def readlist(filename):
	fp = open(filename)
	mydic = {}
	for line in fp.readlines():
		line = line.strip("\n")
		mid = line.find(":")
		if mid != -1:
			front = line[:mid].strip(" ")
			back = line[mid+1:].strip(" ")
		if front != "":
			mydic[front]=back
	fp.close()

	return mydic

import os
import Image
import win32api
import win32print

re_print_e = True
pdf_out = "x"
filename = "tiger.jpg"
res_ = 50
def printImage(filename,res_ = res_):
	if os.path.exists(filename):
		finali = Image.open(filename)
		finali.convert('RGB').save(pdf_out+".pdf", "PDF", resolution = res_)
	else :
		print "Image Doesn't exist "
	print "Done."
	print "Printing .........",
	while(not os.path.exists(pdf_out+".pdf")):
		pass
	if re_print_e:		
		try:
			win32api.ShellExecute (
			0,
			"print",
			pdf_out+".pdf",
			'/d:"%s"' % win32print.GetDefaultPrinter (),
			".",
			0
			)
			print "Done. (Sent the print job to the default printer)"
			print "(Default Printer -> "+str(win32print.GetDefaultPrinter())+" .)"
		except Exception as e:
			print e
			if True:
				print " "
				print "Trying to  Print the file in absolute path mode"
				if re_print_e:
					try:				
						win32api.ShellExecute (0, "print" , os.path.abspath(pdf_out+".pdf" ),'/d:"%s"' % win32print.GetDefaultPrinter(),".",0)
						print "Done. (Sent the print job to the default printer)"
						print "(Default Printer -> "+str(win32print.GetDefaultPrinter())+" .)"
					
					except:
						print " "
						print "Both attempts Failed. Problem with the print setup."
						print " "
	#os.remove(pdf_out+".pdf")

if __name__ == "__main__" :
	printImage(filename)

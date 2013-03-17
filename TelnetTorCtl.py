import socks
import socket
import telnetlib



__originalSocket = socket.socket
__originalCreateConnection = socket.create_connection


def create_connection(address, timeout=None, source_address=None):
	sock = socks.socksocket()
	sock.connect(address)
	return sock

def changeiptelnet(host="localhost",port=9051,passphrase=""):
	#import telnetlib
	print host ,port 
 	socket.socket = __originalSocket
	socket.create_connection = __originalCreateConnection
	tn = telnetlib.Telnet(host,port,5)
	tn.read_until("Escape character is '^]'.", 2)
	tn.write('AUTHENTICATE "'+passphrase+'"\r\n')
	resp = tn.read_until("250 OK", 2)
	if not resp.strip("\r\n") == "250 OK":
		print "error with tor Auth"
	tn.write("signal NEWNYM\r\n")
	resp = tn.read_until("250 OK", 2)
	if not resp.strip("\r\n") == "250 OK":
		print "error with tor"
	tn.write("quit\r\n")
	tn.close()
	socket.socket = socks.socksocket
	socket.create_connection = create_connection


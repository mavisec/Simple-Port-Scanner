#! /usr/bin/python

import socket

sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host= "127.0.0.1" #Enter the HOST
port= 1234		#Enter the PORT

def port_scanner(port):
	if sock.connect_ex((host,port)):
		print("The port %d is closed") % (port)

	else:
		print("The port %d is opened") % (port)

port_scanner(port)
# server

# Import socket module
from socket import *
import os
import sys

# Create a socket object
server = socket(AF_INET, SOCK_STREAM)

#max size of bytes
size = 1000

#encode type
FORMAT = "utf-8"

#set host address
host = '0.0.0.0'

#give port number
port = int(input("Provide Port number: "))

# Bind to the port
server.bind((host , port))

# Now wait for client connection.
server.listen(100)

while(True):

	print("Listening for connection at ", port)
	
	# Establish connection with client.
	client, addr = server.accept()
	
	print("Connection accepted from ", addr)
	
	#recieve file name from client
	f = client.recv(size).decode()
	getFileName = f.split(" ")
	fileName = getFileName[1]
	
	fileinfo = os.stat(fileName)
	filesize = str(fileinfo.st_size)
	
	print("Asking for file ", fileName)
	
	#client.send(filesize.encode(FORMAT))
	
	with open(fileName, "r") as file:
		data = file.read()
		print("Sending the file...")
		client.send(data.encode(FORMAT))
		
	
	#close the file
	file.close()
	
	print("Transfer Complete!")
	
	#close the server
	server.close()

	print("Connection closed, See you later!")

# server

# Import socket module
from socket import *
import sys

# Create a socket object
s = socket(AF_INET, SOCK_STREAM)

#max size of bytes
size = 1000

#set host address
host = '0.0.0.0'

#give port number
port = int(input("Provide Port number: "))

# Bind to the port
s.bind(('' , port))

# Now wait for client connection.
s.listen(100)


# Establish connection with client.
clientS, addr = s.accept()

print("Provide filename: ")
fileName = input()

with open(fileName,'rb') as file:
    s.storbinary(f"STOR {fileName}", file, size)

print("File successfully uploaded")
file.close()

print("Closing connection")
s.close()

print("Connection closed")
# server

from socket import *               # Import socket module
import sys

s = socket(AF_INET, SOCK_STREAM)             # Create a socket object
size = 1000                         #max size to be sent
print("Provide Port number: ")
port = input()

s.bind(('' , port))            # Bind to the port
s.listen(100)                     # Now wait for client connection.

clientS, addr = s.accept()     # Establish connection with client.

print("Provide filename: ")
fileName = input()

with open(fileName,'rb') as file:
    s.storbinary(f"STOR {fileName}", file, size)

print("File successfully uploaded")
file.close()

print("Closing connection")
s.close()

print("Connection closed")

# client

# Import socket module
from socket import *
import sys

# Create a socket object
client = socket(AF_INET, SOCK_STREAM)

#max size allowed
size = 1000

#encode format
FORMAT = "utf-8"

# user input for ip
ip_address = input("Provide Server IP: ")

# user input for port number
port = int(input("Provide Port number: "))

#connect to server
client.connect((ip_address, port))

user = ''

#while the user input doesn't == close
while(user != 'CLOSE'):
    user = input("You are now connected! Enter your commands now: ")
    if user != 'CLOSE':
        x = user.split(' ')
        fileName = x[1]

        #send file name to server
        client.send(user.encode(FORMAT))

        #create the file and add it's data
        with open(fileName, 'wb') as file:
            while(True):

                data = client.recv(size)

                if not data:
                    break
                else:
                    file.write(data)
                    print('Recieved ', fileName)

    else:
        break

#close the file
file.close()

#close the client connection
client.close()
print('Connection closed')
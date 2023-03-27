
# client

# Import socket module
from socket import *
import sys

# Create a socket object
s = socket(AF_INET, SOCK_STREAM)

#max size allowed
size = 1000

# user input for ip
ip_address = input("Provide Server IP: ")

# user input for port number
port = int(input("Provide Port number: "))

#connect to server
s.connect((ip_address, port))

print("You are now connected! Enter your commands now")
user = input()  
x = user.split('')
fileName = x[1]

with open(fileName, 'wb') as file:
    s.retrbinary(user, file.write, size)

s.dir()

file = open(fileName, 'r')
print("File content: ", file.read())

file.close()
print('Successfully got the file')

s.close()
print('connection closed')
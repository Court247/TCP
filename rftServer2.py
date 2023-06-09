# server - sender

# Import socket module
from socket import *
from HelperModule import packet
from HelperModule import timer
from HelperModule import udt


# Create a socket object
server = socket(AF_INET, SOCK_STREAM)

#set up the timer for the whole transmission
t = timer.Timer(10)

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

#initialize sequence number
seqNum = 0

#initialize transmitted packet counts
transCount = 0

#initialize retransmitted packet counts
reTranCount = 0

#allow for the first data packet to send
toSend = True

#set file name
fileName = "Test.txt"

print("Listening for connection at ", port)

# Establish connection with client.
client, addr = server.accept()

print("Connection accepted from ", addr)

#check if file exists
file = open(fileName, 'r')

try:
    #start the timer
    t.start()
    while t.running() and not t.timeout():
        print('0: ')
        if toSend:

            print('1: ')

            #get the file size bytes
            data = file.read(size)

            print(data)

            print('2: ')

            #make the data packet
            cPack = packet.make(seqNum, bytes(data, encoding = FORMAT))

            print('3: ')

            #send the data packet
            udt.send(cPack, client, addr)

            print('4: ')

            #set to send to false
            toSend = False

            print('5: ')

            #add transmission count
            transCount = transCount + 1

            print('6: ')


            #receive the ACK package from UDT
            rPack, rAddr = udt.recv(client)
            print('7: ')

            #extract the package
            rSeqNum, rData = packet.extract(rPack)

            print('8: ')

            #if the sequence numbers are the same then it's good to send the next packet
            if (rData == "Ack " + str(seqNum)) and rSeqNum == seqNum:

                print('9: ')

                #stop the timer
                t.stop()

                #set send to true
                toSend = True

                #increment sequence number
                seqNum = seqNum + 1
            else :
                #else it's the wrong packet and resend current packet
                print("Wrong seq number")

                print('10: ')

                #send the data packet again
                udt.send(cPack, client, addr)

                #add retransmission count
                reTranCount = reTranCount + 1

                #start the timer again
                t.start()
        
finally:
    
    if file:
        #close the file
        file.close()

    print("Transfer Complete!")
    print("Transmission:  ", transCount)
    print("Retransmission: ", reTranCount)

    #close the server
    server.close()

    print("Connection closed, See you later!")

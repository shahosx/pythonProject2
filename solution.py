#import socket
from socket import *
# In order to terminate the program
import sys


def webServer(port=13331):
    serverSocket = socket(AF_INET, SOCK_STREAM)
    # Prepare a server socket
    serverSocket.bind(('', port))
    # Fill in start
    serverSocket.listen(2)
    # Fill in end

    while True:
        # Establish the connection
        connectionSocket, addr = serverSocket.accept()# Fill in start      #Fill in end
        try:

            try:
                message = serverSocket.recv(1024).decode() # Fill in start    #Fill in end
                filename = message.split()[1]
                f = open(filename[1:])
                outputdata = f.read()# Fill in start     #Fill in end

                # Send one HTTP header line into socket.
                connectionSocket.send('HTTP/1.1 200 OK\r\n'.encode())
                # Fill in start

                # Fill in end
                connectionSocket.send(outputdata.encode())
                # Send the content of the requested file to the client
                for i in range(0, len(outputdata)):
                    connectionSocket.send(outputdata[i].encode())

                connectionSocket.send('\r\n'.encode())
                connectionSocket.close()
            except IOError:
                connectionSocket.send('HTTP/1.1 404 Not Found\r\n'.encode())
                connectionSocket.send('<html><head></head><body><h1> 404 Not Found</h1></body></html>\r\n')

        except (ConnectionResetError, BrokenPipeError):
            pass

    serverSocket.close()
    sys.exit()  # Terminate the program after sending the corresponding data


if __name__ == "__main__":
    webServer(13331)
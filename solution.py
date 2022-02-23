import socket
from socket import *
import smtplib

def smtp_client(port=1025, mailserver='127.0.0.1'):
    msg = "\r\n My message email from Shahadat Hossain"
    endmsg = "\r\n.\r\n"
    host =''
    # Choose a mail server (e.g. Google mail server) if you want to verify the script beyond GradeScope
    gmail_user= 'shahosx@gmail.com'
    gmail_Password = ''
    # Create socket called clientSocket and establish a TCP connection with mailserver and port
    clientSocket = socket(AF_INET, SOCK_DGRAM)
    clientSocket.connect(mailserver)
    # Fill in start
    # Fill in end

    recv = clientSocket.recv(1024).decode()
    #print(recv) #You can use these print statement to validate return codes from the server.

    #if recv[:3] != '220':
    #print('220 reply not received from server.')

    # Send HELO command and print server response.
    heloCommand = 'HELO Alice\r\n'
    clientSocket.send(heloCommand.encode())
    recv1 = clientSocket.recv(1024).decode()

    #print(recv1)
    #if recv1[:3] != '250':
    #print('250 reply not received from server.')

    # Send MAIL FROM command and handle server response.
    # Fill in start
    sent_from ='MAIL FROM: <shahosx@gmail.com>\r\n'
    clientSocket.send(sent_from.encode())
    recv2= clientSocket.recv(1024).decode()
    # Fill in end
    #Subject = ''
    # Send RCPT TO command and handle server response.
    email_to = 'RCPT TO: <shahosx@gmail.com>\r\n'
    clientSocket.send(email_to.encode())
    recv3= clientSocket.recv(1024).decode()

    # Fill in start

    # Fill in end


    # Send DATA command and handle server response.
    sending_data ='DATA: \r\n'
    clientSocket.send(msg.encode())
    recv4 = clientSocket.recv(1024).decode()
    # Fill in start
    # Fill in end

    # Send message data.
    # Fill in start
    # Fill in end

    # Message ends with a single period, send message end and handle server response.
    # Fill in start
    clientSocket.send(endmsg.encode())
    recv3 = clientSocket.recv(1024).decode()
    # Fill in end
    clientSocket.close()
    # Send QUIT command and handle server response.
    # Fill in start
    # Fill in end


if __name__ == '__main__':
    smtp_client(1025, '127.0.0.1')
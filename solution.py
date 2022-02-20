import socket
from socket import *
import smtplib

def smtp_client(port=1025, mailserver='smtp@gmail.com'):
    msg = "\r\n My message email from Shahadat Hossain"
    endmsg = "\r\n.\r\n"
    host =''
    # Choose a mail server (e.g. Google mail server) if you want to verify the script beyond GradeScope
    gmail_user= 'shahosx@gmail.com'
    gmail_Password = ''
    # Create socket called clientSocket and establish a TCP connection with mailserver and port
    clientSocket = socket(AF_INET, SOCK_DGRAM)
    clientSocket.bind('',port)
    # Fill in start
    # Fill in end

    recv = clientSocket.recv(1024).decode()
    #print(recv) #You can use these print statement to validate return codes from the server.
    #if recv[:3] != '220':
    #    print('220 reply not received from server.')

    # Send HELO command and print server response.
    heloCommand = 'HELO Alice\r\n'
    clientSocket.send(heloCommand.encode())
    recv1 = clientSocket.recv(1024).decode()
    #print(recv1)
    if recv1[:3] != '250':
        print('250 reply not received from server.')

    # Send MAIL FROM command and handle server response.
    # Fill in start
    sent_from =gmail_user
    FROM =[shahosx@gmail.com]
    # Fill in end
    Subject = ''
    # Send RCPT TO command and handle server response.
    # Fill in start
    send_To = 'shahadatx@gmail.com'

    # Fill in end
    clientSocket.send(msg.encode())
    # Send DATA command and handle server response.
    # Fill in start
    # Fill in end

    # Send message data.
    # Fill in start
    # Fill in end

    # Message ends with a single period, send message end and handle server response.
    # Fill in start
    clientSocket.send(endmsg.encode())
    # Fill in end

    # Send QUIT command and handle server response.
    # Fill in start
    # Fill in end


if __name__ == '__main__':
    smtp_client(1025, '127.0.0.1')
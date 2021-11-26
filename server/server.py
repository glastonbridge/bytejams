#!/usr/bin/env python3

import socket
import sys
import os

# useless defaults
serverPort = 4444
separator = "|"
UNIX_NEWLINE = '\n'
WINDOWS_NEWLINE = '\r\n'
MAC_NEWLINE = '\r'

if len(sys.argv) == 2:
    # arg[1] == port-nr. arg[0]== is python script itself
    serverPort = int(sys.argv[1])
else:
    print("\nRun like : python3 server.py server-port")
    print("running without params will start interactive config.")
    print("using a non-integer port-nr or a in-use port will crash/exit the script.\n")
    serverPort = int(input("server ip port number: "))

# todo: test input for validity!

# Create a UDP socket + Bind socket to Port; ipaddress not needed when running a server
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
try:
    s.bind(("", serverPort))
    print("\nserver started listening on Port {}\n".format(str(serverPort)))
except socket.error as msg:
    print("Error binding socket: {}".format(msg))
    exit(1)

keepRunning = bool(True)

while keepRunning:
    data, address = s.recvfrom(64*1014)

    # code from client
    # msg = showdownId + separator + filename + separator + fileData
    # utf-8 is irrelevant for sources out of TIC-80
    # datagram = data.decode('utf-8').split(separator, 2)
    datagram = data.decode('ascii').split(separator, 2)
    print("ID: {}, file: {}, len: {}".format(datagram[0], datagram[1], str(len(str(datagram[2])))))
    # print("file-content:\n{}\n".format(datagram[3]) )
    with open("./incoming/{}.lua".format(datagram[0]), "w+", newline="\n") as fileToWrite:
        fileToWrite.seek(0)
        # .replace might be redundant, since also in client, but hey
        content = str(datagram[2]).replace(WINDOWS_NEWLINE, UNIX_NEWLINE).replace(MAC_NEWLINE, UNIX_NEWLINE)
        fileToWrite.write(content)
        fileToWrite.truncate()

# unreachable
# close the socket
s.close()
exit(0)

#!/usr/bin/env python3

import os
import socket
import sys
import time

# useless defaults
serverIp = "127.0.0.1"
serverPort = 4444
intervalInMs = 20
showdownId = ""
filename = ""
separator = "|"
packet_count = int(0)

UNIX_NEWLINE = '\n'
WINDOWS_NEWLINE = '\r\n'
MAC_NEWLINE = '\r'

if len(sys.argv) == 6:
    serverIp = sys.argv[1]
    serverPort = int(sys.argv[2])
    intervalInMs = int(sys.argv[3])
    showdownId = sys.argv[4]
    filename = sys.argv[5]
else:
    print("\nRun like: python3 client.py server-ip server-port interval-in-milliseconds showdown-ID filename>")
    print("running without params will start interactive config.")
    print("invalid input will just crash/exit the script.\n\n")
    serverIp = input("server ip address: ")
    serverPort = int(input("server ip port number: "))
    intervalInMs = int(input("Interval in milliseconds: "))
    showdownId = input("Showdown ID: ")
    filename = input("your filename: ")

# todo: test input for validity

# Create socket for server
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)
print("\nclient started for server: {}:{}, interval: {}ms, ID: {}, file: {}\n"
      .format(serverIp, str(serverPort), str(intervalInMs), str(showdownId), filename))

lastModificationDate = 0.0
lastIntervalMs = time.time_ns()/1000000.0
nextIntervalMs = lastIntervalMs
lastFileContent = ""

keepRunning = bool(True)

while keepRunning:

    try:
        # check if file is modified, only check every intervalInMs
        currentModificationDate = os.path.getmtime(filename)
        hasChanged = (currentModificationDate > lastModificationDate)
        lastModificationDate = currentModificationDate

        # you know, just for good measure we'll check if the content has changed...
        # Not the most robust of ways of checking if there is a real difference
        # but there were cases when older versions of TIC-80 would continuously save at 60Hz
        if hasChanged:
            with open(filename, mode='r') as file:
                # the server also .replaces, but better to strip anything- before- sending
                fileData = file.read().replace(WINDOWS_NEWLINE, UNIX_NEWLINE).replace(MAC_NEWLINE, UNIX_NEWLINE)
            if lastFileContent == fileData:
                hasChanged = False

        # Some apps (perhaps only on Windows) will change a file.date -twice- on save
        # first to wipe the file, second to edit
        if hasChanged & (len(fileData) > 0):
            # already has content
            # file = open(filename, 'r')
            # fileData = file.read()

            # build datagram
            msg = showdownId + separator + filename + separator + fileData
            # utf-8 is irrelevant for sources out of TIC-80
            # s.sendto(msg.encode('utf-8'), (serverIp, serverPort))
            s.sendto(msg.encode('ascii'), (serverIp, serverPort))
            packet_count += 1
            print("counter:{}, ID:{}, file:{}, len:{}"
                  .format(str(packet_count), showdownId, filename, str(len(fileData))))

            # this, just to fool Windows 10 with its double fileDate-change
            # if sending goes quick enough, we could miss a file change because of this
            # it is a bit flimsy, all of this
            # lastModificationDate = os.path.getmtime(filename)
            lastFileContent = fileData
    except IOError:
        hasChanged = False
        # print(".")

    # calculate next interval with delay;
    #  this is the minimum wait to update, by way of a delay inside the while-True
    currentTimeMs = time.time_ns()/1000000.0
    while nextIntervalMs < currentTimeMs:
        nextIntervalMs = nextIntervalMs + intervalInMs

    delayIntervalMS = nextIntervalMs - currentTimeMs
    lastIntervalMS = nextIntervalMs
    if delayIntervalMS > 0:
        time.sleep(delayIntervalMS / 1000.0)

# unreachable
# close the socket
s.close()
exit(0)

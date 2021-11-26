# Byte Jam server

## Prerequisites

- Windows (this would be trivial to port to other platforms, it's just not been a priority)
- Python 3
- Port 4444 exposed to the outside world
- Four copies of the bytebattle tic80 client inside the `/server` directory, renamed tic80server_1.exe, tic80server_2.exe, tic80server_3.exe, tic80server4.exe (see the section on OBS)

## How to run a byte jam

1. Inform your participants
2. Launch the server
3. Launch OBS

### 1. Inform your participants

1. Go into the `/clients` directory and update every file with `clientstart` in it to use your IP address.
2. Copy the bytebattle client for Windows in there, give it the name `tic80showdown.exe`
3. Zip up that folder and send it to your participants. Give each participant a player number between 1-4, tell them to read the readme, tell them that you hope they have fun, and tell them that you love them.

### 2. The server

Launching `server.bat` on a Windows machine should spin up four tic80s and a python server.

### 3. OBS

You can discern the separate tic80s in OBS by their executable name. There is an example Scene Collection that you can import, in the `../obs` directory. This is why in the prerequisites you had to make four copies of the executable with different names.

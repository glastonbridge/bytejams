REM Server: (python3) server.py <PortNr>

start tic80server_1 --skip --codeimport=./incoming/1.lua --delay=5
start tic80server_2 --skip --codeimport=./incoming/2.lua --delay=5
start tic80server_3 --skip --codeimport=./incoming/3.lua --delay=5
start tic80server_4 --skip --codeimport=./incoming/4.lua --delay=5

python server.py 4444
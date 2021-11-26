Byte Jam setup

Contestant preparation
----------------------
* If you do not have it already (the windows version is included in this zip), get the TIC-80 with Byte Battle extensions from here
  https://github.com/nesbox/TIC-80/actions/runs/1205770914#artifacts
  The scripts in this zip assume that you have unzipped it to a folder, and placed the executable in the same folder.
* Make sure you have a python3 interpreter installed (it has been tested with 3.7 but should work with earlier)
* You will need to give TIC-80 permission to run. Right-click on the tic80 app in this folder and click "open."
  The OS may ask you if you want to run it. Say yes and don't ask again. When the TIC-80 client loads, quit it.

Competing
---------
The host will decide if you are client 1, 2, 3 or 4. 
You will need to run both the clientstart#.sh (to connect to the server) and the tic80xxx_launcher.sh (to launch the TIC-80 client
with the correct configuration). Run them from separate tabs in your terminal. You should then have a copy of TIC-80 running to the
server. Happy jamming!

Manually running
----------------
Apart from client.py, the launch scripts are all just one-liners. If you look inside, you will see that the structure is simple and
you're welcome to launch TIC-80 that way instead. Basically, the TIC-80 saves everything to a datafile, and the client polls that file
for changes. Simple!

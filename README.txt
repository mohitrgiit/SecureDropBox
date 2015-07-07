
Designed and developed a desktop application which ensures privacy of data when a user uploads files to a cloud storage service like Dropbox, Box and Google Drive etc. Privacy preservation is achieved using BP-XOR erasure encoding scheme. There is a monitored directory into which a user can drop a file. The file is then encoded using BP-XOR and four file chunks are generated according to the following scheme.

Storage Code:
f1,f2,f3 - splits of original file of size chunksize

R1,R2.....R6 - six random chunks of chunksize

f1 xor R5 = R8

f2 xor R4 = R7

f3 xor R6 = R9 

R6 xor R7 = R67

R3 xor R8 = R38
          = R14
          = R89
          = R45
          = R26
          = R25
          = R37
          = R19


Chunks distributed among servers:

Server 1 : R1,R67,R38

Server 2 : R2,R14,R89

Server 3 : R3,R45,R26

Server 4 : R25,R37,R19


The file can be recovered from any three servers.



To use:

Compile and start filemonitor.c . This will start monitoring the MagicBox folder. Any file dropped into the folder will be split and uploaded.

To download, start test.py. This is the GUI for downloading files. It displays the files that stored across the four servers(by original filename) and select a file for downloading.



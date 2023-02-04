from ftplib import FTP 
2 import os 
3 
 
4 
 
5 # Gather Credentials saved as environment variables 
6 host = os.environ['HOST'] 
7 port = int(os.environ['PORT']) 
8 user = os.environ['USER'] 
9 pswd = os.environ['PASS'] 
10 
 
11 # Establish FTP connection 
12 ftp = FTP() 
13 ftp.connect(host, port) 

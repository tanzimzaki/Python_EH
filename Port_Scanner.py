#!/usr/bin/python

#Tanzim_Zaki_Saklayen
#Student_ID:10520140

import socket     #retrieve socket library to perform the port scanning activity

ip_address = input("Enter IP address: ")  #user is prompt to insert the IP address to inititate the scan
first = int(input("Enter first port: "))   #user is prompt to insert the first port number to initiate the scan
last = int(input("Enter last port: "))      #user is prompt to insert the last port number to initiate the scan

for port in range (first, last):       #for loop is implemented to scan each port if the port is open
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    if s.connect_ex((ip_address, port)) == 0:
        print("Port",port,"is Open")
    s.close() 




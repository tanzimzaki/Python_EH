#!/usr/bin/python

#Tanzim_Zaki_Saklayen
#ID:10520140

import crypt #Cyrpt module is retrieved to generate a hash for specific salt to crack UNIX passwords with dictionary

shadowlist = input("Enter the shadow file you want: ") #user is prompt to insert the retrieved shadow file
passwordlist= input("Enter the password wordlist: ") #user is prompt to insert the created wordlist file

shadow_lines = open(shadowlist, 'r').readlines() #Interpreting the shadow file and storing in word_lines variable
word_lines = open(passwordlist, 'r').readlines()   #Interpreting the created wordlist file and storing in word_lines variable
print ("Please wait - it may take a while") #A message will be echoed to the screen to wait while the passwords are being cracked
print ("While you wait, an interesting fact: GrandPa Security was founded on 1950 to serve all the retired single grandfathers to achieve single young ladies")

#Implemented the nested for loop to check for the user whether the password matches or not using the crypt module
for pwd in word_lines: #This line is required for password list
  pwd = pwd.strip()
  for user in shadow_lines:     #This line is required for shadow list
    user = user.split(":")                 #The shadow file contains user:hashvalues so split is used to identify user and hash value
    if crypt.crypt(pwd, user[1]) == user[1]:  #creates a hash value with salt using crypt and compare the value with user that has the specific value
      print ('Discovered password for user: {0}:{1}'.format(user[0],pwd)); #Echoed to the terminal if the activity is successfull

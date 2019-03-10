#author: Remberto
#last modified 5-10-17
#Description: This is the code that will get the user information
#from data.txt and send a message of the open parking lots to the user

import smtplib
import os

# at&t:     @mms.att.net
# t-mobile: @tmomail.net
# verizon:  @vtext.com
# sprint:   @page.nextel.com

def sendMessage(message):
    #reads the information from data
    data = open('data.txt','r')
    info = data.readlines()
    data.close()
    #formats the information
    number = info[4]
    number = number[:-1]
    phoneCar = info[3]
    phoneCar = phoneCar[:-1]
    firstNam = info[0]
    firstNam = firstNam[:-1]
    secondNam = info[1]
    secondNam = secondNam[:-1]
    #connects to the setver
    server = smtplib.SMTP( "smtp.gmail.com", 587 )
    server.starttls()
    #logs in into the texting servise account
    server.login( 'parkingdetectorcst@gmail.com', 'CST2052017' )
    #sends the message to the user
    if(phoneCar == 'verizon'):
        server.sendmail( 'Parking Spot Detector', number+'@vtext.com', 'Hi '+firstNam+' '+secondNam+ ' the parking lots avilable are ' + message)
        print('Message Sent')
    if(phoneCar == 'sprint'):
        server.sendmail( 'Parking Spot Detector', number+'@page.nextel.com', 'Hi '+firstNam+' '+secondNam+ ' the parking lots avilable are ' + message)
        print('Message Sent')
    if(phoneCar == 't-mobile'):
        server.sendmail( 'Parking Spot Detector', number+'@tmomail.net', 'Hi '+firstNam+' '+secondNam+ ' the parking lots avilable are ' + message)
        print('Message Sent')
    if(phoneCar == 'at&t'):
        server.sendmail( 'Parking Spot Detector', number+'@mms.att.net', 'Hi '+firstNam+' '+secondNam+ ' the parking lots avilable are ' + message)
        print('Message Sent')
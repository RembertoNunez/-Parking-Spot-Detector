#Author: Daniel Ochoa
#last Modified: 04-19-17
#Description: This file connects the project together. Its main purpose is to read the scores and deside if the parking spot is open or not.
#futher improvements: 1. Connect the results of this file into the notification services.
#2. make the system calls into a function

from cropImage import cropImage #this file takes a picture of an image
#and crops it to 16 different images.
import time
import cv2
import os
import numpy as np
from PIL import Image
from textMessage import sendMessage
#from image import blackAndWhite

def textPerson():
	#labels of the parking spots
	labels = ['a1','a2','a3','a4','a5','a6','b1','b2','b3','b4','b5','b6']
	
	version = 1 #this variable is used to cycle through the different picutes of the parking spot. This far there is only 10 pictures
	stop = 2
	while(version  != stop):
	
		#gets the file path
		imgFilePath = "car/car" + str(version) + ".jpg"
		#inputs the file path and the functions outputs the images of each parking spot.
		cropImage(imgFilePath)
		version = version + 1
		
		#this is not needed it's just nice to see what picture it is currently processing
		im = Image.open(imgFilePath)
		im.show()
	
	
	#**************************************************************
		#this opens up the text file the scores are entered.
		#opening and closing it with the write mode erases everything in the file. I do this to get rid of previous scores
		file = open("parkingScores.txt","w")
		file.close()
	
		#I used system calls because it was the only way my processor would handel the amount of information.
		#label_image.py runs with an image and then writes the score of that spot into parkingScores.txt
	
		os.system("python label_image.py a1.jpg")
	
		os.system("python label_image.py a2.jpg")
	
		os.system("python label_image.py a3.jpg")
	
		os.system("python label_image.py a4.jpg")
	
		os.system("python label_image.py a5.jpg")
	
		os.system("python label_image.py a6.jpg")
	
		os.system("python label_image.py b1.jpg")
	
		os.system("python label_image.py b2.jpg")
	
		os.system("python label_image.py b3.jpg")
	
		os.system("python label_image.py b4.jpg")
	
		os.system("python label_image.py b5.jpg")
	
		os.system("python label_image.py b6.jpg")
	
		#os.system("python label_image.py c1.jpg")
	
		#os.system("python label_image.py c2.jpg")
	
		#os.system("python label_image.py c3.jpg")
	
		#os.system("python label_image.py c4.jpg")
	#****************************************************************
	
		#Reads the data from parkingScores.txt and puts it into an array.
		file = open("parkingScores.txt","r")
		score = file.readlines()
	
		print (score)
		parking_avilable = ""
		
		
		for i in range(12):
			temp = score[i]
	#here I decide if the parking spot is avilable or not the lowest score I accept is a 60%
			if(temp[:3] == '0.8' or temp[:3] == '0.9' or temp[:3] == '0.7' or temp[:3] == '0.6' or temp[:3] == '0.5'):
				score[i] = 0
				print (labels[i] + " is open")
				parking_avilable = parking_avilable + labels[i] + " "
			else:
				score[i] = 1
				print (labels[i] + " is taken")
		if(version > 14):
			version = version + 1
		print (score)
		print (parking_avilable)
		sendMessage(parking_avilable)
		parking_avilable = ""
	stop = stop + 1
		
	


#Author: Daniel Ochoa
#Last Modified: 04-19-17
#Description: Takes in a file path. Opens the image and crops out each parking spot.

from PIL import Image

#takes in a file path
def cropImage(img):
	#opens the file path
	img = Image.open(img)

	#crops the main image into individual parking spots
	#and saves it into its corresponding picture
	a1 = img.crop((1100,725,1200,840))
	a1.save("a1.jpg")

	a2 = img.crop((1100,605,1200,710))
	a2.save("a2.jpg")

	a3 = img.crop((1100,490,1210,585))
	a3.save("a3.jpg")

	a4 = img.crop((1110,375,1200,470))
	a4.save("a4.jpg")

	a5 = img.crop((1105,270,1200,355))
	a5.save("a5.jpg")

	a6 = img.crop((1120,165,1200,250))
	a6.save("a6.jpg")

	b1 = img.crop((860,715,960,820))
	b1.save("b1.jpg")

	b2 = img.crop((880,595,970,695))
	b2.save("b2.jpg")

	b3 = img.crop((890,485,990,575))
	b3.save("b3.jpg")

	b4 = img.crop((910,275,1000,360))
	b4.save("b4.jpg")

	b5 = img.crop((910,275,1000,360))
	b5.save("b5.jpg")

	b6 = img.crop((920,180,1000,260))
	b6.save("b6.jpg")


	


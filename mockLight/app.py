#Author: Daniel Ochoa
#last Modified: 05-9-17
#Description: This is the main file were we connect our website to the 
#texting servise and the parking lot detector.
from flask import Flask, render_template, request, url_for, redirect
import os
from text import textPerson

app = Flask(__name__, template_folder='template')

#this varible is used to cycle through the different pictures in car/
version = 1

@app.route('/')
def homepage():
    return render_template('homepage.html')
    
@app.route('/', methods=['POST'])
def enterInformation():
    #for used to get the users information
    name = request.form['name']
    lastName = request.form['lastName']
    email = request.form['email']
    carrier = request.form['PhoneCarrier']
    phone = request.form['phone']
    notify = request.form['DateNotified']
    if (request.form['submit'] == "submit"):
        #writes the information of the user intp a text file for later use
        file = open("data.txt", "w")
        file.write(name + '\n')
        file.write(lastName + '\n')
        file.write(email + '\n')
        file.write(carrier + '\n')
        file.write(phone + '\n')
        file.write(notify)
        file.close()
        global version
        #calculates the open parking lots and text the user
        textPerson(version)
        #moves on to the next picture
        version = version + 1
        return render_template('homepage.html')
        
if __name__ == '__main__':
    app.run(
        debug=True,
        port=int(os.getenv('PORT', 8080)),
        host=os.getenv('IP', '0.0.0.0')
    )

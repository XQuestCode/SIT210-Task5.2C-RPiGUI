# import everything from tkinter module
from tkinter import *   
import RPi.GPIO as GPIO
# create a tkinter window
root = Tk()             
redpin = 10               #pin for red led
greenpin = 11             #pin for green led
bluepin = 12              #pin for blue led
#global variables to be used when button toggles

redState = True

greenState = True

blueState = True
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(redpin, GPIO.OUT)
GPIO.setup(greenpin, GPIO.OUT)
GPIO.setup(bluepin, GPIO.OUT)

# Open window having dimension 100x100
root.geometry('300x300')
bg = PhotoImage(file = "image.png")
label1 = Label( root, image = bg)
label1.place(x = 0, y = 0)
#Functions
def Toggle(button):
   
    if button["relief"] == SUNKEN:
        button["relief"] = RAISED
        button["width"] = 10
    else:
        button["relief"] = SUNKEN
        button["width"] = 9
        
def Reset():  #to reset all the three LEDs
    global redpin
    global greenpin
    global bluepin
    redButton["relief"] = RAISED
    greenButton["relief"] = RAISED
    blueButton["relief"] = RAISED
    GPIO.output(redpin, GPIO.LOW)
    GPIO.output(greenpin, GPIO.LOW)
    GPIO.output(bluepin, GPIO.LOW) 
    
def redToggle(): 
    global redState
    if redState == True:
        Toggle(redButton)
        GPIO.output(redpin, GPIO.HIGH)
        redState = False
    else :
        Toggle(redButton)
        GPIO.output(redpin, GPIO.LOW)
        redState = True

def greenToggle():
    global greenState
    if greenState == True:
        Toggle(greenButton)
        GPIO.output(greenpin, GPIO.HIGH)
        greenState = False
    else :
        Toggle(greenButton)
        GPIO.output(greenpin, GPIO.LOW)
        greenState = True

def blueToggle():
    global blueState
    if blueState == True:
        Toggle(blueButton)
        GPIO.output(bluepin, GPIO.HIGH)
        blueState = False
    else:
        Toggle(blueButton)
        GPIO.output(bluepin, GPIO.LOW)
        blueState = True

####
# Create a Button
redButton = Button(root, text ="RED",bd = '5', fg = 'white', bg = 'red', height = 1, width = 10, relief=RAISED , command = redToggle)
greenButton = Button(root, text ="GREEN", bd = '5', fg = 'white', bg = 'green', height = 1, width = 10, relief=RAISED, command = greenToggle )
blueButton = Button(root, text ="BLUE", bd = '5',  fg = 'white', bg = 'blue', height = 1, width = 10, relief=RAISED, command = blueToggle )

redButton.pack(padx=100,pady=10)
greenButton.pack(padx=100,pady=10)
blueButton.pack(padx=100,pady=10)
# Set the position of button on the top of window.  
   
 
root.mainloop()
GPIO.cleanup()

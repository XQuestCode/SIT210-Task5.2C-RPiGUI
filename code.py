# import everything from tkinter module
from tkinter import *   
import RPi.GPIO as GPIO
# create a tkinter window
root = Tk()             
redpin = 10               #pin for red led
greenpin = 11             #pin for green led
bluepin = 12              #pin for blue led
#global variables to be used when button toggles
#Coded by Aditya Parmar
#XQuest

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(redpin, GPIO.OUT)
GPIO.setup(greenpin, GPIO.OUT)
GPIO.setup(bluepin, GPIO.OUT)
#Coded by Aditya Parmar
#XQuest
# Open window having dimension 100x100
root.geometry('300x300')
bg = PhotoImage(file = "image.png")
label1 = Label( root, image = bg)
label1.place(x = 0, y = 0)
#Functions
var = IntVar()
def Toggle():
    global var
    Reset()
    #GPIO.cleanup()
    if(var.get()== 1):
        print("red")
        redToggle()
    elif(var.get()== 2):
        print("green")
        greenToggle()
    elif(var.get()== 3):
        print("blue")
        blueToggle()
    else:
        Reset()
        print("Resetting all pins")
        
#Coded by Aditya Parmar
#XQuest
def Reset():
    global redpin
    global greenpin
    global bluepin
    GPIO.output(redpin, GPIO.LOW)
    GPIO.output(greenpin, GPIO.LOW)
    GPIO.output(bluepin, GPIO.LOW) 

def redToggle(): 
    global redpin
    GPIO.output(redpin, GPIO.HIGH)
    

def greenToggle():
    global greenpin
    GPIO.output(greenpin, GPIO.HIGH)
    

def blueToggle():
    global bluepin
    GPIO.output(bluepin, GPIO.HIGH)

####
# Create a Button
redButton = Radiobutton(root, text ="RED", fg= "red", variable=var, value=1, command = Toggle)

greenButton = Radiobutton(root, text ="GREEN", fg= "green",  variable=var, value=2, command = Toggle )

blueButton = Radiobutton(root, text ="BLUE", fg= "blue", variable=var, value=3, command = Toggle )

resetButton = Radiobutton(root, text ="Reset",  variable=var, value=4, command = Toggle )
resetButton.select()


redButton.pack(anchor = W, padx=100,pady=10)
greenButton.pack(anchor = W, padx=100,pady=10)
blueButton.pack(anchor = W ,padx=100,pady=10)
resetButton.pack(anchor = W ,padx=100,pady=10)
# Set the position of button on the top of window.  
   
#Coded by Aditya Parmar
#XQuest

root.mainloop()
GPIO.cleanup()

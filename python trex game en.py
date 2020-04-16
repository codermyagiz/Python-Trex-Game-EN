from PIL import ImageGrab, ImageOps #We're adding the Pillow library because we want to know the pixel values in a specific area of the screen.
import pyautogui #Pyautogui is used for mouse and keyboard control on python.
import time #Time is used to control time on python.
from numpy import * #Numpy is used to do some calculations.

class cordinates(): #We're opening a coordinates class.
    replay_button = (340, 390) #replay_button
    dinosaur_xy = (202, 441)  #dinosaur cordinates
    #The following values are the coordinates we need to check if our Cactus is present.
    #I'll put in a tutorial to find these coordinates.
    #x = 220 (the cordinate required to check whether the Cactus exists) 
    #y = 466 (the cordinate of half the Cactus)

def restart_game(): #restart_game
    pyautogui.click(cordinates.replay_button) #We restart the game using the "click" module of the Pyautogui library.
    
def pressSpace():  #pressSpace 
    pyautogui.keyDown('space') #Pyautogui will press space using the library's "keyDown" module.
    time.sleep(0.05) #sleep is a delay function.
    print('Jump') #İt'll be written "Jump" on the console.
    pyautogui.keyUp('space') #Using the "keyUp" module of the pyautogui library, pressing space will be left.

def imageGrab(): #The imageGrab library is for the display to receive ss.
    scan = (cordinates.dinosaur_xy[0] + 63, cordinates.dinosaur_xy[1], cordinates.dinosaur_xy[0] + 100, cordinates.dinosaur_xy[1]+30) #Here we determine where the area to scan is. This is not a place to watch the tutorial, but the average values, I split the screen to one side editor to one side of the game I found the most appropriate values.
    image = ImageGrab.grab (scan)   #Here we're using imageGrab library because we'll screenshot the scan zone.
    grayImage = ImageOps.grayscale(image)  #the screenshot will be convert the grayscale.
    a = array(grayImage.getcolors())      #Take the pixel values.
    print(a.sum())                      #Pixel values print the console
    return(a.sum())                    #Return the pixel values.

def main():     
    restartGame()
    while True:
        if (imageGrab()!=1357):  #This number is variable. This number about the "scan".
            time.sleep(0.1)
            pressSpace()

                    
   
main()                               #Starting the python code program.                                                                                                                                                                                                                                                                                                                   
   

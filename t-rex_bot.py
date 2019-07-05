from PIL import ImageGrab,ImageOps
import pyautogui
import time
from numpy import *

class Cordinates():  #this class has the cordinates of dino and the reply button.
    replayBtn = (523,485)
    dinasaur = (182,496)
    #250 = x cordinate to check for trees
    #500 = y cordinates to lowest obstecls

def restartGame():				#function for restarting the game.
    pyautogui.click(Cordinates.replayBtn)
    pyautogui.keyDown('down')

def pressSpace():				#this function will control all the key pressing events.
    pyautogui.keyUp('down')
    pyautogui.keyDown('space')
    print("Jump")
    time.sleep(0.08)
    pyautogui.keyUp('space')
    pyautogui.keyDown('down')

def imageGrab():				#this function will grab screenshots to get the info of obstracles.
    box = (Cordinates.dinasaur[0]+30,Cordinates.dinasaur[1],Cordinates.dinasaur[0]+155,Cordinates.dinasaur[1]+7)
    image = ImageGrab.grab(box)
    grayImage = ImageOps.grayscale(image)
    a = array(grayImage.getcolors())
    #print(a.sum())
    return(a.sum())
'''while True:
    imageGrab()'''


def main():
    restartGame()
    while True:
        if (imageGrab()!=1122):
            pressSpace()
            time.sleep(0.05)
main()

#created by Uchit Patel.
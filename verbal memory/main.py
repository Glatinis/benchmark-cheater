import cv2 
import pytesseract
import pyautogui as pyag
import numpy as np
import sys; sys.path.append("..")
from common import adjustCoordinate
from PIL import Image, ImageGrab

CUSTOMCONFIG = r"--oem 3 --psm 8"

STARTBTN = adjustCoordinate((950,540))
NEWBTNPOS = adjustCoordinate((1020,475))
SEENBTNPOS = adjustCoordinate((885,475))
bboxStart = adjustCoordinate((650, 350))
bboxEnd = adjustCoordinate((1350, 440))

def getProcessedImg():
    screenshot = ImageGrab.grab((bboxStart[0], bboxStart[1], bboxEnd[0], bboxEnd[1]))

    grayscaled = cv2.cvtColor(np.array(screenshot), cv2.COLOR_BGR2GRAY)
    thresholded = cv2.threshold(grayscaled, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

    processed = Image.fromarray(thresholded)
    # processed.save("test output.png")

    return processed

def Img2Word(img):
    word = pytesseract.image_to_string(img, config=CUSTOMCONFIG)
    word = "".join(filter(str.isalpha, word))

    return word


def main():
    lastWord = ""
    seenWords = []

    pyag.click(STARTBTN)

    while True:
        processed = getProcessedImg()
        word = Img2Word(processed)

        print(word)

        if len(word) < 1: break
        if lastWord == word: break
        else: lastWord = word
        
        if word in seenWords:
            pyag.click(SEENBTNPOS)
        else:
            pyag.click(NEWBTNPOS)
            seenWords.append(word)
    
    pyag.click(STARTBTN)


if __name__ == "__main__":
    main()
        
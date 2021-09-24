import pyautogui as pyag
import sys; sys.path.append("..")
from common import adjustCoordinate
from PIL import ImageGrab


CONFIG1 = [adjustCoordinate((820,300)), adjustCoordinate((950,300)), adjustCoordinate((1080,300)),
           adjustCoordinate((820,425)), adjustCoordinate((950,425)), adjustCoordinate((1080,425)),
           adjustCoordinate((820,550)), adjustCoordinate((950,550)), adjustCoordinate((1080,550))]

STARTBTN = adjustCoordinate((950,530))


def getPointColors(config):
    screenshot = ImageGrab.grab()
    pointColors = []

    for point in config:
        pointColor = screenshot.getpixel(point)
        pointColors.append(pointColor)
    
    return pointColors


def main():
    currentConfig = CONFIG1
    currentPattern = []
    lastIndex = None

    pyag.click(STARTBTN)

    while True:
        pointColors = getPointColors(currentConfig)
        whiteIndex = pointColors.index((255,255,255)) if (255,255,255) in pointColors else None

        if whiteIndex != lastIndex and whiteIndex != None:
            currentPattern.append(whiteIndex)
        
        if lastIndex != None and whiteIndex == None:
            print(currentPattern)
            
            for index in currentPattern:
                positionToClick = currentConfig[index]
                pyag.click(positionToClick)

            currentPattern = []
        
        lastIndex = whiteIndex



if __name__ == "__main__":
    main()
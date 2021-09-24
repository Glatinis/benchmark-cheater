import pyautogui as pyag
import sys; sys.path.append("..")
from common import adjustCoordinate
from ctypes import windll
from time import sleep



GREEN = 7002955
CHECKPOS = adjustCoordinate((950,570))
dc = windll.user32.GetDC(0)

def getpixel(x,y):
    return windll.gdi32.GetPixel(dc, x, y)

def main():
    pyag.click(CHECKPOS)

    while True:
        boxColor = getpixel(CHECKPOS[0], CHECKPOS[1])
        if boxColor == GREEN:
            pyag.click(CHECKPOS)
            sleep(0.5)
            pyag.click(CHECKPOS)


if __name__ == "__main__":
    main()
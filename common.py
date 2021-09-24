import ctypes

user32 = ctypes.windll.user32
screenSize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)

def adjustCoordinate(oldCoordinate):
    OLDWIDTH = 1920
    OLDHEIGHT = 1080
    NEWWIDTH = screenSize[0]
    NEWHEIGHT = screenSize[1]
    oldX = oldCoordinate[0]
    oldY = oldCoordinate[1]

    newX = round((oldX * NEWWIDTH) / OLDWIDTH)
    newY = round((oldY * NEWHEIGHT) / OLDHEIGHT)

    return (newX,newY)


if __name__ == "__main__":
    print(adjustCoordinate((500,500)))
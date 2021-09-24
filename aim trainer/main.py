import cv2
import numpy as np
import sys; sys.path.append("..")
from common import adjustCoordinate
from PIL import ImageGrab


target = cv2.imread("target.png")
bboxStart = adjustCoordinate((0,116))
bboxEnd = adjustCoordinate((1900,652))

while True:
    screenshot = cv2.cvtColor(np.array(ImageGrab.grab(bbox=(bboxStart[0], bboxStart[1], bboxEnd[0], bboxEnd[1]))), cv2.COLOR_BGR2RGB)

    result = cv2.matchTemplate(target, screenshot, cv2.TM_SQDIFF_NORMED)

    # We want the minimum squared difference
    mn,_,mnLoc,_ = cv2.minMaxLoc(result)

    # Draw the rectangle:
    # Extract the coordinates of our best match
    MPx, MPy = mnLoc

    # Step 2: Get the size of the template. This is the same size as the match.
    trows, tcols = target.shape[:2]

    # Step 3: Draw the rectangle on large_image
    cv2.rectangle(screenshot, (MPx,MPy), (MPx + tcols, MPy + trows), (0,0,255), 2)
    half = cv2.resize(screenshot, (0, 0), fx = 0.6, fy = 0.6)

    # Display the original image with the rectangle around the match.
    cv2.imshow("output", half)

    # The image is only displayed if we call this
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cv2.destroyAllWindows()
# import the packages
import cv2
import numpy as np
import argparse
import imutils

# argument parser construction
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the Image")
args = vars(ap.parse_args())

# read image
image = cv2.imread(args["image"])
# cv2.imshow("Image", image)
# cv2.waitKey(0)

# create a mask to filter the black shapes using inRange
lower = np.array([0,0,0])
upper = np.array([15,15,15])
mask = cv2.inRange(image, lower, upper)
cv2.imshow("Mask", mask)
cv2.waitKey(0)

contours = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
contours = imutils.grab_contours(contours)
print("Found {} black shapes".format(len(contours)))

# loop over contours
for cnt in contours:
    cv2.drawContours(image, [cnt], -1, (0,255,0), 2)
    cv2.imshow("Final Image", image)
    cv2.waitKey(0)
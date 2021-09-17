import numpy as np
import time
import cv2

# Deciding the Codec algorithm for video and setting the output file
fourcc = cv2.VideoWriter_fourcc(*'XVID')
output_file = cv2.VideoWriter('final.avi', fourcc, 20.0, (650, 400))

# Starting the webcam and putting the code to sleep for 3 seconds
capture = cv2.VideoCapture(0)
time.sleep(3)

# Capturing the background for 60 seconds and flipping it
for i in range(60):
  ret, bg = capture.read()
bg = np.flip(bg, axis=1)

while capture.isOpened():
  ret, img = capture.read()
  if (not ret):
    break
  img = np.flip(img, axis=1)
  img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

  lower_red = np.array([0, 100, 50])
  upper_red = np.array([20, 255, 255])
  mask1 = cv2.inRange(img_hsv, lower_red, upper_red)

  lower_red = np.array([170, 100, 70])
  upper_red = np.array([180, 255, 255])
  mask2 = cv2.inRange(img_hsv, lower_red, upper_red)

  mask1 += mask2

  # Opening and expanding the part with red color
  mask1 = cv2.morphologyEx(mask1, cv2.MORPH_OPEN, np.ones((3,3), np.uint8))
  mask2 = cv2.morphologyEx(mask1, cv2.MORPH_DILATE, np.ones((3,3), np.uint8))

  # Selecting only the part without red color and storing it in mask2
  mask2 = cv2.bitwise_not(mask1)

  # Keeping only the part of the image without red color
  res1 = cv2.bitwise_and(img, img, mask=mask2)

  # Keeping only the part of the image with red color
  res2 = cv2.bitwise_and(img, img, mask=mask1)

  # Generating the final output
  final = cv2.addWeighted(res1, 1, res2, 1, 0)
  output_file.write(final)

  # Displaying the output to the user
  cv2.imshow("Invisibility cloak", final)
  cv2.waitKey(1)

capture.release()
cv2.destroyAllWindows()
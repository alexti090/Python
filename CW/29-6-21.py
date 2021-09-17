import cv2
import pandas
import numpy as np
""" import seaborn as sb
import matplotlib.pyplot as plt """
from sklearn.datasets import fetch_openml
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from PIL import Image 
import PIL.ImageOps
import os, time

x, y = fetch_openml('mnist_784', version=1, return_X_y=True)
print(pandas.Series(y).value_counts())
classes = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

nClasses = len(classes)
samplesPerClass = 10
""" figure = plt.figure(figsize=(nClasses*2, samplesPerClass*2))

clm = 0
for c in classes:
  indexes = np.flatnonzero(y==c)
  rIndexes = np.random.choice(indexes, samplesPerClass, replace=False)
  row = 0
  for r in rIndexes:
    pltIndex = row * nClasses + clm + 1
    p = plt.subplot(samplesPerClass, nClasses, pltIndex)
    p = sb.heatmap(np.reshape(x[r], (28, 28)), cmap=plt.cm.gray, xticklabels=False, yticklabels=False, cbar=False)
    p = plt.axis('off')
    row += 1
  clm += 1
figure.show() """

xTrain, xTest, yTrain, yTest = train_test_split(x, y, random_state=9, train_size=7500, test_size=2500)
xTrain /= 255.0
xTest /= 255.0

clf = LogisticRegression(solver='saga', multi_class='multinomial')
clf.fit(xTrain, yTrain)

predictions = clf.predict(xTest)
accuracy = accuracy_score(yTest, predictions)
print('Accuracy: ', accuracy*100)

""" cm = pandas.crosstab(yTest, predictions, rownames=['Actual'], colnames=['Predicted'])
plt2 = plt.figure(figsize=(10, 10))
plt2 = sb.heatmap(cm, annot=True, cbar=False) """

cap = cv2.VideoCapture(0)

while(True):
  try:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    height, width = gray.shape
    upperleft = (int(width/2 - 50), int(height/2 - 50))
    bottomright = (int(width/2 + 50), int(height/2 + 50))
    cv2.rectangle(gray, upperleft, bottomright, (0,255,0), 2)

    roi = gray[upperleft[1]:bottomright[1], upperleft[0]:bottomright[0]]

    img_gray_pil = Image.fromarray(roi)
    img_gray_pil_scaled = img_gray_pil.convert('L')
    img_gray_pil_scaled_resize = img_gray_pil_scaled.resize((28,28), Image.ANTIALIAS)
    img_gray_pil_scaled_resize_inverted = PIL.ImageOps.invert(img_gray_pil_scaled_resize)
    pixel_filter = 30

    min_pixel = np.percentile(img_gray_pil_scaled_resize_inverted, pixel_filter)
    img_gray_pil_scaled_resize_inverted_clip = np.clip(img_gray_pil_scaled_resize_inverted-min_pixel, 0, 255)
    max_filter = np.max(img_gray_pil_scaled_resize_inverted)
    img_gray_pil_scaled_resize_inverted_clip = np.asarray(img_gray_pil_scaled_resize_inverted_clip)/max_filter

    testsample = np.array(img_gray_pil_scaled_resize_inverted_clip).reshape(1, 784)
    testprediction = clf.predict(testsample)
    print("Predicted class is : ", testprediction)
    
    if cv2.waitKey(1) & 0xFF == ord('x'):
      break
  except Exception as e:
    pass

cap.release()
cv2.destroyAllWindows()
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.datasets import fetch_openml
from PIL import Image 
import PIL.ImageOps
import pandas as pd
import numpy as np
import cv2

x, y = np.load('./Colab Files/image.npz')['arr_0'], pd.read_csv('./Colab Files/alphabet_recognition.csv')['labels']
classes = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',  'U', 'V', 'W', 'X', 'Y', 'Z',]
nClasses = len(classes)

xTrain, xTest, yTrain, yTest = train_test_split(x, y, random_state=9, train_size = 7500, test_size=2500)
xTrain /= 250.0
xTest /= 250.0

clf = LogisticRegression(solver='saga', multi_class='multinomial')
clf.fit(xTrain, yTrain)
yPred = clf.predict(xTest)
accuracy = accuracy_score(yTest, yPred)
print('Accuracy: ', str(accuracy*100)+'%')

cap = cv2.VideoCapture(0)

while(True):
  try:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    height, width = gray.shape
    ul = (int(width/2-50), int(height/2-50))
    br = (int(width/2+50), int(height/2+50))
    cv2.rectangle(gray, ul, br, (0,255,0), 2)
    roi = gray[ul[1]:br[1], ul[0]:br[0]]

    img_pil = Image.fromarray(roi)
    img_pil_bw = img_pil.convert('L')
    img_pil_bw_resize = img_pil_bw.resize((30,22), Image.ANTIALIAS)
    img_pil_bw_resize_inverted = PIL.ImageOps.invert(img_pil_bw_resize)
    pixel_filter = 20

    min_pixel = np.percentile(img_pil_bw_resize_inverted, pixel_filter)
    img_pil_bw_resize_inverted_clip = np.clip(img_pil_bw_resize_inverted-min_pixel, 0, 255)

    max_filter = np.max(img_pil_bw_resize_inverted)
    img_pil_bw_resize_inverted_clip = np.asarray(img_pil_bw_resize_inverted_clip)/max_filter

    testsample = np.array(img_pil_bw_resize_inverted_clip).reshape(1, 660)
    prediction = clf.predict(testsample)
    print("Predicted class is: ", prediction)

    if cv2.waitKey(1) & 0xFF == ord('x'):
      break
  except Exception as exc:
    print(exc)
    break

cap.release()
cv2.destroyAllWindows()
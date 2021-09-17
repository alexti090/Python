import numpy as np 
import pandas as pd
from sklearn.datasets import fetch_openml
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from PIL import Image 
import PIL.ImageOps

X, y =  fetch_openml('mnist_784', version = 1, return_X_y= True)

xtrain, xtest, ytrain, ytest = train_test_split(X, y, test_size = 2500, train_size = 7500, random_state = 9)
xtrainscaled = xtrain/255.0
xtestscaled = xtest/255.0

classifier = LogisticRegression(multi_class="multinomial", solver="saga")
classifier.fit(xtrainscaled, ytrain)

def getPrediction(image):
  img_pil = Image.open(image)
  img_bw = img_pil.convert("L")
  img_bw_resize = img_bw.resize((28, 28), Image.ANTIALIAS)

  pixel_filter = 30
  min_pixel_filter = np.percentile(img_bw_resize, pixel_filter)
  img_bw_resize_filtered = np.clip(img_bw_resize - min_pixel_filter, 0, 255)
  max_pixel_filter = np.max(img_bw_resize)
  img_bw_resize_filtered = np.asarray(img_bw_resize_filtered)/max_pixel_filter
  
  test_image = np.array(img_bw_resize_filtered).reshape(1, 784)
  test_prediction = classifier.predict(test_image)
  return test_prediction[0]
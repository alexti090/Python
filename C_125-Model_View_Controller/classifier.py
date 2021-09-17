from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from PIL import Image
import PIL.ImageOps
import numpy as np
import pandas

x, y = np.load('./C_125-Model_View_Controller/image.npz')['arr_0'], pandas.read_csv('./C_125-Model_View_Controller/alphabet_recognition.csv')['labels']
classes = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',  'U', 'V', 'W', 'X', 'Y', 'Z',]

xTrain, xTest, yTrain, yTest = train_test_split(x, y, random_state=9, train_size = 7500, test_size = 2500)
xTrain /= 250.0
xTest /= 250.0

clf = LogisticRegression(solver='saga', multi_class='multinomial')
clf.fit(xTrain, yTrain)

def getPred(image):
  img_pil = Image.open(image)
  img_bw = img_pil.convert("L")
  img_bw_resize = img_bw.resize((22, 30), Image.ANTIALIAS)

  pixel_filter = 30
  min_filter = np.percentile(img_bw_resize, pixel_filter)
  max_filter = np.max(img_bw_resize)
  img_bw_resize_filtered = np.clip(img_bw_resize - min_filter, 0, 255)
  img_bw_resize_filtered = np.asarray(img_bw_resize_filtered)/max_filter
  
  test_image = np.array(img_bw_resize_filtered).reshape(1, 660)
  test_predict = clf.predict(test_image)
  return test_predict[0]

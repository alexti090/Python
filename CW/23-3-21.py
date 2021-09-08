import dropbox
import cv2
import time

imgCount = 0

def takeSnap():
  cam = cv2.VideoCapture(0)
  ret, frame = cam.read()
  if not ret:
    print('Failed to take snapshot.')
    return 0
  elif ret:
    imgName = 'image'+str(imgCount)+'.png'
    cv2.imwrite(imgName, frame)
    return imgName

def uploadFiles(res):
  accessToken = '74Tpzuc3BBMAAAAAAAAAASexk2_ssotFu6nOnlkZAFORy-02I5Eg1rq52NlmYRLx'
  dbx = dropbox.Dropbox(accessToken)
  with open(res, 'rb') as file:
    dbx.files_upload(file.read(), '/'+res, mode=dropbox.files.WriteMode.overwrite)

while True:
  res = takeSnap()
  if res:
    imgCount += 1
    uploadFiles(res)
  time.sleep(30)
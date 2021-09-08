import os
import shutil

path1 = input('Enter folder path: ')
files = os.listdir(path1)
list = []
for d in files:
  name, ext = os.path.splitext(d)
  ext = ext[1:]
  if os.path.exists(path1+ext):
    shutil.move(path1+d, path1+ext+'\\'+d)
  else:
    os.makedirs(path1+ext)
    shutil.move(path1+d, path1+ext+'\\'+d)
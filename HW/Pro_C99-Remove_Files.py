import time
import os

oldFiles = []
now = time.time()

def delete(path):
  for (root, folders, files) in os.walk(path):
    for file in files:
      filePath = root+'\\'+file
      fileAge = os.stat(filePath).st_ctime
      if now - fileAge > 2592000:
        oldFiles.append(filePath)
  for folder in folders:
    delete(root+'\\'+folder)

while True:
  pathName = input('Enter folder path: ')
  if not os.path.exists(pathName):
    print('Path does not exist, try again.')
    time.sleep(2)
  elif os.path.exists(pathName):
    delete(pathName)
    break

print(str(len(oldFiles)), 'files older than 30 days (that is, 2925000 seconds) found.')
while True:
  time.sleep(2)
  a = input('Delete permanently? (Y/N): ')
  if a == "N" or a == "No" or a == "n" or a == "no":
    print('Deletion cancelled.')
    break
  elif a == "Y" or a=="Yes" or a == "y" or a == "yes":
    print('Deleting...')
    for file in oldFiles:
      os.remove(file)
    time.sleep(3)
    break
  else:
    print("Invalid: Enter Yes/No, or Y/N.")
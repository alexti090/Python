import dropbox
import os

dbx = dropbox.Dropbox('74Tpzuc3BBMAAAAAAAAAASexk2_ssotFu6nOnlkZAFORy-02I5Eg1rq52NlmYRLx')
while True:
  fileFrom = input('Enter file path to upload: ')
  if os.path.exists(fileFrom):
    name = input('Save to DropBox as: (enter file name without extension) -> ')
    path, ext = os.path.splitext(fileFrom)
    fileTo = '/' + name + ext
    with open(fileFrom, 'rb') as file:
      dbx.files_upload(file.read(), fileTo)
    break
  else:
    print('File path does not exist, try again')
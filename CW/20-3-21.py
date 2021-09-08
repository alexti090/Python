import dropbox

class UploadFile:
  def __init__(self, accessToken):
    self.accessToken = accessToken

  def upload(self, fileFrom, to):
    dbx = dropbox.Dropbox(self.accessToken)
    with open(fileFrom, 'rb') as file:
      dbx.files_upload(file.read(), to)
    print('Succesfuly done')

accessToken = '74Tpzuc3BBMAAAAAAAAAASexk2_ssotFu6nOnlkZAFORy-02I5Eg1rq52NlmYRLx'
upload = UploadFile(accessToken)

fileFrom = input('Enter file path to upload: ')
fileTo = '/testFile.txt'
upload.upload(fileFrom, fileTo)
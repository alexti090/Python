def func():
  inp = input('Enter file path: ')
  file = open(inp, 'r')
  lines=file.readlines()
  words=0
  for l in lines:
    w=l.split(' ')
    words = words + len(w)
  print(words)

def func2():
  source = input('Enter source file: ')
  dest = input('Enter destination file: ')
  try:
    srcFile = open(source, 'r')
    lines = srcFile.readlines()

    while True:
      choice = input('Enter 1 to append, enter 2 to overwrite: ')
      if choice == '1':
        destFile = open(dest, 'a')
        for l in lines:
          destFile.writelines(l)
        break
      elif choice == '2':
        destFile = open(dest, 'w')
        for l in lines:
          destFile.writelines(l)
        break
      else:
        print('Invalid input.')
  except:
    print('Invalid path, file does not exist')
func2()
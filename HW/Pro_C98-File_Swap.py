def swapText():
  while True:
    inp1 = input('Enter path for file 1: ')
    inp2 = input('Enter path for file 2: ')
    try:
      file1 = open(inp1, 'r')
      file2 = open(inp2, 'r')

      data1 = file1.readlines()
      file1.close()
      data2 = file2.readlines()
      file2.close()

      file1 = open(inp1, 'w')
      file2 = open(inp2, 'w')
      for l in data2:
        file1.writelines(l)
      for l in data1:
        file2.writelines(l)
      break
    except:
      print('Invalid path, please try again')
swapText()
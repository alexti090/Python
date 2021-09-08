import time
import random

again = True
num = random.randint(1, 100)
turns = 0
while again==True:
  try:
    inp=int(input("Guess my number! It is somewhere from 1 to 100! "))
    if inp == num:
      print("You WON in just", str(turns), "chances!")
      while True:
        time.sleep(1)
        a=input("Play again? (Y/N): ")
        if a == "N" or a == "No" or a == "n" or a == "no":
          print("Thanks for playing!")
          again = False
          time.sleep(2)
          break
        elif a == "Y" or a=="Yes" or a == "y" or a == "yes":
          print("Starting new game...")
          turns = 0
          num = random.randint(1, 20)
          time.sleep(3)
          break
        else:
          print("Invalid: Enter Yes/No, or Y/N.")
    elif inp > num:
      print("No, my number is smaller than", inp)
      turns = turns + 1
      time.sleep(2)
    elif inp < num:
      print("No, my number is larger than", inp)
      turns = turns + 1
      time.sleep(2)
  except:
    print("Enter a number!")
    turns = turns + 1
    time.sleep(2)
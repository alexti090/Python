import time

class ATM():
  def __init__(self):
    self.balance = 0
    self.symbol = '₹'

  def withDraw(self):
    draw = int(input('Withdraw how much? '))
    if self.balance - draw >= 0:
      self.balance -= draw
      print('Withdrew', self.symbol+str(draw), 'from your account, your balance is', self.symbol+str(self.balance)+'.')
    else:
      print("You don't have enough balance to withdraw this amount!")

  def deposit(self):
    dep = int(input('Deposit how much? '))
    self.balance += dep
    print('Deposited',  self.symbol+str(dep), 'to your account, your balance is', self.symbol+str(self.balance)+'.')

  def switch(self):
    if self.symbol == '₹':
      self.symbol = '$'
      self.balance /= 74
      print('Switched from INR(₹) to USD($).')
    elif self.symbol == '$':
      self.symbol = '₹'
      self.balance *= 74
      print('Switched from USD($) to INR(₹).')

  def check(self):
    print('Your balance is', self.symbol+str(self.balance)+'.')

  def command(self):
    print('\n'+"Type 'W' to withdraw, 'D' to deposit, 'S' to switch currency, 'B' to check your balance or 'E' to exit.")
    command = input()
    if command.upper() == 'W':
      self.withDraw()
      time.sleep(2)
      self.command()
    elif command.upper() == 'D':
      self.deposit()
      time.sleep(2)
      self.command()
    elif command.upper() == 'S':
      self.switch()
      time.sleep(2)
      self.command()
    elif command.upper() == 'B':
      self.check()
      time.sleep(2)
      self.command()
    elif command.upper() == 'E':
      print('Logging out...')
      time.sleep(3)
    else:
      print('Invalid input, try again')

bank = ATM()
bank.command()
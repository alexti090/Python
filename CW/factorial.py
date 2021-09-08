num=int(input('Enter a number: '))

## Factorial code
product=1
for i in range(1, num+1):
  product = product*i
print('The factorial of', num, 'is:',product)

## Prime number code
flag=False
for i in range(2, int(num/2+1)):
  if num%i == 0:
    flag=True
    break

if flag==False:
  print(num, 'is prime.')
else:
  print(num, 'is not prime')
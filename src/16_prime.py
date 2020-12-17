import sys

num = int(sys.argv[1])
y = [x+1 for x in range(int(num**0.5))]

def notPrime(x):
    print(f'{num} is not a prime number')

if num <= 1:
    print('Provide a number larger than one.')
    quit()

z = [x for x in y if num%x == 0]

if len(z) == 1:
    print(f'{num} is a prime number')
else:
    notPrime(num)

# python 16_prime.py
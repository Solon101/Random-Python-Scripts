from os import *
from time import *
IsRunning = True
n=1

def clear():
    if name == 'nt':
        _ = system('cls')

while True:
    print(n)
    n*=2+1
    sleep(.5)

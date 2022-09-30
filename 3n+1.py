# 3n+1 program
import time

n = int(input ('Please enter a number to test in the Collatz conjecture: '))
t = int(input('Please enter the delay in seconds between numbers printing on screen: '))

C = True

while C == True:

    time.sleep(t)

    print(n)

    if (n % 2) == 0:

              n = n / 2

    else:

              n = 3 * n + 1
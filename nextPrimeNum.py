#!/usr/bin/env python3
# nextPrimeNum.py - find prime numbers until the user chooses to stop asking for the next one.

def nextPrimeNum():
    primes = []
    b = 0
    num = 1

    while len(primes) <= b:
        for i in range(1, num+1 , 2):
            if (num % 2 != 0) and (num % i == 0):
                if i != 1 and i != num:
                    num += 1
                    continue
                if i == num:
                    primes.append(num)
                    print(primes)
                    num += 1
                    input('press enter to get next prime number')
                    b += 1
                    continue
            if num % 2 == 0:
                if num == 2:
                    primes.append(num)
                    print(primes)
                    num += 1
                    input('press enter to get next prime number')
                    b += 1
                    continue
                else:
                    num += 1
                    continue

if __name__ == '__main__':
        nextPrimeNum()

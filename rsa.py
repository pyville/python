'''
RSA 암호화를 Python으로 구현했습니다.
이정주 (jj2015@korea.ac.kr)
사용자가 입력할 큰 소수들은 영문 위키피디아에서 가져오실 수 있습니다.
단, 알고리즘의 특성상 소수가 너무 커지면 암호화 및 복호화에 많은 시간이 소요됩니다.
링크: https://en.wikipedia.org/wiki/List_of_prime_numbers
'''

import math
import sys

def isPrime (n):
    if (n == 1):
        return False
    if (n == 2):
        return True
    k = math.floor(math.sqrt(n))
    i = 2
    while(True):
        if (n % i == 0):
            return False
        if (i == k):
            break
        i = i+1
    return True

def GCD (a, b):
    if (a == b):
        return a

    if (b == 0):
        return a

    if (a < b):
        temp = a
        a = b
        b = temp

    return GCD(b, a % b)

def RSA (p, q, e):
    n = p*q
    pi = (p-1)*(q-1)
    d = 0
    while(True):
        if ((e*d) % pi == 1):
            break
        d = d+1
    return d

def encrypt (num, n, e):
    return (num ** e) % n

def decrypt (num, n, d):
    return (num ** d) % n

prime1 = int(input('첫번째 소수 p를 입력해주세요>')) # 17
print('소수 여부: ', isPrime(prime1))
prime2 = int(input('두번째 소수 q를 입력해주세요>')) # 23
print('소수 여부: ', isPrime(prime2))
encryptkey = int(input('(p-1)(q-1)과 서로소인 암호화 키를 입력해주세요>')) # 31
print('서로소 여부: ', GCD((prime1-1)*(prime2-1),encryptkey)==1)

if ((isPrime(prime1) == False) or (isPrime(prime2)== False) or (GCD((prime1-1)*(prime2-1),encryptkey)!=1)):
    print('조건이 충족되지 않아서 RSA 알고리즘을 중단합니다.')
    sys.exit(1)

n = prime1*prime2
decryptkey = RSA(prime1, prime2, encryptkey)

print('==========================================')
print('다음과 같이 RSA 알고리즘을 생성합니다.')
print('==========================================')
print('n: ', n) # n만 공개하고, 곱해서 n이 되는 두 소수는 공개하지 않음
print('공개 encryption key: ', encryptkey) # 공개함
print('비공개 decryption key: ', decryptkey) # 공개하지 않음
print('==========================================')
print('RSA 알고리즘 생성이 완료되었습니다.')
print('==========================================')

number1 = int(input('암호화할 숫자를 입력해주세요>')) # 66
print('encrypt ',number1,': ', encrypt(number1, n, encryptkey))

number2 = int(input('복호화할 숫자를 입력해주세요>')) # 212
print('decrypt ',number2,': ', decrypt(number2, n, decryptkey))

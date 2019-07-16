list1 = ['삼청동', '파주', '미국', '맛집', '거짓말','어벤져스']

def fibo(n):
    if n==1:
        return 1
    if n==2:
        return 2
    return fibo(n-1)+fibo(n-2)

def factorial(n):
    if n==0:
        return 1
    if n==1:
        return 1
    return n*factorial(n-1)

k = '삼청동' in list1

print(k)


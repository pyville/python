# 피보나치 수열 계산기 (recursive, non-recursive)

def fib(n):
    print('Calculating fib of', n)
    if n == 1:
        return 1
    if n == 2:
        return 1
    return fib(n-1) + fib(n-2)

def quickfib(n):
    fiblist = [1, 1]
    for i in range(n):
        print('Calculating fib of', i+1)
        # ignore if n == 1
        if i == 0:
            continue
        # ignore if n == 2
        if i == 1:
            continue
        fiblist.append(fiblist[i-2]+fiblist[i-1])
        print(fiblist[i])

    return fiblist.pop()

# 팩토리얼 계산기 (recursive, non-recursive)

def fac(n):
    print('Calculating fac of', n)
    if n == 0:
        return 1
    if n == 1:
        return 1
    return fac(n-1)*n

def quickfac(n):
    # ignore if n == 0
    if n == 0:
        return 1

    # Create a list
    faclist = [1]
    for i in range(n):
        print('Calculating fac of', i + 1)
        # ignore if n == 1
        if i == 0:
            continue
        faclist.append(faclist[i-1]*(i+1))
        print(faclist[i])

    return faclist.pop()



# 어떻게 진행되는지 확인

print(quickfib(150))

print(quickfac(150))

# 시간차이 확인
'''
print(fib(50))

print(fac(50))
'''
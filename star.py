def star(n):
    for i in range(n):
        print('*'*(i+1))

def sigma(n):
    sum = 0
    for i in range(n+1):
        if (i == 0):
            continue
        sum += i
        print('{}를 더하면 {}'.format(i, sum))

n = input('별을 몇개 따다줄까요>')
star(int(n))

s = input('1부터 몇까지 더해볼까요>')
sigma(int(s))

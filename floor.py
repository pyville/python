import random

def floor(list):
    for i in range(len(list)):
        print('{}층에 {}님이 살고있어요.'.format(i+1,list[i]))

list1 = []

n = input('살고 있는 사람 수>')

for i in range(int(n)):
    k = input('{}번째 살고 있는 사람 이름>'.format(i+1))
    list1.append(k)

random.shuffle(list1)
floor(list1)
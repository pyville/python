while(True):
    human = input('가위, 바위, 보 중 하나를 선택해주세요>')
    if (human == '가위' or human == '바위' or human == '보'):
        break
    else:
        print('올바른 패를 내 주세요. 휴먼')
computer = '?'
print('인간이 낸 것:', human)
if human == '가위':
    computer = '바위'
elif human == '바위':
    computer = '보'
elif human == '보':
    computer = '가위'
else:
    print('올바른 패를 내 주세요. 휴먼')
print('컴퓨터가 낸 것:', computer)
print('컴퓨터 승리')


anwsor1 = input('나는 누구일까요? 나는 보통 동그래요.:')
anwsor2 = input('나는 누구일까요? 나는 바늘이 세 개 있어요:')
anwsor3 = input('나는 누구일까요? 나는 시간을 알려줘요.:')

print('anwsor1:', anwsor1)

if anwsor1 == '시계':
    print('정답이에요!')

else:
    print('anwsor2', anwsor2)
    if anwsor2 == '시계':
        print('정답이에요!')
            else:
                print('anwsor3', anwsor3)
                if anwsor3 == '시계':
                    print('정답이에요!')
                        else:
                            print('스무고개 실패!')

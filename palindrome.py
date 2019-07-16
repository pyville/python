def palindrome(str):
    list1 = list(str)
    list2 = []
    list3 = list(str)

    while list1 != []:
        list2.append(list1.pop())

    if list2 == list3:
        return True
    return False

'''
print(palindrome('abba'))
print(palindrome('기러기'))
print(palindrome('abracadabra'))
print(palindrome('dadada'))
print(palindrome('mom'))

'''

while(True):

    str1 = input('회문 문자열을 입력하세요>')
    if not str1:
        break
    print(palindrome(str1))

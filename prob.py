def DashInsert(str):
    list1 = list(str)
    err = 0
    for i in range(len(list1)):
        if err == 1:
            err = 0
            continue
        if int(list1[i]) % 2 == 0 and int(list1[i+1]) % 2 == 0:
            list1.insert(i+1, '*')
            err = 1
        if int(list1[i]) % 2 == 1 and int(list1[i + 1]) % 2 == 1:
            list1.insert(i+1, '-')
            err = 1
    return ''.join(list1)

#str1 = input('숫자를 입력하세요>')
#print(DashInsert(str1))

def zipstr(str1):
    list1 = list(str1)
    list2 = []
    literal = ''
    count = 0
    for value in list1:
        if value != literal:
            list2.append(count)
            literal = value
            count = 1
            list2.append(value)
        else:
            count += 1
    del list2[0]
    if isinstance(list2[-1], str):
        list2.append(1)
    return list2

#print(zipstr('aaabbcccccca'))

def duplicate(str1):
    list1 = list(str1)
    list2 = [int(value) for value in list1]
    list3 = [n for n in range(10)]
    list2.sort()
    if list2 == list3:
        return True
    else:
        return False

print(duplicate('0987654321'))
print(duplicate('09876654321'))




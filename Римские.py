x = int(input('Введите число: '))
if 1 <= x <= 3:
    print('I' * x)
elif x == 4:
    print('IV')
elif 5 <= x <= 8:
    print('V' * (x-5) * 'I')
elif x == 9:
    print('IX')
elif x == 10:
    print('X')
elif x == 50:
    print('L')
elif x == 100:
    print('C')
elif x == 500:
    print('D')
elif x == 1000:
    print('M')
else: print('ошибка')

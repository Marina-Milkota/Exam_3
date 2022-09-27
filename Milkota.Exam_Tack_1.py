# 1. Напишите функцию, которая запрашивает у пользователя номер карты, CVC-код и PIN-код.
# После этого выводит на экран номер карты с первыми четырьмя цифрами, остальные заменены на звездочки,
# CVC-код в виде ###, и PIN-код в виде &&&0 (вместо 0 последняя цифра).

def card_number(n,c,p):
    print('Номер карты: ',n[:4]+('#'*len(n[4:])))
    print('CVC-код: ###')
    print('PIN-код: ','&&&' + p[-1])
while True:
    numb_card=input('Введите номер карты(16 цифр): ')
    if len(numb_card)!=16:
        print('Номер карты введен не верно!Попробуйте еще раз!')
        continue
    cvc = input('Введите 3-хзначный CVC-код: ')
    if len(cvc)!=3:
        print('CVC-код карты введен не верно!Попробуйте еще раз!')
        continue
    pin = input('Введите PIN-код: ')
    if len(pin)!=4:
        print('PIN-код карты введен не верно!Попробуйте еще раз!')
        continue
    else:break

card_number(numb_card,cvc,pin)

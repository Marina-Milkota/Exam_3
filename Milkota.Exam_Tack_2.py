# 2. Напишите функцию, которая возвращает True, если введенный текст читается
# одинаково слева-направо и справа-налево.Иначе – False.

def text(stroka):
    if stroka==stroka[-1::-1]:print(True)
    else:print(False)

st=input('Введите строку: ')
text(st)
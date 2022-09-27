#3. Дописать классы Company, Programmer.

# ДЗ на вторник:
# Класс Company:
# 1. Создайте класс Company
# 2.Создайте статическое свойство levels, которое будет содержать (как словарь) все уровни квалификации программиста:
# 1:junior, 2:middle, 3:senior, 4:lead.
# 3.Создайте метод __init__(), внутри которого будут определены два динамических protected свойства: 1) _index - передается параметром и
# 2) _levels - принимает из словаря levels значение с ключом _index
# 4.Создайте метод _level_up(), который будет переводить программиста на следующий уровень
# 5. Создайте метод is_lead(), который будет проверять, что программист достиг последней квалификации

class Company:
    levels={1: "junior", 2: "middle", 3: "senior", 4: "lead"}
    def __init__(self,index):
        if index > 4 : index = 4
        self._index= index
        self._levels= self.levels[self._index]

    def _level_up(self):
        if self._index != 4:
            self._index += 1
            self._levels = self.levels[self._index]
            print(f'Ваш уровень: {self._levels}')

    def is_lead(self):
        if self._index==4:print('Достигнут максимальный уровень!')
        else:
            print('Ваш уровень: ', self.levels[self._index] , '. Поработайте еще!')
            return self._index == 4

# Класс Programmer:
# 1. Создайте класс Programmer
# 2. Создайте метод __init__(), внутри которого будут определены два динамических свойства:
# 1) name - передается параметром, является публичным и
# 2) _level – уровень квалификации на основе словаря из Company
# 3. Создайте метод work(), который заставляет программиста работать, что позволяет ему становиться
# более квалифицированным с помощью метода _level_up()
# 4. Создайте статический метод knowledge_base(), который выведет в консоль справку по программированию.

class Programmer(Company):
    def __init__(self, name, ur):
        super().__init__(ur)
        self.name = name

    def work(self):
        self._level_up()

    @staticmethod
    def knowledge_base():
        print(Company.levels)

# Тесты:
# 1.Вызовите справку по программированию
# 2.Создайте объекты классов Company, Programmer
# 3.Используя объект класса Programmer, повысьте свой уровень квалификации
# 4.Дойдите до уровня lead

test_C=Company(1)
test_P=Programmer('Petr',2)
test_P.knowledge_base()
print(test_P.work())

while test_P.is_lead() == False:
     test_P._level_up()

test_C._level_up()
test_P.is_lead()


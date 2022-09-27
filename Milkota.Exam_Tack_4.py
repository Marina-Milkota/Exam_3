# 4. Создайте класс на тему животных. Используйте статические и динамические переменные,
# дочерний (1 или более) классов на конкретное животное.
# Публичные и приватные методы. Полиморфизм (одинаковые названия методов info в обоих классах,
# которые выводят информацию о животных, либо о конкретном животном данного класса).
# Создайте объекты каждого класса и обратитесь к каждому методу. Напишите один staticmethod,
# один classmethod, к которым также обратитесь.

class Animals:
    kol_male = 44
    kol_female = 30
    __vid = 'predators'
    def __init__(self,poroda):
        self.poroda=poroda

    def __private_method(self):
        print('Class method called')

    def insideclass(self):
        print("Private variable:", Animals.__vid)

    def info(self):
        print(f'Male: {self.kol_male}, Female: {self.kol_female}')

    @staticmethod
    def get_class_details():
        print('This is class Animals')

class Cats(Animals):
    kol_male = 5
    kol_female = 12
    def __init__(self,clor,vid):
        super().__init__(vid)
        self.color=clor

    def info(self):
        print(f'Male: {self.kol_male}, Female: {self.kol_female}')

    @staticmethod
    def get_class_details():
        print('This is class Cats')

    @classmethod
    def classmethod(cls):
        print('Cats have 4 paws')

class Dogs(Animals):
    kol_male = 6
    kol_female = 8
    def __init__(self, prd):
        super().__init__(prd)

    def info(self):
        print(f'Male: {self.kol_male}, Female: {self.kol_female}')

    def form_para(self):
        if self.kol_female<self.kol_male:print(f'We have {self.kol_female} couple of dogs')
        else:print(f'We have {self.kol_male} couple of dogs')

cat=Cats('grey','British')
birds=Animals('Tit')
dog=Dogs('Labrador')
print(cat.color)
print(cat.poroda)
print(birds.poroda)
cat.info()
birds.info()
dog.info()
birds.insideclass()
Animals.get_class_details()
Cats.get_class_details()
Cats.classmethod()
dog.form_para()


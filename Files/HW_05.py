#5.1.
#Создайте любой класс с произвольным количеством подклассов, экземпляров, атрибутов и методов
#- как минимум один атрибут должен быть с уровнем доступа private. Соответственно, для получания значений
# этого атрибута нужно использовать методы "get" и "set"
#5.2.
# Cоздайте репозиторий на Github и отправте файл с домашним заданием в этот удаленный репозиторий




class Plane:
    Category = 'Transport'
    def __init__(self, model, seats, color):
        self.model = model
        self._model = model
        self.seats = seats
        self.color = color

    def run(self):
        return "I'm a princess of the sky!"

    def get_model(self):
        return f'Hello! My name is {self.model}'

    def set_name(self, new_name):
        self._name = new_name

# создадим объект класса - plane
plane1 = Plane('Boeing 747-400', 423, 'white')
print(plane1.model)
print(plane1.get_model())
print(plane1.color)
print(plane1.seats)
print(plane1.Category)

dfsd
dsf



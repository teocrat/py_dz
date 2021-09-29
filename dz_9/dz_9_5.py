class Stationery:
    title = 'paper clip'

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    def draw(self):
        print('Пишем стихи')


class Pencil(Stationery):
    def draw(self):
        print('Рисуем картины')


class Handle(Stationery):
    def draw(self):
        print('Выделяем текст')


a = Stationery()
a.draw()
b = Pen()
b.draw()
c = Pencil()
c.draw()
d = Handle()
d.draw()

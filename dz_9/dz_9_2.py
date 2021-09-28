class Road:
    def __init__(self, _length, _width):
        self.lenght = _length
        self.width = _width

    def calc(self):
        ma = int((self.lenght * self.width * ma_1 * thick) / 1000)

        print(f'Масса асфальта для прокладки дороги: {ma} т')


ma_1 = int(input('Введите массу асфальта, необходимую для покрытия 1 кв. метра дороги толщиной в  1 см в кг: '))
thick = int(input('Введите толщину дорожного покрытия в см: '))
a = Road(5000, 20)
a.calc()

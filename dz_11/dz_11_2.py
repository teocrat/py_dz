class NoZero(Exception):

    def __init__(self, text):
        self.text = text


num = input('Введите делитель: ')

try:
    num = int(num)
    if num == 0:
        raise NoZero('Деление невозможно, делитель равен 0')
except(ValueError, NoZero) as err:
    print(err)
else:
    print('Продолжайте')

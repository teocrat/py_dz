class Woker:
    def __init__(self):
        self.name = input('Введите имя сотрудника: ')
        self.surname = input('Введите фамилию сотрудника: ')
        self.position = input('Введите должность сотрудника: ')
        wage = int(input('Введите оклад сотрудника: '))
        bonus = int(input('Введите премию сотрудника: '))
        self._income = {'wage': wage, 'bonus': bonus}


class Position(Woker):
    def get_full_name(self):
        print(f'Сотрудник: {self.name} {self.surname}\nДолжность: {self.position}')

    def get_total_income(self):
        total_income = sum(self._income.values())
        print(f'Общий доход сотрудника: {total_income} рублей')


a = Position()
a.get_full_name()
a.get_total_income()

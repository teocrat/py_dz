class OnlyNum:
    def __init__(self):
        list_int = []
        i = 0
        while i >= 0:
            self.data = input("Введите данные, если данных нет введите stop: ")
            if self.data == 'stop':
                print(list_int)
                break

            try:
                list_int.append(int(self.data))
            except ValueError as err:
                print(f'Данные не числовые {err}')


a = OnlyNum()

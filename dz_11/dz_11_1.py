class Date:

    def __init__(self, d=0, m=0, y=0):
        self.d = d
        self.m = m
        self.y = y

    @classmethod
    def get_int_date(cls, date):
        d, m, y = map(int, date.split('.'))
        int_data = cls(d, m, y)
        return int_data

    @staticmethod
    def valid_date(date):
        d, m, y = map(int, date.split('.'))

        if m > 12:
            print('Недопустимый формат месяца')
        elif d > 28 and m == 2 or d > 30 and (m == 4 or m == 6 or m == 9 or m == 11) or d > 31 and (
                m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m == 12):
            print('Недопустимый формат дня')

        elif y < 1900 or y > 2100:
            print('Недопустимый формат года')
        else:
            print(f'{d:02d}.{m:02d}.{y}')


str_date = input('Введите дату в формате ДД.ММ.ГГГГ: ')
a = Date()
a.get_int_date(str_date)
a.valid_date(str_date)

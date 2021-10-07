import json


class Warehouse:
    with open('printers.csv', 'r', encoding='utf-8') as f:
        shelf_printers = json.load(f)

    with open('scanners.csv', 'r', encoding='utf-8') as f:
        shelf_scanners = json.load(f)

    with open('copiers.csv', 'r', encoding='utf-8') as f:
        shelf_copiers = json.load(f)

    with open('inv_num.csv', 'r', encoding='utf-8') as f:
        inv_num = json.load(f)

    with open('accounts_department.csv', 'r', encoding='utf-8') as f:
        accounts_department = json.load(f)

    with open('management.csv', 'r', encoding='utf-8') as f:
        management = json.load(f)

    with open('administration.csv', 'r', encoding='utf-8') as f:
        administration = json.load(f)


class OfficeEquipment:

    def __init__(self):
        n = 0
        while n >= 0:
            self.type = input('Введите  тип оргтехники\n принтер - 1, сканер - 2, копир - 3: ')
            if self.type != "1" and self.type != "2" and self.type != "3":
                print('Введен неверный номер меню')
            else:
                break

        self.name = input('Введите модель  оргтехники: ')
        self.num = input('Введите инвентарный номер оргтехники: ')

    def move_warehouse(self):
        if self.num not in Warehouse.inv_num:
            Warehouse.inv_num.append(self.num)

            if self.type == '1':
                Warehouse.shelf_printers.setdefault(self.num, self.name)
                with open('printers.csv', 'r+', encoding='utf-8') as f:
                    json.dump(Warehouse.shelf_printers, f)

                with open('inv_num.csv', 'w', encoding='utf-8') as f:
                    json.dump(Warehouse.inv_num, f)

            elif self.type == '2':
                Warehouse.shelf_scanners.setdefault(self.num, self.name)
                with open('scanners.csv', 'r+', encoding='utf-8') as f:
                    json.dump(Warehouse.shelf_scanners, f)

                with open('inv_num.csv', 'w', encoding='utf-8') as f:
                    json.dump(Warehouse.inv_num, f)

            elif self.type == '3':
                Warehouse.shelf_copiers.setdefault(self.num, self.name)
                with open('copiers.csv.', 'r+', encoding='utf-8') as f:
                    json.dump(Warehouse.shelf_copiers, f)

                with open('inv_num.csv', 'w', encoding='utf-8') as f:
                    json.dump(Warehouse.inv_num, f)

        else:
            print('Такой инвентарный номер уже существует')


def move_division():
    i = 0
    while i >= 0:
        n = input('Переместить выбранную оргтехнику в подразделение(y/n): ')
        if n == 'y':
            k = input('Выбирите подразделение (бухгалтерия - 1, управление - 2, администрация - 3): ')
            v = input('Укажите инв. номер перемещаемого аппарата: ')

            if v in Warehouse.shelf_printers:
                d = Warehouse.shelf_printers[v]
                Warehouse.shelf_printers.pop(v)
                with open('printers.csv', 'w', encoding='utf-8') as f:
                    json.dump(Warehouse.shelf_printers, f)
            elif v in Warehouse.shelf_scanners:
                d = Warehouse.shelf_scanners[v]
                Warehouse.shelf_scanners.pop(v)
                with open('scanners.csv', 'w', encoding='utf-8') as f:
                    json.dump(Warehouse.shelf_scanners, f)
            elif v in Warehouse.shelf_copiers:
                d = Warehouse.shelf_copiers[v]
                with open('copiers.csv', 'w', encoding='utf-8') as f:
                    json.dump(Warehouse.shelf_copiers, f)
            if k == '1':
                Warehouse.accounts_department.setdefault(v, d)
                with open('accounts_department.csv', 'r+', encoding='utf-8') as f:
                    json.dump(Warehouse.accounts_department, f)
            elif k == '2':
                Warehouse.management.setdefault(v, d)
                with open('management.csv', 'r+', encoding='utf-8') as f:
                    json.dump(Warehouse.management, f)
            elif k == '3':
                Warehouse.administration.setdefault(v, d)
                with open('administration.csv', 'r+', encoding='utf-8') as f:
                    json.dump(Warehouse.administration, f)

        else:
            break


class Printer(OfficeEquipment):
    @staticmethod
    def count_printers():
        return len(Warehouse.shelf_printers)


class Scanner(OfficeEquipment):
    @staticmethod
    def count_scanners():
        return len(Warehouse.shelf_scanners)


class Copier(OfficeEquipment):
    @staticmethod
    def count_copiers():
        return len(Warehouse.shelf_copiers)


i = 0
while i >= 0:
    s = input('Вы хотите добавить оргтехнику на склад? y/n:  ')
    if s == 'y':
        a = Printer()
        a.move_warehouse()
        s = input('Продолжить? y/n: ')
        if s == 'y':
            b = Scanner()
            b.move_warehouse()
        else:
            break

        s = input('Продолжить? y/n: ')
        if s == 'y':
            c = Copier()
            c.move_warehouse()
        else:
            break
    else:
        break

move_division()
print(f'Количество принтеров на складе: {Printer.count_printers()} шт.')
print(f'Количество сканеров на складе: {Scanner.count_scanners()} шт.')
print(f'Количество копиров на складе: {Copier.count_copiers()} шт.')
count = Printer.count_printers() + Scanner.count_scanners() + Copier.count_copiers()
print(f'Общее количество оборудования на складе: {count} шт.')

print(Warehouse.shelf_printers)
print(Warehouse.shelf_scanners)
print(Warehouse.shelf_copiers)

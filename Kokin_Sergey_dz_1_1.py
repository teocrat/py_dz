# 1.Реализовать вывод информации о промежутке времени в зависимости от его продолжительности duration в секундах
duration = int(input('Введите продолжительность времени в  секундах: '))

s = duration % 60
m = duration // 60
h = duration // 3600
d = duration // 86400

if m > 60:
    m = m % 60

if h > 24:
    h = h % 24

print(f'Промежуток времени равен {d} дней, {h} часов, {m} минут, {s} секунд')
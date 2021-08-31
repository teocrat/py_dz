perc = []
for i in range(1, 101):
    perc.append(i)

for n in perc:
    if n > 4 and n < 21:
        print(n, ' процентов')
    elif n % 10 == 1:
        print(n, ' процент')

    elif n % 10 == 2 or n % 10 == 3 or n % 10 == 4:
        print(n, ' процента')
    else:
        print(n, ' процентов')

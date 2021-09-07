prices = [23.50, 67, 34.24, 89.20, 80, 66.05, 132.87, 102.56, 75.03, 43.70, 56, 76.08]

print('-' * 100)
print('A')

for x in prices:
    kk = f"{x % 1:.02f}".split('.')[-1]
    print(f"{int(x):02d}", 'руб', kk, 'коп, ', end=" ")

print(f"\n{ '_' * 100} ")
print('B')

print(id(prices))
prices.sort()
print(prices)
print(id(prices))

print('-' * 100)
print('C')

rev_list = reversed(prices)
print(list(rev_list))

print('-' * 100)
print('D')

print(prices[-5:])







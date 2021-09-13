from sys import argv
from utils_4_4 import currency_rates

if __name__ == '__main__':
    cur = argv[1]

    print(currency_rates(cur))

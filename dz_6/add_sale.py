from sys import argv

buy = argv[1]

with open('bakery.csv', 'a', encoding='utf-8') as f:
    f.write(buy + '\n')


from requests import get, utils

cur = input('Введите условное обозначение валюты: ')


def currency_rates(cur):

    response = utils.get_unicode_from_response(get('http://www.cbr.ru/scripts/XML_daily.asp'))
    content = response.split('<Valute ID=')
    for n in content:
        if cur.upper() in n:
            return float(n.replace('/', '').split('<Value>')[-2].replace(',', '.'))


print(currency_rates(cur))

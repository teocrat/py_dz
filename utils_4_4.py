from requests import get, utils


def currency_rates(cur):
    response = utils.get_unicode_from_response(get('http://www.cbr.ru/scripts/XML_daily.asp'))
    content = response.split('<Valute ID=')
    for n in content:
        if cur.upper() in n:
            return float(n.replace('/', '').split('<Value>')[-2].replace(',', '.'))


if __name__ == '__main__':
    print(currency_rates("eur"))

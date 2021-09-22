import re


def email_parse(email_adress):
    RE_RARSE_USER = re.compile(r'([\w\d]{6,30})\@')
    RE_RARSE_DOMAIN = re.compile(r'\@([\w \d]{2,63}\.\w{2}$)')

    user = RE_RARSE_USER.findall(email_adress)
    domain = RE_RARSE_DOMAIN.findall(email_adress)
    for i in user:
        for n in domain:
            email_dict = {'username': i, 'domain': n}
    try:
        assert RE_RARSE_USER.findall(email_adress)
        assert RE_RARSE_DOMAIN.findall(email_adress)
    except:
        raise ValueError('Некорректно введен email: ' + email_adress)

    return print(email_dict)


if __name__ in '__main__':
    email_parse("someone@geekbrains.ru")
    email_parse("someone@geekbrainsru")

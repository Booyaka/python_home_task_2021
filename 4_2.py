from requests import get, utils


def currency_rates(valute):
    my_list = content.split('<Valute')
    for i in my_list:
        if valute.upper() in i:
            value = i[i.find('Value') + 6:i.find('Value') + 13]
            val = float(value.replace(',', '.'))
            print(val, type(val))


response = get('http://www.cbr.ru/scripts/XML_daily.asp')
encodings = utils.get_encoding_from_headers(response.headers)
content = response.content.decode(encoding=encodings)

currency_rates('USD')
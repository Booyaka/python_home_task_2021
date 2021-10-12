from requests import get, utils
from datetime import date


def currency_rates(valute):
    my_list = content.split('<Valute')
    for i in my_list:
        if valute.upper() in i:
            value = i[i.find('Value') + 6:i.find('Value') + 13]
            val = float(value.replace(',', '.'))
            print(f'{valute}: {val}, {type(val)}')
        elif 'Date' in i:
            date_response = i[i.find('Date=') + 6:i.find('Date=') + 16]
            day = int(date_response[:2])
            month = int(date_response[3:5])
            year = int(date_response[6:10])
            result = date(year, month, day)
            print(f'Date: {result}, {type(result)}')


response = get('http://www.cbr.ru/scripts/XML_daily.asp')
encodings = utils.get_encoding_from_headers(response.headers)
content = response.content.decode(encoding=encodings)

if __name__ == '__main__':
    currency_rates('USD')
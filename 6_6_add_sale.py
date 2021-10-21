from sys import argv


def add_sale(args):
    with open('bakery.csv', 'a', encoding='utf-8') as f:
        f.write(f'{args}\n')


_, sales = argv

if __name__ == '__main__':
    add_sale(sales)
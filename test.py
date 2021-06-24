from beautifultable import BeautifulTable


company_name = 'Alex'
company_address = '20 Sol st'
company_city = 'Netanya'
message = 'Thank you for shopping with us!'


def store():
    print('*' * 50)
    print(f'\t\t{company_name.title()}')
    print(f'\t\t{company_address.title()}')
    print(f'\t\t{company_city.title()}')
    products = []
    product_price = []
    is_buying = True

    dict = {
        'pc': 100,
        'book': 25,
        'pen': 5,
        'paper': 30,
        'laptop': 200,
        'screen': 400
    }

    while is_buying:
        a = input("Enter product name: ")
        if a in dict:
            products.append(a)
            product_price.append(dict[a])
        else:
            print("Not such product...")
        buy_more = input('Anything else? Y/N')
        if buy_more == 'Y'.lower():
            continue
        elif buy_more == 'N'.lower():
            print('Check out price')
            is_buying = False
        else:
            print('Invalid input')

    if not is_buying:
        print('*' * 50)
        print(f'\t\t Products')
        table = BeautifulTable()
        table.column_headers = ["Product", "Price"]
        for product in products:
            table.append_row([product,  f'{dict[product]}$'])
        print(table)
        print('=' * 50)
        print(f'\t\tTotal price: {sum(product_price)}$')

        print('\t', message)
        print('*' * 50)


store()
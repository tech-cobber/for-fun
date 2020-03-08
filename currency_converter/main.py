from currency_converter.currency import Currency


def run():
    rub_default = Currency(100)
    rub = Currency(500, 'RUB')
    usd = Currency(100, 'USD')
    eur = Currency(1, 'EUR')
    chf = Currency(10, 'CHF')
    gbr = Currency(3, 'GBP')

    test = f'\n{rub_default}\n\
{rub}\n{usd}\n{eur}\n{chf}\n{gbr}\n\
{rub_default} + {rub} = {rub_default + rub}\n\
{usd} - {rub} = {usd - rub}\n\
{eur} - {chf} = {eur - chf}\n\
{rub} + {gbr} = {rub + gbr}\n\
{rub} + 333 = {rub + 333}\n'
    print(test)
    print(f'repr -> {rub.__repr__()}\n')

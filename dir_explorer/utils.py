import re
from random import random
from collections import Counter


def count_pages_pdf(filename: str = r'static/example.pdf'):
    with open(filename, 'rb') as f:
        data = f.read()
    page = b'/Type /Page '
    page_count = len(re.findall(page, data))
    print(page_count)


def genetate_0_1(size: int = 10):

    def one_or_zero(rand: float) -> str:
        if rand > 0.5:
            return '1'
        else:
            return '0'
    matrix = [
        [one_or_zero(random()) for i in range(size)]
        for i in range(size)]
    text = [' '.join(row) for row in matrix]
    with open('static/ones_zeros', 'w') as f:
        f.write('\n'.join(text))


def count_zeros(filename: str = 'static/ones_zeros'):
    with open('static/ones_zeros', 'r') as f:
        text = f.read()
    counter = Counter(text)
    zeros = counter.get('0')
    if zeros:
        print(f"There are {zeros} free places at the time")
    else:
        print(f"All the places are occupied")


def is_free(row: int, col: int,
            filename: str = 'static/ones_zeros'):
    with open('static/ones_zeros', 'r') as f:
        text = f.read()
    lines = text.split('\n')
    if lines[row - 1][2 * (col - 1)] == '0':
        print('This place is free!')
    else:
        print("It's occupied :C")


if __name__ == "__main__":
    # count_pages_pdf()
    genetate_0_1()
    count_zeros()
    is_free(10, 10)

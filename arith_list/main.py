from arith_list.arith_list import ArithList


def run():
    left_term = ArithList([0, 1, 2, 1, 2, 2])
    right_term = ArithList([3, 1, 1, 1, 1, 1])
    result = left_term + right_term
    print(result)
    print(left_term)
    print(right_term)
    result = right_term - left_term
    print(result)

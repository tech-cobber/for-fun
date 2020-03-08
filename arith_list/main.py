from arith_list.arith_list import ArithList


def run():
    left_term = ArithList([0, 1, 2, 1])
    right_term = ArithList([3, 1, 2, 4, 8, 1])
    test = f"\nleft: {left_term}\nright: {right_term}\n\n\
+: {left_term + right_term}\n\
-: {left_term - right_term}\n\
>: {left_term > right_term}\n\
<: {left_term < right_term}\n\
==: {left_term == right_term}\n\
!=: {left_term != right_term}\n\
>=: {left_term >= right_term}\n\
<=: {left_term <= right_term}\n"
    print(test)

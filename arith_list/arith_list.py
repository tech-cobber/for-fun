from typing import Tuple


class ArithList(list):
    """ This class overrides some arithmetic methods
     and comparators from list"""

    def make_equal(self, term: list) -> Tuple[bool, list]:
        """ True means extended self and False stands for term"""
        diff = self.__len__() - len(term)
        if not diff:
            extended = term.copy()
            return False, extended
        elif (diff < 0):
            extended = self.__getitem__(
                slice(self.__len__())
                )
            extended.extend(
                [0 for _ in range(abs(diff))]
            )
            return True, extended
        else:
            extended = term.copy()
            extended.extend(
                [0 for _ in range(diff)]
            )
            print(extended)
            return False, extended

    def sum(self):
        return sum(
            self.__getitem__(
                slice(self.__len__())
                )
            )

    def __add__(self, term: list) -> list:
        self_extended, extended = self.make_equal(term)
        if self_extended:
            result = list(map(lambda a, b: a + b, term, extended))
        else:
            result = [
                self.__getitem__(idx) + extended[idx]
                for idx in range(len(extended))
            ]
        return result

    def __sub__(self, term: list) -> list:
        self_extended, extended = self.make_equal(term)
        if self_extended:
            result = list(map(lambda a, b: a - b, term, extended))
        else:
            result = [
                self.__getitem__(idx) - extended[idx]
                for idx in range(len(extended))
            ]
        return result

    def __lt__(self, term: list) -> bool:
        return self.sum() < sum(term)

    def __le__(self, term: list) -> bool:
        return self.sum() <= sum(term)

    def __eq__(self, term: list) -> bool:
        return self.sum() == sum(term)

    def __ne__(self, term: list) -> bool:
        return self.sum() != sum(term)

    def __gt__(self, term: list) -> bool:
        return self.sum() > sum(term)

    def __ge__(self, term: list) -> bool:
        return self.sum() >= sum(term)

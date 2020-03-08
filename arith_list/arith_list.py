class ArithList(list):
    """ This class overrides some arithmetic methods
     and comparators from list"""

    def make_equal(self, term: list) -> None:
        diff = self.__len__() - len(term)
        if not diff:
            return None
        elif (diff < 0):
            super().extend(
                [0 for _ in range(abs(diff))]
            )
        else:
            term.extend(
                [0 for _ in range(diff)]
            )

    def sum(self):
        return sum(
            self.__getitem__(
                slice(self.__len__())
                )
            )

    def __add__(self, term: list) -> list:
        self.make_equal(term)
        result = [
            super(ArithList, self).__getitem__(idx) + term[idx]
            for idx in range(len(term))
        ]
        return result

    def __sub__(self, term: list) -> list:
        self.make_equal(term)
        result = [
            super(ArithList, self).__getitem__(idx) - term[idx]
            for idx in range(len(term))
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

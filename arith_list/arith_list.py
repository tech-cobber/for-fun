class ArithList(list):
    """ This class overrides some arithmetic methods
     and comparators from list"""

    def make_equal(self, term: list) -> None:
        diff = super().__len__() - len(term)
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

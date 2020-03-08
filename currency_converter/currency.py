from __future__ import annotations
from typing import Union
import yaml


def get_rate() -> dict:
    rate = {}
    with open("currency_converter/rate.yaml", 'rt') as stream:
        try:
            rate = yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(exc)
    return rate


rate = get_rate()


class Currency():
    __slots__ = 'name', 'value'

    def __init__(self, value, name='RUB'):
        self.name = name
        self.value = value

    def get_converted(self, term: Currency) -> float:
        if (self.name == term.name):
            return term.value
        else:
            return term.value * rate[term.name][self.name]

    def __add__(self, term: Union[int, float, Currency]) -> Currency:
        instance = object.__new__(Currency)
        if isinstance(term, Currency):
            value = self.value + self.get_converted(term)
            instance.value, instance.name = value, self.name
        else:
            value = self.value + term
            instance.value, instance.name = value, self.name
        return instance

    def __sub__(self,
                term: Union[int, float, Currency]) -> Union[Currency, str]:
        instance = object.__new__(Currency)
        if isinstance(term, Currency):
            value = self.value - self.get_converted(term)
            if value > 0:
                instance.value, instance.name = value, self.name
            else:
                return f"You will have {value} {self.name}. Sure about that?"
        else:
            value = self.value - term
            instance.value, instance.name = value, self.name
        return instance

    def __str__(self) -> str:
        return f'{self.value} {self.name}'

    def __repr__(self):
        return f'{self.__module__}.Currency({self.name}, {self.value})'

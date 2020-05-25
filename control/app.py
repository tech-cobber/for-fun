from typing import List
from functools import reduce
from .utils import logging, profile


@profile
@logging
def multiply_short(data: List[int]) -> List[int]:
    if data:
        result = [
            reduce(lambda mul, this: mul * this
                   if this != element else mul,
                   data)
            for element in data if element
        ]
    else:
        result = []
    return result


@profile
@logging
def multiply(data: List[int]) -> List[int]:

    @logging
    def func(data: List[int], element: int) -> int:
        accum = 1
        for i in data:
            if i != element:
                accum *= i
        return accum

    result = []
    for element in data:
        result.append(func(data, element))
    return result


@logging
def multiply_linear_time(data: List[int]) -> List[int]:
    if 0 in data:
        raise ValueError("There is zero in the array! x * 0 is 0 you know?")
    result = []
    left = 1
    for i in range(len(data)):
        result.append(left)
        left = left * data[i]
    right = 1
    for i in range(len(data) - 1, -1, -1):
        result[i] = right * result[i]
        right = right * data[i]
    return result


def mocking():
    ''' For mocking use only '''
    return multiply([i for i in range(10_000_000)])

from loguru import logger
from typing import List


def logging(func):

    def wrapper(*args, **kwargs) -> List[int]:
        if func.__name__ == 'func':
            data, element = args
            result: List[int] = func(*args, **kwargs)
            logger.debug(f'Computed multiplication of {data} without {element} -> {result}')
            return result
        elif func.__name__ == 'multiply':
            data: List[int] = args[0]
            if data:
                if not isinstance(data, list):
                    logger.error(f'Expected list: but found {type(data)}')
                    raise ValueError(f'Expected list: but found {type(data)}')
                logger.debug(f'Passed list: {data}')
                result: List[int] = func(*args, **kwargs)
                logger.info(f'Finished processing with result: {result}')
                return result
            else:
                logger.error(f"List can't be empty!")
                raise ValueError("List can't be empty!")
        else:
            logger.warning(f'Dunno how to log function {func.__name__} :C')
            result = func(*args, **kwargs)
            logger.info(f'Finished processing {func.__name__} with result: {result}')
            return result

    return wrapper

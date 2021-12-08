from functools import wraps
from typing import Optional

import cache


def decorator(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)

    # wrapper.__name__ = fn.__name__
    # wrapper.__doc__ = fn.__doc__
    return wrapper


@decorator
def test(arg1: str, arg2) -> Optional[list]:
    """
    Общее описание

    Примеры кода

    :param arg1: Описание параметра
    :param arg2:
    :return:
    """
    ...


@decorator
def test2(arg1, arg2):
    """ Краткое описание """
    ...


print(f"Я вызываюсь при импорте и выполнении скрипта {__name__}")
if __name__ == '__main__':
    print(test.__name__)
    print(test.__doc__)

    help(test)

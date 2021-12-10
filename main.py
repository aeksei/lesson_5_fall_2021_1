import os
import json
from typing import Union

import requests

import docstring


INDENT = 4


def main():
    print(print_json_string([1, 2, 3]))


def print_json_string(obj: Union[list, dict]) -> str:
    return json.dumps(obj, indent=INDENT)


if __name__ == '__main__':
    main()

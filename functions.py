import re
from typing import Iterator


def file_data(filename: str) -> Iterator[str]:
    with open('data/' + filename, 'r', encoding='utf-8') as file:
        for line in file:
            yield line.strip()


def filter_lines(lines: str, value: str) -> filter:
    return filter(lambda line: value in line, lines)


def map_lines(lines: str, column: int) -> map:
    column = int(column)
    return map(lambda line: line.split()[column], lines)


def unique_lines(lines: str, value: str) -> set:
    return set(lines)


def sort_lines(lines: str, reverse: bool) -> list:
    return sorted(lines, reverse=True if reverse == 'desc' else False)


def limit_lines(lines: str, value: int) -> list:
    value = int(value)
    return list(lines)[:value]


def regex(lines: str, value: str) -> list:
    reg_ex = re.compile(f'({value})')
    return reg_ex.findall(lines)

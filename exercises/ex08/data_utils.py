"""Dictionary related utility functions."""

__author__ = "730471018"

from csv import DictReader

DATA_DIRECTORY = "../../data"
DATA_FILE_PATH = f"{DATA_DIRECTORY}/nc_durham_2015_march_21_to_26.csv" 


def read_csv_rows(file_name: str) -> list[dict[str, str]]:
    """Read the rows of a csv into a table."""
    result: list[dict[str, str]] = []

    file_handle = open(file_name, "r", encoding="utf8")

    csv_reader = DictReader(file_handle)
    for row in csv_reader:
        result.append(row)

    file_handle.close()

    return result


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Produces a list[str] of all values in a single column."""
    result: list[str] = []
    for row in table:
        item: str = row[column]
        result.append(item)
    return result


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform a row-oriented table to a column-oriented table."""
    result: dict[str, list[str]] = {}
    first_row: dict[str, str] = row_table[0]
    for column in first_row:
        result[column] = column_values(row_table, column)
    return result


def head(column_table: dict[str, list[str]], n_rows: int) -> dict[str, list[str]]:
    """Return column-based table that only contains n number of rows of data."""
    result: dict[str, list[str]] = {}
    if n_rows >= len(column_table):
        return column_table 
    for string in column_table:
        if n_rows == 0:
            result[string] = []
        else:
            i: int = 0
            while i < n_rows:
                n_list: list[str] = []
                idx: int = 0
                while idx < n_rows:
                    n_list.append(column_table[string][idx])
                    idx += 1
                result[string] = n_list
                i += 1
    return result


def select(og_table: dict[str, list[str]], column_names: list[str]) -> dict[str, list[str]]:
    """Returns columb-based table that contains a specific subset of original table."""
    result: dict[str, list[str]] = {}
    for name in column_names:
        result[name] = og_table[name]
    return result


def concat(table_1: dict[str, list[str]], table_2: dict[str, list[str]]) -> dict[str, list[str]]:
    """Returns a column-based table that combines the two given column-based tables."""
    result: dict[str, list[str]] = {}
    for column in table_1:
        result[column] = table_1[column]
    for column in table_2:
        if column in result:
            result[column] += table_2[column]
        else:
            result[column] = table_2[column]
    return result


def count(input_list: list[str]) -> dict[str, int]:
    """Returns a dictionary that counts the frequency of each item in the inputted list."""
    result: dict[str, int] = {}
    for item in input_list:
        if item in result:
            result[item] += 1
        else: 
            result[item] = 1
    return result

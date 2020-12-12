from typing import List
from utils.file_utils import read_input_data, write_output_data


def find_start_and_end_of(string: str, substring: str) -> List:
    substring_borders = []
    string_length = len(string)
    substring_length = len(substring)
    if substring_length == 0:
        return substring_borders
    for string_index in range(string_length - substring_length + 1):
        for substring_index in range(substring_length):
            if string[string_index + substring_index] != substring[substring_index]:
                break
        else:
            substring_borders.append((string_index, string_index + substring_length - 1))
    return substring_borders


if __name__ == "__main__":
    input_string, substring_to_find = read_input_data()
    substring_coordinates = find_start_and_end_of(input_string, substring_to_find)
    write_output_data(substring_coordinates)

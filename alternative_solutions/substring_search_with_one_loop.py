from typing import List


def find_start_and_end_of(string: str, substring: str) -> List:
    substring_borders = []
    string_length = len(string)
    substring_length = len(substring)
    substring_index = 0
    string_index = 0
    if substring_length == 0:
        return substring_borders
    while string_index < string_length:
        if string[string_index] == substring[substring_index]:
            substring_index += 1
        else:
            string_index -= substring_index
            substring_index = 0
        if substring_index == substring_length:
            substring_borders.append((string_index - substring_length + 1, string_index))
            string_index -= substring_index - 1
            substring_index = 0
        string_index += 1
    return substring_borders

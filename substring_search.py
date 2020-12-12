from typing import List

INPUT_FILE_NAME = "strings.in"
OUTPUT_FILE_NAME = "strings.out"


def read_input_data() -> List:
    with open(INPUT_FILE_NAME, "r") as input_file:
        return input_file.readlines()


def write_output_data(substring_borders: List) -> None:
    with open(OUTPUT_FILE_NAME, "w") as output_file:
        output_file.write(str(substring_borders))


def find_start_and_end_of(string: str, substring: str) -> List:
    substring_borders = []
    string_length = len(string)
    substring_length = len(substring)
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

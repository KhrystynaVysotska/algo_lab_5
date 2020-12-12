from typing import List

INPUT_FILE_NAME = "strings.in"
OUTPUT_FILE_NAME = "strings.out"


def read_input_data() -> List:
    with open(INPUT_FILE_NAME, "r") as input_file:
        return input_file.read().splitlines()


def write_output_data(substring_borders: List) -> None:
    with open(OUTPUT_FILE_NAME, "w") as output_file:
        output_file.write(str(substring_borders))
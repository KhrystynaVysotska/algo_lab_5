import unittest
from substring_search import find_start_and_end_of


class BruteForceAlgorithmTest(unittest.TestCase):
    def test_substring_not_found(self):
        input_string = "aabaabaabaabaabaabaab"
        input_substring = "aaab"
        substring_borders = find_start_and_end_of(input_string, input_substring)
        self.assertEqual([], substring_borders)

    def test_substring_one_entry(self):
        input_string = "aaaaaaaaaawkjwkawkjlwjalawklaa"
        input_substring = "wjal"
        substring_borders = find_start_and_end_of(input_string, input_substring)
        self.assertEqual([(20, 23)], substring_borders)

    def test_substring_many_sequential_entries(self):
        input_string = "aaaaaa"
        input_substring = "aaa"
        substring_borders = find_start_and_end_of(input_string, input_substring)
        self.assertEqual([(0, 2), (1, 3), (2, 4), (3, 5)], substring_borders)

    def test_substring_many_entries(self):
        input_string = "asaskdasaasjdasaasacscaaasscaaasslassaccaaas"
        input_substring = "aas"
        substring_borders = find_start_and_end_of(input_string, input_substring)
        self.assertEqual([(8, 10), (15, 17), (23, 25), (29, 31), (41, 43)], substring_borders)

    def test_substring_in_sentence(self):
        input_string = "The ants enjoyed the barbecue more than the family."
        input_substring = "the"
        substring_borders = find_start_and_end_of(input_string, input_substring)
        self.assertEqual([(17, 19), (40, 42)], substring_borders)

    def test_empty_substring(self):
        input_string = "abcd"
        input_substring = ""
        substring_borders = find_start_and_end_of(input_string, input_substring)
        self.assertEqual([], substring_borders)

    def test_long_substring(self):
        input_string = "abcd"
        input_substring = "abc"
        substring_borders = find_start_and_end_of(input_string, input_substring)
        self.assertEqual([(0, 2)], substring_borders)

    def test_many_entries_of_one_letter(self):
        input_string = "bbbb"
        input_substring = "b"
        substring_borders = find_start_and_end_of(input_string, input_substring)
        self.assertEqual([(0, 0), (1, 1), (2, 2), (3, 3)], substring_borders)


if __name__ == '__main__':
    unittest.main()

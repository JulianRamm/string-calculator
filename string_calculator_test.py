import unittest
from string_calculator import StringCalculator
from exceptions import NegativesNotAllowed


class TestStringCalculator(unittest.TestCase):

    def setUp(self):
        """Set up test fixtures."""
        self.calculator = StringCalculator()

    def test_calculate_sum_with_empty_string(self):
        self.assertEqual(self.calculator.add(""), 0)

    def test_calculate_sum_with_one_number(self):
        self.assertEqual(self.calculator.add("2"), 2)

    def test_calculate_sum_with_two_numbers(self):
        self.assertEqual(self.calculator.add("2,5"), 7)

    def test_calculate_sum_with_n_numbers(self):
        self.assertEqual(self.calculator.add("2,5,0,3,10"), 20)

    def test_when_new_lines_in_input_string_accept_them_and_sum_accordinly(self):
        self.assertEqual(self.calculator.add("3\n4,6\n1"), 14)

    def test_when_pass_any_delimiter_it_should_return_normal_sum(self):
        self.assertEqual(self.calculator.add("//;\n2;1;2"), 5)
        
    def test_when_sum_negative_numbers(self):
        with self.assertRaises(NegativesNotAllowed):
            self.calculator.add("-1,3")

    def test_when_any_number_is_greater_than_1000_ignore_it_when_summing(self):
        self.assertEqual(self.calculator.add("//;\n2000;1;2"), 3)

    def test_when_pass_any_length_as_delimiter(self):
        self.assertEqual(self.calculator.add("//[****]\n2000****1****2****3"), 6)

    def test_when_pass_multiple_delimiters(self):
        self.assertEqual(self.calculator.add("//[*][%][&]\n2000*1%2&3"), 6)

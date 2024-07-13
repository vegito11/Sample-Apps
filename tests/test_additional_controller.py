# tests/test_additional_controller.py

import os
import unittest
from controllers.additional_controller import (
    calculate_sum, check_even, generate_sequence, greet
)

class TestAdditionalController(unittest.TestCase):

    def test_calculate_sum(self):
        result = calculate_sum(5, 10)
        self.assertEqual(result['result'], 15)

    def test_check_even(self):
        result = check_even(4)
        self.assertTrue(result['is_even'])

    def test_generate_sequence(self):
        result = generate_sequence(5)
        self.assertEqual(result['sequence'], [1, 2, 3, 4, 5])

    def test_greet(self):
        result = greet('Alice')
        self.assertEqual(result['message'], 'Hello, Alice!')

    def test_fail_calculate_sum(self):
        if os.getenv('FAIL_SUM_TEST', '').lower() == 'false':
            self.skipTest("Skipping test_calculate_sum due to environment variable setting.")

        result = calculate_sum(10, 20)
        self.assertEqual(result['result'], 40)

    def test_fail_check_even(self):
        if os.getenv('FAIL_EVEN_TEST', '').lower() == 'false':
            self.skipTest("Skipping test_check_even due to environment variable setting.")

        result = check_even(3)
        self.assertTrue(result['is_even'])

    def test_fail_generate_sequence(self):
        if os.getenv('FAIL_SEQUENCE_TEST', '').lower() == 'false':
            self.skipTest("Skipping test_generate_sequence due to environment variable setting.")

        result = generate_sequence(3)
        self.assertEqual(result['sequence'], [1, 2, 3, 4])

if __name__ == '__main__':
    unittest.main()

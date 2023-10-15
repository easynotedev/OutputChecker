import unittest
import os
import math
import traceback
from outputChecker import TestSourceCodes

class TestOutputChecker(unittest.TestCase):
   
    def setUp(self):
        self.test_source_codes = TestSourceCodes()
        print(f"Current working directory: {os.getcwd()}")

    def test_expected_is_source_code_output(self):
        result = self.test_source_codes.check_output( 'test-simple.py', 'expected-test_output.txt')
        result = math.ceil(result)
        self.assertEqual(result, 75)

    def test_expected_is_not_source_code_output(self):
        result = self.test_source_codes.check_output( 'test-simple.py', 'expected_output.txt')
        self.assertAlmostEqual(result, 4.16, 1)

    def test_expected_no_line_in_source_code_output(self):
        result = self.test_source_codes.check_output( 'no-source-code-line.py', 'no-expected-line.txt')
        self.assertAlmostEqual(result, 100)


if __name__ == '__main__':
    unittest.main()
   
    
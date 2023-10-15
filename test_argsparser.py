import unittest
import io
import sys
import argparse

class TestSourceCodes(unittest.TestCase):
    def test_output(self, source_file, expected_outputs_file):
        with open(args.source_file) as f:
            source_code = f.read()
        
        # Redirect stdout to a buffer
        stdout_ = sys.stdout  # Keep a reference to the original standard output
        sys.stdout = io.StringIO()
        # Run the source code and get its output
        exec(source_code)

        output = sys.stdout.getvalue()
        # Reset stdout to its original value
        sys.stdout = stdout_
        output_lines = output.split(',')
        print(f"Value outputted: {output_lines}")
        
        with open(args.expected_outputs_file) as f:
            content = f.read()
            expected_lines = [line.strip() for line in content.split(',')]
        print(f"Value expected : {expected_lines}")
        


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Test source code against expected output.')
    parser.add_argument('source_file', type=str, help='path to source code file')
    parser.add_argument('expected_outputs_file', type=str, help='path to file containing expected output lines')
    args = parser.parse_args()

    tester = TestSourceCodes()
    tester.test_output(args.source_file, args.expected_outputs_file)

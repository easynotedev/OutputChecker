import unittest
import io
import sys
from colour import Color
import argparse
import traceback

class TestSourceCodes(unittest.TestCase):
        def check_output(self, source_file, expected_outputs_file):
            with open(source_file) as f:
                source_code = f.read()
                # Redirect stdout to a buffer
                stdout_ = sys.stdout  # Keep a reference to the original standard output
                sys.stdout = io.StringIO()
                
                try:
                    # Create a dictionary to serve as local and global scope for exec()
                    exec_scope = {}
                    # Run the source code and get its output
                    exec(source_code, exec_scope, exec_scope)
                    output = sys.stdout.getvalue()
                    #Reset stdout to its original value
                    sys.stdout = stdout_

                    # Read the expected output from a file
                    with open(expected_outputs_file, 'r') as f:
                        content = f.read()
                    expected_lines = [line.strip() for line in content.split('\n')]
                    print(f"expected lines: {expected_lines}")
                    output_lines = output.split('\n')
                    print(f"output  lines: {output_lines}")
                    print("+=============================================================+")    
                    print("+===================+START-OF-LINE-CHECKER+===================+")
                    print("+=============================================================+")  
                    print(f"No.      output Lines: {len(output_lines)} ")
                    print(f"\033[92mNo. of expected Lines: {len(expected_lines)}\033[0m")
                    Total_Score = 0
                    
                    for i, expected_line in enumerate(expected_lines):
                        char_Score = 0
                        print(f"=================CHECKER-OUTPUT-LINE {i+1}=================")
                        print(f"\033[92mexpected line-char: {expected_line}\033[0m")
                        line_Score = 0
                        try:
                            print(f"  output line-char: {output_lines[i]}")
                            print(f"Expected line length: {len(expected_line)}")
                            print(f"  Output line length: {len(output_lines[i])}")
                            if (len(expected_line) == 0 and len(output_lines[i]) == 0):
                                print("**Same length of zero**")
                                line_Score = 1    
                            elif(len(expected_line) == 0 and len(output_lines[i]) != 0):
                                print("**expected_line has no length but out_lines has length**")
                                line_Score = 0
                            elif len(output_lines[i]) == 0:
                                print("**output_lines has no length**")
                                line_Score = 0
                            else:
                                diff = 0
                                for j, expected_char in enumerate(expected_line):   
                                    try:
                                        self.assertEqual(ord(expected_char), ord(output_lines[i][j]))
                                        #print("\033[92mTest passed in char.\033[0m")
                                        print(f"\033[92m{expected_char}\033[0m", end='')
                                        print(f"\033[92m{output_lines[i][j]}\033[0m")
                                        char_Score += 1/len(expected_line)
                                    except IndexError:
                                        char_Score += 0
                                    except AssertionError:
                                        #print("\033[91mTest failed in char.\033[0m")
                                        print(f"\033[92m{expected_char}\033[0m", end='')
                                        print(f"\033[91m {output_lines[i][j]}\033[0m") 
                                        char_Score += 0
                                    
                                print(f"character Score: {char_Score}")
                                diff = abs(len(output_lines[i]) - len(expected_line))
                                print(f"diffrnce line length: {diff}") 
                                print(f"length score: {len(output_lines[i]) / max(len(expected_line), len(output_lines[i]))}")
                                line_Score = char_Score * (len(output_lines[i]) / max(len(expected_line), len(output_lines[i])))
                            print(f"line_Score of Similarity per line: {line_Score:0.2f}")
                        except IndexError:
                            line_Score += 0                        
                        
                        Total_Score +=  line_Score
                    print("+=============================================================+")    
                    print("+====================+END-OF-LINE-CHECKER+====================+")
                    print("+=============================================================+")    
                    # Define the colors for the gradient
                    red = Color("red")
                    green = Color("green")

                    # Calculate the percentage of green in the gradient
                    percentage = (Total_Score / len(expected_lines)) * 100

                    # Get the color at the specified percentage
                    color = list(red.range_to(green, 101))[int(percentage)]

                    # Print the result in the specified color
                    print(f"\033[38;2;{int(color.red * 255)};{int(color.green * 255)};{int(color.blue * 255)}mTotal Line Score: {percentage:.2f}%\033[0m")
                except NameError as NamErr:
                        #Reset stdout to its original value
                        sys.stdout = stdout_
                        print(f"\033[91mSource file incorrect syntax or Runtime error occurred: \033[0m", NamErr)
                        print(traceback.format_exc())

            return percentage
        
if __name__ == '__main__':

        parser = argparse.ArgumentParser(description='Test source code against expected output.')
        parser.add_argument('source_file', type=str, help='path to source code file')
        parser.add_argument('expected_outputs_file', type=str, help='path to file containing expected output lines')
        args = parser.parse_args()

        tester = TestSourceCodes()
        tester.check_output(args.source_file, args.expected_outputs_file)


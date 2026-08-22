'''
import sys
input_file = sys.argv[1]
output_file = sys.argv[2]
print(f"Input: {input_file}\nOutput: {output_file}")
'''

import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--input", help="Input file path", required=True)
parser.add_argument("--min-salary", help="Minimum salary filter", type=int, required=False)
parser.add_argument("--output", help="Output file path", required=True)
args = parser.parse_args()
print(f"Input: {args.input}\nMinimum Salary: {args.min_salary}\nOutput: {args.output}")
import argparse, csv
from pathlib import Path

parser = argparse.ArgumentParser()
parser.add_argument("--input", help="Input file path", required=True)
parser.add_argument("--output", help="Output file path", required=True)
args = parser.parse_args()
input_file = Path(args.input)
output_file = Path(args.output)

if input_file.exists():
    with open(input_file, 'r') as input_f, open(output_file, 'w', newline='') as output_f:
        reader = csv.reader(input_f)
        writer = csv.writer(output_f)
        next(reader)  # Skip header
        writer.writerow(["name", "department", "salary"])
        for row in reader:
            name, dept, sal = row
            if dept == 'Data' and int(sal) > 70000:
                writer.writerow(row)
else:
    print(f"Error: The file {input_file} does not exist.")
    raise SystemExit(1)

import argparse, csv, logging
from pathlib import Path


def process_file(input_file, output_file):
    if input_file.exists():
        with open(input_file, 'r') as input_f, open(output_file, 'w', newline='') as output_f:
            logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s", filename="data/logs/logfile.log", filemode='a')
            cnt = 0
            invalid_records = 0
            reader = csv.reader(input_f)
            writer = csv.writer(output_f)
            next(reader)  # Skip header
            writer.writerow(["name", "department", "salary"])
            for row in reader:
                if len(row) != 3:
                    invalid_records += 1
                    logging.warning(f"Invalid record (wrong number of columns): {row}")
                    continue  # Skip rows that don't have exactly 3 columns
                name, dept, sal = row
                try:
                    sal = int(sal)  # Attempt to convert salary to integer
                except ValueError:
                    invalid_records += 1
                    continue  # Skip rows where salary is not a valid integer
                if dept == 'Data' and sal > 70000:
                    writer.writerow(row)
                    cnt += 1
    
    else:
        raise FileNotFoundError
    return cnt, invalid_records


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", help="Input file path", required=True)
    parser.add_argument("--output", help="Output file path", required=True)
    args = parser.parse_args()
    input_file = Path(args.input)
    output_file = Path(args.output)
    try:
        count, invalid_count = process_file(input_file, output_file)
        logging.info(f"Number of employees in Data department with salary > 70000: {count}")
        logging.info(f"Number of invalid records: {invalid_count}")
    except FileNotFoundError:
        logging.error(f"Error: The file {input_file} does not exist.")
        
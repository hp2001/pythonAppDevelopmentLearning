import csv

with open("data/employees.csv", "r") as input_file, open("data/output.csv", "w", newline="") as output_file:

    reader = csv.reader(input_file)
    writer = csv.writer(output_file)

    next(reader)

    writer.writerow(["name", "department", "salary"])

    for row in reader:
        name, dept, sal = row 
        if dept == "Data" and int(sal)>70000:
            writer.writerow(row)
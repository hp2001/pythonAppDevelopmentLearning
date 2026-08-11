import csv
ans = []

with open("employees.csv","r") as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        name, dept, sal = row
        if dept == 'Data' and int(sal)>70000:
            ans.append(row)

with open("output.csv","w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["name", "department","salary"])
    for i in ans:
        # writer.writerow(f"{i[0]} - {i[1]} - {i[2]}")
        writer.writerow(i)
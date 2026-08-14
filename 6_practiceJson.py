import json
filtered = []
with open("data/employee.json","r") as input, open("data/employee_output.json", "w") as output:
    d = json.load(input)
    for data in d:
        if data['department'] == "Data" and data['salary'] > 70000:
            filtered.append(data)
    json.dump(filtered, output, indent=4)
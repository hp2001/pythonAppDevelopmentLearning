with open("data/employees.txt", 'r') as file:
    ans = []
    for line in file:
        name, dept, sal = line.strip().split(',')
        if dept == 'Data' and int(sal) > 70000:
            ans.append(line.strip())
    print(ans)
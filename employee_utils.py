'''def get_data_employees(employees):
    result = []

    for employee in employees:
        if employee["department"] == "Data":
            result.append(employee)

    return result
'''
from socket import if_nameindex


def get_data_employees(employees):
    result = []

    for employee in employees:
        if employee["department"] == "Data":
            result.append(employee)

    return result

if __name__ == "__main__":
    print("employee_utils.py executed")
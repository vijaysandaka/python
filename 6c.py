def write_employee_report(filename):
    employees = [
        {"name": "Alice", "department": "HR"},
        {"name": "Bob", "department": "Engineering"},
        {"name": "Charlie", "department": "Finance"}
    ]
   
    with open(filename, "w") as file:
        for employee in employees:
            line = f"Name: {employee['name']}, Department: {employee['department']}\n"
            file.write(line)

# Call the function to create the report
write_employee_report("employee_report.txt")

# Read and display the report
with open("employee_report.txt", "r") as file:
    print(file.read())
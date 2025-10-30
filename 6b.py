def count_error_lines(filename):
    error_count = 0
    try:
        with open(filename, "r") as file:
            for line in file:
                if "ERROR" in line.upper():
                    error_count += 1
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
        return 0
    return error_count

error_lines = count_error_lines("log.txt")
print(f"Number of lines with 'ERROR': {error_lines}")
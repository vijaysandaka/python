grades = [85, 90, 78, 92, 88]

print("Grades List:", grades)

try:
    index = int(input("Enter the index of the grade you want to view: "))
    print(f"The grade at index {index} is: {grades[index]}")
except IndexError:
    print("Invalid index. Please enter a valid index.")
except ValueError:
    print("Invalid input. Please enter a numerical index.")
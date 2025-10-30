def analyze_student_grades():
    student_names = ["Alice", "Bob", "Charlie", "Diana"]
    student_grades = [85, 92, 78, 90]
 
    print("Welcome to the Student Grades Analyzer!\n")
   
    num_students = len(student_names)
    print("Number of students:", num_students)
   
    print("\nType of student_names list:", type(student_names))
    print("Type of student_grades list:", type(student_grades))
   
    highest_grade = max(student_grades)
    lowest_grade = min(student_grades)
    print("\nHighest grade:", highest_grade)
    print("Lowest grade:", lowest_grade)
   
    sorted_grades = sorted(student_grades)
    print("\nSorted grades:", sorted_grades)
 
    reversed_grades = list(reversed(sorted_grades))
    print("Reversed grades:", reversed_grades)
   
    grade_indices = list(range(1, num_students + 1))
    print("\nGrade indices from 1 to number of students:", grade_indices)
 
analyze_student_grades()
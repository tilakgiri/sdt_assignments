from calculate import calculate_average
from student_data import get_student_data

students = get_student_data()
average = calculate_average(students)

print(f"Class average: {average:.1f}")
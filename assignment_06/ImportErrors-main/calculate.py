import numpy as np
# Missing fix: import numpy as np, average is actually np.mean

def calculate_average(students):
  grades = [student["grade"] for student in students]
  return np.mean(grades)
def calculate_grade(mark1, weight1, mark2, weight2, mark3, weight3):

  weighted_mark1 = mark1 * weight1
  weighted_mark2 = mark2 * weight2
  weighted_mark3 = mark3 * weight3
  
  overall_grade = weighted_mark1 + weighted_mark2 + weighted_mark3
  
  return overall_grade

mark1 = float(input("Enter mark 1: "))
weight1 = float(input("Enter weight for mark 1 (as a decimal): "))
mark2 = float(input("Enter mark 2: "))
weight2 = float(input("Enter weight for mark 2 (as a decimal): "))
mark3 = float(input("Enter mark 3: "))
weight3 = float(input("Enter weight for mark 3 (as a decimal): "))

grade = calculate_grade(mark1, weight1, mark2, weight2, mark3, weight3)
print(f"Overall grade: {grade:.4f}")


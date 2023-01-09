def calculate_grade(mark1, weight1, mark2, weight2, mark3, weight3):
  weighted_mark1 = mark1 * weight1
  weighted_mark2 = mark2 * weight2
  weighted_mark3 = mark3 * weight3

  overall_grade = weighted_mark1 + weighted_mark2 + weighted_mark3
  
  return overall_grade

def get_float(prompt_message = "Enter a float: "):
  while True:
    try:
      user_input = input(prompt_message)
      val = float(user_input)
      return val
    except ValueError:
      print("Bad input. Please try again.")


mark1 = get_float("Enter mark 1: ")
weight1 = get_float("Enter weight for mark 1 (as a decimal): ")
mark2 = get_float("Enter mark 2: ")
weight2 = get_float("Enter weight for mark 2 (as a decimal): ")
mark3 = get_float("Enter mark 3: ")
weight3 = get_float("Enter weight for mark 3 (as a decimal): ")

grade = calculate_grade(mark1, weight1, mark2, weight2, mark3, weight3)
print(f"Overall grade: {grade:.2f}")

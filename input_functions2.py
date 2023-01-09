def get_int(string = "Enter a integer between 1 and 10 "):
       while True:
        try:
          user_input = input(string)
          val = int(user_input)
          return val
        except ValueError:
          print("Bad input. Please try again.")
          
def get_float(string = "Enter a number between 1 and 10 "):
  while True:
    try:
      user_input = input(string)
      val = float(user_input)
      return val
    except ValueError:
      print("Bad input. Please try again.")
          
          
int_val = get_int()
float_val = get_float()        

      

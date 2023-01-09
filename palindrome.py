
string = input("Enter some text: ")

string = ''.join(c for c in string if c.isalpha())

string = string.lower()

if string == string[::-1]:
  print("The text is a palindrome.")
else:
  print("The text is not a palindrome.")

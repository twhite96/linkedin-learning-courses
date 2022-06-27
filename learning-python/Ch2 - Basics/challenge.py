def is_palindrome(string):
  if string == string[::-1]:
    return True
  return False

start = True
while(start):
  palindrome = input("Enter a string to test for palindrome or 'exit' > ")
  print("Palindrome test: ", palindrome)
def is_palindrome(s):
    return s == s[::-1]

user_input = input("Enter a string: ")

if is_palindrome(user_input):
    print("The entered string is a palindrome.")
else:
    print("The entered string is not a palindrome.")
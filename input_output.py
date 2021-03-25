def reverse_text(text: str):
    return text[::-1]


def is_palindrome(text: str):
    return text == reverse_text(text)


input_something = input("Print some text here!")

if is_palindrome(input_something):
    print("Yes, its palindrome!")
else:
    print("No, its not palindrome!")

def check_palindrome(text):
    return text == text[::-1]


if __name__ == "__main__":
    text = "madam"   # no input()
    if check_palindrome(text):
        print("The string is a Palindrome")
    else:
        print("The string is not a Palindrome")

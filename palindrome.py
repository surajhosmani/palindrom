def check_palindrome(text):
    if text == text[::-1]:
        return "Palindrome"
    else:
        return "Not Palindrome"

if __name__ == "__main__":
    text = input("Enter a string: ")
    print(
        "The string is a Palindrome"
        if check_palindrome(text) == "Palindrome"
        else "The string is not a Palindrome"
    )
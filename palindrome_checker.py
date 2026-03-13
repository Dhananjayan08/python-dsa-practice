def palindrome(s):
    s = s.lower()
    if s==s[::-1]:
        return "Palindrome"
    else:
        return "Not Palindrome"

s = input("Enter a String: ")
print(palindrome(s))

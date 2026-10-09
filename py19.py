# Accept the name and check if its palindrome
name = input("Enter name:")
if name == name[::-1]:
    print("Palindrom")
else:
    print("Not Palindrom")
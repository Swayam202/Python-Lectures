# Python examples for common sting function

#simple string
text = "  Welcom to IMCC!  "

# 1.  String spaces from both ends
print("Remove space", text.strip())

# 2. Lowercase

# 3. Uppercase

# 4.  Capitalixe first  letter
text = text.strip()
print("Capitalize First letter : ", text.capitalize())

# 5. Title case (capitalize each world)
print(text.title())

# 6. Count occcurences of a substring
print ("Letter C occure ", text.count('C'))

# 7. Find the  position of a substing (-1 if not founf)
print("Position of IMCC in text is ", text.find("IMCC"))

# 8. Replace a substring
print(text.replace("IMCC", "Python Magic"))

# 9. Check if string start or ends with certain substring
print(text.startswith("    We"))
print(text.endswith("!   "))

# 10. Split string into list by a delimiter
print("Simple split", text.split())

# 11. 

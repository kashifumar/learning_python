# This Python program demonstrates string concatenation, which means joining text (strings)
# together.

# command to execute the script
# python3 code/01_basics/strings102.py

# 1️⃣ Defining Two Strings
firstName = "Muhammad"
lastName = "Musa"

# firstName is assigned the text "Muhammad".
# lastName is assigned the text "Musa".
# Both are strings because they are enclosed in "" (double quotes).

# 2️⃣ Joining Strings Using + (Concatenation)
print(firstName + " " + lastName)

# The + operator joins (concatenates) strings together.
# " " (a space) is added between firstName and lastName to ensure there is a space 
# between the names.

# 📌 Output:
# Muhammad Musa

# 👉 Without the " ", the output would be "MuhammadMusa", which is incorrect.

# 3️⃣ Printing with , (Comma)
print(firstName, lastName)

# The , (comma) automatically adds a space between the values.
# It does not require manual spacing like " " in concatenation.

# 📌 Output:
# Muhammad Musa

# Same result as before, but the , makes it easier to write.

# Key Takeaways

# ✅ String Concatenation (+) manually joins text.
# ✅ Adding " " (a space string) is needed to separate words.
# ✅ Using , (comma) automatically adds a space when printing multiple values.
# ✅ Both methods work, but , is simpler for printing.

# Alternative Example: Adding a Greeting
greeting = "Hello, " + firstName + " " + lastName + "!"
print(greeting)

# 📌 Output:
# Hello, Muhammad Musa!

# This shows how concatenation can be used in real-world applications like greeting users.
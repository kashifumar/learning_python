# This Python program introduces strings and numbers, showing how data types work in Python.

# command to execute the script
# python3 code/01_basics/strings101.py

# 1️⃣ Defining a String (Text Data)

name = "Musa"
year = "2017"

# name stores the text "Musa" (a person's name).
# year stores the text "2017" (even though it looks like a number, 
# it's inside quotes, so it's treated as text, not a number).

# 2️⃣ Checking the Data Type of year
print(type(year))

# The type() function checks what kind of data year is storing.
# Since "2017" is inside quotes, Python recognizes it as a string (str), which means it's text.

# 📌 Output:
# <class 'str'>
# This means year is a string (text) in Python.

# 3️⃣ Changing the Type of Quotes

year = '2017'
print(type(year))

# Here, year is still assigned "2017", but using single quotes instead of double quotes.
# Python treats single (') and double (") quotes the same for strings.
# The output will still be:
# <class 'str'>

# 4️⃣ Trying to Add 1 to a String
# print(year + 1)

# 🚨 Error Alert! 🚨
# Since year is a string ("2017"), Python does not allow mathematical operations on it.

# 📌 Python will show an error:
# TypeError: can only concatenate str (not "int") to str
# 👉 This means you cannot add a number to text directly.

# Fixed Version to Avoid the Error
# To fix the error, you can convert year to an integer before adding:
year = "2017"
year = int(year)  # Convert string to an integer
print(year + 1)   # Now it works!

# 📌 Output:
# 2018

# 5️⃣ Changing year to a Number
year = 2017
print(type(year))

# Now, year is assigned 2017 without quotes.
# Since it has no quotes, Python treats it as a number (int, meaning integer).
# The output will be:
# <class 'int'>

# Now, year is a number and can be used in math calculations.

# 6️⃣ Adding 1 to a Number
print(year + 1)

# Now that year is a number, Python can perform addition.
# 2017 + 1 results in 2018.

# 📌 Output:
# 2018

# Key Takeaways
# 1️⃣ Strings (str) are text and always inside quotes (" " or ' ').
# 2️⃣ Numbers (int) do not need quotes and can be used for math.
# 3️⃣ type() tells us what kind of data we are dealing with.
# 4️⃣ You cannot mix strings and numbers in math.
# 5️⃣ To convert a string to a number, you need int(year) (not done in this code, but important to know).
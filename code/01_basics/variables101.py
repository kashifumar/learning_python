#This Python program introduces variables and data types, showing how Python handles 
# different types of values.

# command to execute the script
# python3 code/01_basics/variables101.py

# 1️⃣ Creating Variables and Checking Their Types
bookPrice = 3
amount = 2.5
print(type(bookPrice))

# bookPrice is assigned 3, which is a whole number (integer).
# amount is assigned 2.5, which is a decimal number (float).
# The type(bookPrice) function tells us what type of data is stored in bookPrice.

# 📌 Output:
# <class 'int'>

# ✅ This means bookPrice is of type integer (int).

# 2️⃣ Changing the Data Type of bookPrice
bookPrice = "Hello"
print(type(bookPrice))
print(bookPrice)

# Now, bookPrice is reassigned "Hello", which is a string (text).
# The type() function confirms that the type of bookPrice has changed.

# 📌 Output:
# <class 'str'>
# Hello

# ✅ Python allows variables to change types (from int to str).
# ✅ When we print bookPrice, it now displays "Hello" instead of a number.


# 3️⃣ Understanding Variable Names and Case Sensitivity
year = 2017
Year = "2017"

print("Type of year is ", type(year))
print("Type of Year is ", type(Year))

# year is assigned 2017 (a number, integer).
# Year is assigned "2017" (text, string).
# Python is case-sensitive, so year and Year are two different variables.

# 📌 Output:
# Type of year is  <class 'int'>
# Type of Year is  <class 'str'>

# ✅ Even though they look similar, year and Year are separate variables.
# ✅ Python treats uppercase and lowercase variable names differently.

# Key Takeaways

# 1️⃣ Variables store data and can change over time.
# 2️⃣ Python allows changing data types dynamically (e.g., int to str).
# 3️⃣ type() helps check the data type of a variable.
# 4️⃣ Python is case-sensitive, so year and Year are not the same.

# Extra Example: Mixing Types (Common Mistake)

# This will cause an error:
# print(year + Year)

# 🚨 Error:
# TypeError: unsupported operand type(s) for +: 'int' and 'str'

# 👉 You cannot add a number (int) to text (str) without conversion.
# print(year + int(Year))  # Convert "2017" (str) to 2017 (int)

# 📌 Output:
# 4034

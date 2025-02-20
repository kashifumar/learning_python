# Type Conversion And Variable Names in Python
# When working with variables, sometimes we need to convert data types to perform 
# certain operations. This is called type conversion (type casting).

# command to execute the script
# python3 code/01_basics/02_variables.py

# 1️⃣ Converting Strings to Numbers
# If a number is stored as a string ("123"), we cannot perform calculations with it 
# unless we convert it.

# ✅ Example (Correct Conversion)
year = "2017"  # This is a string
new_year = int(year)  # Convert string to integer

print(new_year + 1)  # Now we can do math

# 📌 Output:
# 2018

# ✅ int(year) converts "2017" (string) to 2017 (integer), so we can add 1.

# ❌ Example (Without Conversion - Error)
# print(year + 1)  # Trying to add a number to a string

# 🚨 Error:
# TypeError: can only concatenate str (not "int") to str
# 👉 This happens because "2017" is still a string.

# 2️⃣ Converting Numbers to Strings
# Sometimes we need to convert numbers into text, such as when printing messages.

# ✅ Example (Correct Conversion)
year = 2017
print("The year is " + str(year))  # Convert number to string before concatenation

# 📌 Output:
# The year is 2017

# ✅ str(year) converts 2017 (integer) to "2017" (string), so it can be joined with other text.


# 3️⃣ Converting Between Float and Integer
# Float → Integer: Removes decimal part (does not round).
# Integer → Float: Adds .0 to the number.

# Example
amount = 2.9
print(int(amount))  # Convert float to integer (removes decimal part)

price = 5
print(float(price))  # Convert integer to float

# 📌 Output:
# 2
# 5.0

# ✅ int(2.9) removes .9, keeping only 2.
# ✅ float(5) becomes 5.0, making it a decimal.


# 4️⃣ Good Variable Naming Practices
# Using clear and meaningful variable names makes code easy to understand.

# ❌ Bad Naming (Confusing)
a = "John"
b = 25
c = 3.5
# 👉 No one knows what a, b, or c represent.

# ✅ Good Naming (Descriptive)
customer_name = "John"
customer_age = 25
discount_rate = 3.5
# 👉 Easy to understand what each variable stores.

# Final Thoughts & Best Practices

# ✅ Always convert types when mixing numbers and text.
# ✅ Use int(), float(), and str() to avoid errors.
# ✅ Choose clear variable names (avoid x, y, a, etc.).
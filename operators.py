# # Artimetic Operators
# # + - * /
#
# # Comprison Operators
# # >
# # <
# # ==
#
# value1 = 6
# value2 = 7
#
# print(value2 > value1) # Boolean
# print(value1 > value2)
# print(value1 + value2) # Adding the values
# print(value1 - value2)
# print(value1 >= value2)
# print(value1 != value2) # not equal
#
# # Built in methods available in python hat gives us boolean outcome as well
#
# name = "Tuan"
# # isalpha() #
# print(name.isalpha()) # Returns the boolean outcome
# print(name.isdigit()) # Checks the values if in digits
# print(name.startswith()) # Checks if the input starts with a capital letter
#
# # When using integers then casting is needed to convert it into a string
# age = 12
# print(str(age.isalpha()))

# Strings, Concatenation and Casting

# single_quotes = 'Hello World'
# greetings = "Hello World!"
# H E L L O   W O R L D     !
# 0 1 2 3 4 5 6 7 8 9 10 11 12
# To find out the length of the string, we use the method len()
# print(len(greetings))
#
# # String slicing
# print(greetings[5:])
# # print out "World!"

# white_spaces = "lots of spaces at the end                 "
# print(len(white_spaces)) # Shows the number of spaces including the white spaces
# print(len(white_spaces.strip())) # Takes away the white spaces and shows the length of string
# print(white_spaces.strip()) # Prints out the string

# example_text = "Here is some text with a lot of texts"
# print(example_text.count("text")) # Counts how many times a selected word appears in the string
#
# print(example_text.lower()) # Converts the string to lowercase
# print(example_text.upper()) # Converts the string to uppercase
# print(example_text.capitalize())
# print(example_text.replace("with", ","))

# Concatenation? Combining values, variables and strings together

first_name = 'Tuan'
last_name = 'Pham'
age = 25

print(first_name + " " + last_name + " " + str(age)) # String and integer concatenation
print(f"{first_name} {last_name} is {age} years old")

# print(type(str(age)))
# Casting - casting string into int or int into string

# Find the method to cast string into an integer and display the value and the type after conversion
print(int(age))
print(type(int(age)))


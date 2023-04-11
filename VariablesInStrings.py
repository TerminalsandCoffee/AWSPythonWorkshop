"""
In this method you can use the {} in your string to indicate where the variable should go. 
Then use .format(variable_name) after the quotation marks. 
If you have multiple variables, for each variable you use a {}. 
In the .format() separate each variable with a comma. 
For example .format(variable_1, variable_2)
"""

first_name = "John"
surname = "Doe"
print("My first name is {}. My family name is {}".format(first_name, surname))


"""
format called f-strings to include variables in your strings

"""
firstname = "Jane"
surname = "Doe"

print(f"My first name is {firstname}. My family name is {surname}")

my_int = 50
sentence = "The total comes to: "

#print(sentence + my_int) < this is wrong


print(sentence + str(my_int))

#str() returns a string object
#int() returns an integer object
#float() returns a floating point object
#bool() a boolean value of True or False








"""
        dictionaries
To read the value associated with a key, 
you need to provide the name of the dictionary and the the value of the key inside square brackets.
"""
user = {"first_name":"Ada"}
print(user["first_name"])
#output: Ada

"""
to update
Dictionaries are mutable, which means they can be changed after you create them. 
You can add, update or delete the key-value pairs in a dictionary.
"""

user["family_name"] = "Byron"
print(user)
#output {'first_name': 'Ada', 'family_name': 'Byron'}


#modify
user["family_name"] = "Lovelace"
print(user)
# {'first_name': 'Ada', 'family_name': 'Lovelace'}


#delete
del user["family_name"]
print(user)
#output {'first_name': 'Ada'}



"""
To determine a type
"""

my_variable = "A string"
print(type(my_variable))
#output <class 'str'>


















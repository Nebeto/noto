# Instanciating

my_variable = {
  "attribute_1": "value_1",
  "attribute_2": True,
  "attribute_3": 1,
}

# Getting a value for an attribute

print(my_variable["attribute_1"])

# Setting a new value on existing attribute

my_variable["attribute_1"] = "Hello World!"

print(my_variable["attribute_1"])

# Setting a new value on a new attribute

my_variable["attribute_4"] = {
  "a_1": True,
  "a_2": False
}

print(my_variable)

# Remove an attribute

del my_variable["attribute_4"]

print(my_variable)

my_variable = { key: value for key, value in my_variable.items() if key != "attribute_3" }

print(my_variable)

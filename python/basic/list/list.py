def smart_print(header, result):
    points = "." * (40 - len(header))
    print(f"{header} {points} {result}")

# Instanciating

my_variable = [
  "value_1",
  "value_2",
  "value_3",
]

# Getting a value by index

smart_print("[get][value][idx:0]", my_variable[0])

# Setting a new value on existing index

my_variable[0] = "value_4"
smart_print("[set][value:value_4][idx:0]", my_variable)

# Setting a new value on a new index

my_variable.append("Hello World!")
smart_print("[set][value:Hello World!][idx:end]", my_variable)

# Removing a value

my_variable.remove("Hello World!")
smart_print("[remove][value:Hello World!]", my_variable)

# Sublisting

smart_print("[sublist][start:idx:1]", my_variable[1:])

# Sorting

smart_print("[sort]", sorted(my_variable))
smart_print("[sort][reverse]", sorted(my_variable, reverse=True))

# Filtering

smart_print("[filter][value:*3*]", list(filter(lambda value: '3' in value, my_variable)))

# [..](../../..) / [Python](../..) / [Basic](..) / Dictionary

aka. Object, JSON structure

https://github.com/Nebeto/noto/labels/lang https://github.com/Nebeto/noto/labels/lang%3Apython

## Instanciating

```python
my_variable = {
  "attribute_1": "value_1",
  "attribute_2": True,
  "attribute_3": 1,
}
```

## Getting a value for an attribute

```python
print(my_variable["attribute_1"])
# will print "value_1"
```

## Setting a new value

### On existing attribute

```python
my_variable["attribute_1"] = "Hello World!"

print(my_variable["attribute_1"])
# will print "Hello World!"
```

### On a new attribute

```python
my_variable["attribute_4"] = {
  "a_1": True,
  "a_2": False
}

print(my_variable)
# will print {'attribute_1': 'Hello World!', 'attribute_2': True, 'attribute_3': 1, 'attribute_4': {'a_1': True, 'a_2': False}}
```

## Remove an attribute

```python
del my_variable["attribute_4"]

print(my_variable)
# will print {'attribute_1': 'Hello World!', 'attribute_2': True, 'attribute_3': 1}
```

```python
my_variable = { key: value for key, value in my_variable.items() if key != "attribute_3" }

print(my_variable)
# will print {'attribute_1': 'Hello World!', 'attribute_2': True}
```

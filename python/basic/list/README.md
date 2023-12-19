# [..](../../..) / [Python](../..) / [Basic](..) / List

https://github.com/Nebeto/noto/labels/lang https://github.com/Nebeto/noto/labels/lang%3Apython

## Instanciating

```python
my_variable = [
  "value_1",
  "value_2",
  "value_3",
]
```

## Getting a value for an index

```python
print(
    my_variable[0]
) # will print "value_1"
```

## Setting a new value

### On existing index

```python
my_variable[0] = "value_4"

print(
    my_variable[0]
) # will print "value_4"
```

### On a new index

```python
my_variable.append("Hello World!")

print(
    my_variable
) # will print ['value_4', 'value_2', 'value_3', 'Hello World!']
```

## Removing a value

```python
my_variable.remove("Hello World!")

print(
    my_variable
) # will print ['value_4', 'value_2', 'value_3']
```

## Sublisting

```python
print(
    my_variable[1:]
) # will print ['value_2', 'value_3']
```

## Sorting

```python
print(
    sorted(my_variable)
) # will print ['value_2', 'value_3', 'value_4']
```

```python
print(
    sorted(my_variable, reverse=True)
) # will print ['value_4', 'value_3', 'value_2']
```

## Filtering

```python
print(
    list(filter(lambda value: '3' in value, my_variable))
) # will print ['value_3']
```

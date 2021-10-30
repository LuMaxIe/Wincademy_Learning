# Python Basics

## Variables

### Assigning a variable
Assign can be done by using a name plus an equals sign. The type of input will be the type assigned to the variable.

```Python
my_integer = 10
my_float = 0.10
my_string = "Max"
my_bool = True
```

### Casting
Casting is using a constructor to specify a certain type to a variable. This is needed because Python is strongly typed. A string cannot be concatenated with an integer for example. The integer has to be Cast to a string beforehand:

```Python
my_string = 'a string concatenated with.. '
my_integer = 9
my_concat = my_string + str(my_integer)
```

### Strings

* Raw Strings are made by adding a preceding 'R' or 'r': print(r'foo\nbar') >>> prints foo\nbar
* Triple quoted strings allows both quotation marks and newlines

## Comments

There are three types of comments that I'd use:
1. Single line using a single "#"
2. Multiline using """ + """

The multiline comments can be use to generate documentation
```Python
def add(value1, value2):
    """Calculate the sum of value1 and value2."""
    return value1 + value2
```
In the Python interactive help system, the docstring is then made available via the __doc__ attribute.
```Python
>>> print add.__doc__
Calculate the sum of value1 and value2.
```
There is a number of tools that auto-generate documentation from docstrings, such as Doxygen, PyDoc, pdoc, and the autodoc extension for Sphinx.


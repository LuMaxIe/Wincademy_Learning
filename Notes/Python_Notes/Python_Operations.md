# Usefull operations

## Strings

### Indexing and slicing strings

```Python
my_string = "Hi my name is Max!"
first_letter = my_string[0] #H
get_greeting = my_string[0:2] #[:2] also works because of start == beginning, 0 can be omitted
get_name = my_string[-4:-1] #Max
get_steps = my_string[2:8:2] # [start:stop:step]
```

### Adding a variable into a string

You can add a variable in a string by using a preceding 'f' before the string and curly bracers inside of the string

```Python
answer = 50
add_in_string = f'The answer is ... {answer}'
```

## Integers && Floats

### Comparing floats
Comparing a float to another float for "equalness" will not always work out. This is because the internal representations of floats might (and most likely) not be equal:
```Python
x = 1.1 + 2.2
x == 3.3 
# False
```
To determine whether a float is equal to another float is to substract one float from another. The remainder can be compared against a "Tolerance" using the absolute value function "abs()"
```Python
tolerance = 0.00001
x = 1.1 + 2.2
abs(x - 3.3) < tolerance
# True
``` 



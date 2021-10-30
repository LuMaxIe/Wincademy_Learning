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
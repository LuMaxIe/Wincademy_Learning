# Python Functions

## Defining a function

```Python
def function_name(var1, var2):
  return var1 + var2
```

## File structure

A common file structure is defining the main functionality at the top and other funtions below. Important is to have the if statement at the very bottom of the file.

```Python
# (1) Python takes note of this function
def main():
    # (5) At this point greet() is known and we can run it.
    print(greet('Bob'))

# (2) Then this one
def greet(name):
    return f'Hi, {name}!'

# (3) Now this statement is read
if __name__ == '__main__':
    # (4) main is run
    main()
```
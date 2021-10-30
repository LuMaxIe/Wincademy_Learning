# Do not modify these lines
__winc_id__ = '63ce21059cf34d3d8ffef497ede7e317'
__human_name__ = 'comments'

# Add your code after this line

# This code will transform your value to percentages.
# This code will also be my first Python function!
def get_percentage_string(float_value): #define a function here
  return "{:.0%}".format(float_value) # return the input multiplied by 100 and formatted as percentage string

"""Get an example of how the function works by adjusting the value to transform. 
Run the code and see the value printed to the console!"""
value_to_transform = 0.5
print(get_percentage_string(value_to_transform))
"""Don't know what to write anymore, but hey,
here's another comment"""

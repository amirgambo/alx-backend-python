0x00. Python - Variable Annotations

Learning Objectives
General
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

Type annotations in Python 3
How you can use type annotations to specify function signatures and variable types
Duck typing
How to validate your code with mypy
Requirements
General
Allowed editors: vi, vim, emacs
All your files will be interpreted/compiled on Ubuntu 18.04 LTS using python3 (version 3.7)
All your files should end with a new line
The first line of all your files should be exactly #!/usr/bin/env python3
A README.md file, at the root of the folder of the project, is mandatory
Your code should use the pycodestyle style (version 2.5.)
All your files must be executable
The length of your files will be tested using wc
All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
All your classes should have a documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')
All your functions (inside and outside a class) should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')
A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)

0. Write a type-annotated function add that takes a float a and a float b as arguments and returns their sum as a float.

1. Write a type-annotated function concat that takes a string str1 and a string str2 as arguments and returns a concatenated string.

2. Write a type-annotated function floor which takes a float n as argument and returns the floor of the float.

3. Write a type-annotated function to_str that takes a float n as argument and returns the string representation of the float.

4. Define and annotate the following variables with the specified values:

a, an integer with a value of 1
pi, a float with a value of 3.14
i_understand_annotations, a boolean with a value of True
school, a string with a value of “Holberton”

5. Write a type-annotated function sum_list which takes a list input_list of floats as argument and returns their sum as a float.

6. Write a type-annotated function sum_mixed_list which takes a list mxd_lst of integers and floats and returns their sum as a float.

7. Write a type-annotated function to_kv that takes a string k and an int OR float v as arguments and returns a tuple. The first element of the tuple is the string k. The second element is the square of the int/float v and should be annotated as a float.

8. Write a type-annotated function make_multiplier that takes a float multiplier as argument and returns a function that multiplies a float by multiplier.

9. Annotate the below function’s parameters and return values with the appropriate types

10. Augment the following code with the correct duck-typed annotations:

# The types of the elements of the input are not know
def safe_first_element(lst):
    if lst:
        return lst[0]
    else:
        return None

11. Given the parameters and the return values, add type annotations to the function

Hint: look into TypeVar

def safely_get_value(dct, key, default = None):
    if key in dct:
        return dct[key]
    else:
        return default

12. Use mypy to validate the following piece of code and apply any necessary changes.

def zoom_array(lst: Tuple, factor: int = 2) -> Tuple:
    zoomed_in: Tuple = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = [12, 72, 91]

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3.0)

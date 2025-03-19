'''Variables:

Variables are containers for storing data values.

Creating Variables:

Python has no command for declaring a variable.
A variable is created the moment you first assign a value to it.
Variables do not need to be declared with any particular type, and can even change type after they have been set.
A variable can have a short name (like x and y) or a more descriptive name (age, carname, total_volume).

Rules for Python variables:

A variable name must start with a letter or the underscore character
A variable name cannot start with a number
A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
Variable names are case-sensitive (age, Age and AGE are three different variables)
A variable name cannot be any of the Python keywords.

In creating variables there are 3 types of cases,they are
>>camel case
>>snake case
>>pascal case

CAMEL CASE:
    Each word, except the first, starts with a capital letter
    eg:myVariableName = "python"
    
SNAKE CASE:
    Each word is separated by an underscore character:
    eg:my_variable_name = "python"
    
PASCAL CASE:
    Each word starts with a capital letter:
    eg:MyVariableName = "python"
    
    
Many Values to Multiple Variables:

Python allows you to assign values to multiple variables in one line:

Example:
    x, y, z = "Orange", "Banana", "Cherry"
    print(x)
    print(y)
    print(z)

One Value to Multiple Variables:
And you can assign the same value to multiple variables in one line:

Example:
    x = y = z = "Orange"
    print(x)
    print(y)
    print(z)
'''
# Language

A source-to-source Python to JS* compiler. 

Takes in code in the format and syntax of a basic python-esque program, and converts it into the syntax of a JavaScript program. 

Does not support libraries or built-in functions such as range(), will simply treat it as a user-defined function.

## How it works

The input string is broken into tokens or atoms, which are able to identify each element of the code. 

Since python uses tabs instead of braces, a separate handltetabs method is used to convert indentations into braces, which make it easier to convert it to a JavaScript format.

Expressions are parsed and Abstract Syntax Trees are formed, which are then fed to the code generator which converts them into JavaScript-syntax code.

## How to use -

```python3 -i py2js/main.py```

will run the few test codes hardcoded into the program, and print the JavaScript-esque output. 



# BASICS Terminologies and Concepts:

## 1. What is python?
- Python is a high-level, interpreted, interactive and object-oriented scripting language. Python is designed to be highly readable. It uses English keywords frequently where as other languages use punctuation, and it has fewer syntactical constructions than other languages.
## 2. What is Function?
- A function is a block of organized, reusable code that is used to perform a single, related action. Functions provide better modularity for your application and a high degree of code reusing.
- It provide us the side effect of code reusability.
- eg: print(), input(), len(), etc. 
- Here , print() is a function which is used to print the output on the screen it takes the input as a string and prints it on the screen.
## 3. What is Command Line Interface?
- A command-line interface (CLI) processes commands to a computer program in the form of lines of text. The program which handles the interface is called a command-line interpreter or command-line processor. Operating systems implement a command-line interface in a shell for interactive access to operating system functions or services.
- We use python3 <file_name.py> to run the python file in command line interface.
- Here Python3 is the command-line interpreter and <file_name.py> is the file which we want to run.
## 4. What are arguments and parameters?
- An argument is a value that is passed to a function when it is called. When a function is defined, it may have one or more named variables which receive the values of the arguments passed to the function.
- A parameter is a variable in a method definition. When a method is called, the arguments are the data you pass into the method's parameters. Parameter is variable in the declaration of function. Argument is the actual value of this variable that gets passed to function.
- eg: def add(a, b):, add(10, 20), here a and b are parameters and 10 and 20 are arguments.
## 5. What is bug?
- A software bug is an error, flaw or fault in a computer program or system that causes it to produce an incorrect or unexpected result, or to behave in unintended ways.
## 6. What is debugging?
- Debugging is the process of finding and resolving defects or problems within a computer program that prevent correct operation of computer software or a system.
## 7. What is IDE?
- An integrated development environment (IDE) is a software application that provides comprehensive facilities to computer programmers for software development. An IDE normally consists of at least a source code editor, build automation tools and a debugger.
- eg: PyCharm, Jupyter Notebook, etc.
## 8. What is Syntax?
- Syntax is the set of rules that defines the combinations of symbols that are considered to be correctly structured programs in that language.
## 9. What is Variable?
- A variable is a storage location and an associated symbolic name which contains some known or unknown quantity of information referred to as a value.
- eg: a = 10, b = "Hello", etc.
## 10. What are errors?
- An error is a mistake in the program that causes it to behave unexpectedly.
- eg: Syntax Error, Logical Error, etc.
- Syntax Error: It occurs when the syntax of the code is not correct.
- Logical Error: It occurs when the logic of the code is not correct.
- Runtime Error: It occurs when the code is not able to run properly.
- Semantic Error: It occurs when the code is not able to understand the meaning of the code.
## 11. What is Comment?
- A comment is a programmer-readable explanation or annotation in the source code of a computer program. They are added with the purpose of making the source code easier for humans to understand, and are generally ignored by compilers and interpreters.
- eg: # This is a comment, '''This is a comment''', etc.
## 12. What is return value?
- A return value is a value that a function returns to the calling script or function when it completes its task.
## 13. What i newline?
- A newline is a special character or sequence of characters signifying the end of a line of text and the start of a new line.
- eg: \n
- print() function automatically adds a newline character at the end of the string.
## 14. What is indentation?
- Indentation is the space between the margin and the beginning of a line of text.
- It is used to define the block of code in python.
- It is used to define the scope of the code.
## 15. What is a block of code?
- A block of code is a set of statements that are grouped together. A block of code begins with a colon (:) and is indented.
- It is also known as suite.
## 16. What is pseudocode?
- Pseudocode is an informal high-level description of the operating principle of a computer program or other algorithm. It uses the structural conventions of a normal programming language, but is intended for human reading rather than machine reading.
## What is python documentation?
- Python documentation is a set of documents that describes the modules, functions, classes and methods of the Python Standard Library. It also describes the standard types that are built into the interpreter.
- Link: https://docs.python.org/3/ (Official Python Documentation)
- Link for built-in functions: https://docs.python.org/3/library/functions.html
### Note: In python we can use both single and double quotes to define the string.
- eg: "Hello", 'Hello', '''Hello''', """Hello"""
- Here, all the four are valid strings in python.
- We can use single quotes inside the double quotes and double quotes inside the single quotes.
- eg: "Hello 'World'", 'Hello "World"'
- Here, both are valid strings in python.
## What are positional and named/keyword - arguments/parameters?
- Positional arguments are the arguments that can be called by their position in the function definition.
- Named arguments are the arguments that can be called by their name in the function definition.
- eg: def add(a, b):, add(10, 20), add(a=10, b=20)
- Here, a and b are positional arguments and a=10 and b=20 are named arguments.
- In python, we can use both positional and named arguments in the function definition.
- Named arguments also called as keyword arguments.
## What are escape sequences?
- Escape sequences are the sequences of characters that represent a special character when used inside a string.
- eg: \n, \t, \', \", etc.
- Here, \n represents the newline character, \t represents the tab character, \' represents the single quote character, \" represents the double quote character, etc.
- We can use escape sequences inside the string to represent the special characters.
## What is f-string?
- An f-string is a formatted string which is used to format the string in python.
- It is used to format the string by using the curly braces and f character before the string.
- eg: f"Hello {name}, your age is {age}"
- Here, name and age are the variables and we are using the f-string to format the string.
## What are different types of errors in python?
- Syntax Error: It occurs when the syntax of the code is not correct.
- Logical Error: It occurs when the logic of the code is not correct.
- Runtime Error: It occurs when the code is not able to run properly.
- Semantic Error: It occurs when the code is not able to understand the meaning of the code.
- Indentation Error: It occurs when the indentation of the code is not correct.
- Name Error: It occurs when the variable is not defined.
- Type Error: It occurs when the type of the variable is not correct.
- Value Error: It occurs when the value of the variable is not correct.
- Zero Division Error: It occurs when the denominator is zero.
- File Not Found Error: It occurs when the file is not found.
- etc.
## What are different type of formatting in python?
- % formatting: It is used to format the string by using the % character. **eg : print("Hello %s, your age is %d" % (name, age))**
- str.format() method: It is used to format the string by using the str.format() method. **eg: print("Hello {}, your age is {}".format(name, age))**
- f-string: It is used to format the string by using the f character before the string. **eg: f"Hello {name}, your age is {age}"**
- format() function: It is used to format the string by using the format() function. **eg: print("Hello {0}, your age is {1}".format(name, age))**
- Template strings: It is used to format the string by using the Template strings. **eg: from string import Template, t = Template("Hello $name, your age is $age"), t.substitute(name=name, age=age)**
- etc.

## What are data types in python?
- int: It is used to represent the integer values. **eg: 10, 20, 30, etc.**
- float: It is used to represent the floating point values. **eg: 10.5, 20.5, 30.5, etc.**
- complex: It is used to represent the complex values. **eg: 10+20j, 20+30j, 30+40j, etc.**
- str: It is used to represent the string values. **eg: "Hello", 'Hello', '''Hello''', """Hello""", etc.**
- bool: It is used to represent the boolean values. **eg: True, False**
- list: It is used to represent the list of values. **eg: [10, 20, 30], [10.5, 20.5, 30.5], ["Hello", "World"], etc.**
- tuple: It is used to represent the tuple of values. **eg: (10, 20, 30), (10.5, 20.5, 30.5), ("Hello", "World"), etc.**
- set: It is used to represent the set of values. **eg: {10, 20, 30}, {10.5, 20.5, 30.5}, {"Hello", "World"}, etc.**
- dict: It is used to represent the dictionary of values. **eg: {"name": "John", "age": 20}, {"name": "Smith", "age": 30}, {"name": "David", "age": 40}, etc.**
- None: It is used to represent the null values. **eg: None**
- etc.
### Note : In python, we can use the type() function to get the type of the variable.
### Note : In python, we can use the id() function to get the id of the variable.
### Note : In python, we can use the isinstance() function to check the type of the variable.
### Note : In python, we can use the del keyword to delete the variable.
### Note : In python, we can use the input() function to take the input from the user.
### Note : In python, we can use the print() function to print the output on the screen.
### Note : In python, we can use the len() function to get the length of the variable.

## What are the naming conventions in python?
- We should use the lowercase letters to define the variable name.
- We should use the uppercase letters to define the constant name.
- We should use the camel case to define the class name.
- We should use the snake case to define the function name.
- We should use the snake case to define the module name.
- We should use the snake case to define the package name.
- We should use the snake case to define the file name.
- We should use the snake case to define the variable name.
- We should use the snake case to define the method name.
- We should use the snake case to define the attribute name.
- We should use the snake case to define the property name.
- We should use the snake case to define the argument name.
- We should use the snake case to define the parameter name.
- We should use the snake case to define the local variable name.
- We should use the snake case to define the global variable name.
- We should use the snake case to define the instance variable name.
- We should use the snake case to define the class variable name.
## What are different case styles in python?
- Camel Case: In this style, the first letter of the word is in lowercase and the first letter of the remaining words is in uppercase.  **eg: className**
- Pascal Case: In this style, the first letter of all the words is in uppercase. **eg: ClassName**
- Snake Case: In this style, all the letters of the word are in lowercase and the words are separated by the underscore. **eg: class_name**
- Kebab Case: In this style, all the letters of the word are in lowercase and the words are separated by the hyphen. **eg: class-name**
- etc.
## What are different types of operators in python?
- Arithmetic Operators: It is used to perform the arithmetic operations. **eg: +, -, *, /, %, //, etc.**
- Comparison Operators: It is used to compare the values. **eg: ==, !=, <, >, <=, >=, etc.**
- Assignment Operators: It is used to assign the values to the variables. **eg: =, +=, -=, *=, /=, %=, //=, etc.**
- Logical Operators: It is used to perform the logical operations. **eg: and, or, not, etc.**
- Bitwise Operators: It is used to perform the bitwise operations. **eg: &, |, ^, ~, <<, >>, etc.**
- Membership Operators: It is used to test the membership in a sequence. **eg: in, not in, etc.**
- Identity Operators: It is used to compare the objects. **eg: is, is not, etc.**
- etc.

### Note: Each data type in python have inbuilt methods and functions.

## What are different types of data structures in python?
- List: It is used to store the list of values. **eg: [10, 20, 30], [10.5, 20.5, 30.5], ["Hello", "World"], etc.**
- Tuple: It is used to store the tuple of values. **eg: (10, 20, 30), (10.5, 20.5, 30.5), ("Hello", "World"), etc.**
- Set: It is used to store the set of values. **eg: {10, 20, 30}, {10.5, 20.5, 30.5}, {"Hello", "World"}, etc.**
- Dictionary: It is used to store the dictionary of values. **eg: {"name": "John", "age": 20}, {"name": "Smith", "age": 30}, {"name": "David", "age": 40}, etc.**
- etc.
## What are different types of control structures in python?
- Conditional Statements: It is used to execute the block of code based on the condition. **eg: if, elif, else, etc.**
- Looping Statements: It is used to execute the block of code multiple times. **eg: for, while, etc.**
- Transfer Statements: It is used to transfer the control from one place to another place. **eg: break, continue, pass, etc.**
- etc.

## What are different types of functions in python?
- Built-in Functions: It is the inbuilt functions that are provided by the python. **eg: print(), input(), len(), etc.**
- User-defined Functions: It is the functions that are defined by the user. **eg: def add(a, b):, etc.**
- Lambda Functions: It is the anonymous functions that are defined by the lambda keyword. **eg: lambda a, b: a+b, etc.**
- etc.

## What are unary, binary and ternary operators?
- Unary Operators: It is the operators that require only one operand. **eg: -a, +a, ~a, not a, etc.**
- Binary Operators: It is the operators that require two operands. **eg: a+b, a-b, a*b, a/b, a%b, a//b, a**b, a&b, a|b, a^b, a<<b, a>>b, a==b, a!=b, a<b, a>b, a<=b, a>=b, a and b, a or b, etc.**
- Ternary Operators: It is the operators that require three operands. **eg: a if condition else b, etc.**

## What are different types of methods in python?
- Built-in Methods: It is the inbuilt methods that are provided by the python. **eg: append(), extend(), insert(), remove(), pop(), clear(), index(), count(), sort(), reverse(), copy(), etc.**
- User-defined Methods: It is the methods that are defined by the user. **eg: def add(self, a, b):, etc.**
- Static Methods: It is the methods that are defined by the staticmethod decorator. **eg: @staticmethod, etc.**
- Class Methods: It is the methods that are defined by the classmethod decorator. **eg: @classmethod, etc.**
- etc.

## What are different types of modules in python?
- Built-in Modules: It is the inbuilt modules that are provided by the python. **eg: math, random, datetime, etc.**
- User-defined Modules: It is the modules that are defined by the user. **eg: module.py, etc.**
- Third-party Modules: It is the modules that are provided by the third-party. **eg: numpy, pandas, matplotlib, etc.**
- etc.

## What are different types of packages in python?
- Built-in Packages: It is the inbuilt packages that are provided by the python. **eg: os, sys, etc.**
- User-defined Packages: It is the packages that are defined by the user. **eg: package, etc.**
- Third-party Packages: It is the packages that are provided by the third-party. **eg: numpy, pandas, matplotlib, etc.**
- etc.

## What are different types of exceptions in python?
- Built-in Exceptions: It is the inbuilt exceptions that are provided by the python. **eg: ZeroDivisionError, NameError, TypeError, ValueError, etc.**
- User-defined Exceptions: It is the exceptions that are defined by the user. **eg: class MyError(Exception):, etc.**
- etc.

## What are different types of files in python?
- Text Files: It is the files that are used to store the text data. **eg: .txt, etc.**
- Binary Files: It is the files that are used to store the binary data. **eg: .jpg, .png, .pdf, etc.**
- etc.

### Note : a,b = b,a is used to swap the values of the variables.
### Note : In python, we can use the "pass" keyword to define the empty block of code.
### Note : a,b = input("Enter two numbers: ").split() is used to take the multiple inputs from the user and assign it separately to the variables a and b, similarly we can use multiple variables to take the multiple inputs from the user.

## What is interactive mode and script mode?
- Interactive Mode: It is the mode in which the python interpreter takes the input from the user and executes it immediately. **eg: python3**
- Script Mode: It is the mode in which the python interpreter takes the input from the file and executes it. **eg: python3 <file_name.py>**

## What is interpreter and compiler?
- Interpreter: It is the program that translates the high-level language into the machine language line by line. **eg: python3**
- Compiler: It is the program that translates the high-level language into the machine language at once. **eg: gcc**
- In python, the "python" interpreter is used to translate the high-level language into the machine language line by line.
- In python, the "python" compiler is used to translate the high-level language into the machine language at once.

## What are the best practices for writing clean and readable code?

- Use Meaningful Names: Variable, function, and class names should be descriptive and meaningful. They should reflect what they represent or what they do.  
- Follow a Consistent Naming Convention: Whether it's camelCase, snake_case, or PascalCase, stick to a consistent naming convention throughout your code.  
- Write Short Functions and Methods: Functions and methods should ideally do one thing and be relatively short. This makes them easier to understand and test.  
- Use Comments and Docstrings: Use comments to explain why certain code exists, and use docstrings to describe what functions, methods, and classes do.  
- Avoid Deep Nesting: Too many levels of indentation can make code harder to read. Try to avoid this by returning early or breaking up functions.  
- Handle Errors Gracefully: Use try/except blocks to handle errors and exceptions. This prevents your program from crashing unexpectedly.  
- Use Consistent Indentation and Spacing: Consistent indentation and spacing make your code easier to read. Most programming languages have a recommended style guide (like PEP 8 for Python).  
- Keep Line Length Reasonable: Long lines of code can be hard to read. Try to keep line length under a certain limit (like 80 characters).  
- Organize and Group Related Code: Related code should be grouped together. This could be in the same function, class, or module.  
- Refactor and Simplify: Always look for opportunities to refactor and simplify your code. If you see repeated code, consider whether it can be turned into a function. If a function is complex, see if it can be broken down into simpler functions.

## What is type conversion or type casting?
- Type Conversion/Type casting: It is the process of converting the data from one type to another type. **eg: int(), float(), str(), etc.**

### Note : We can print number comma separated by using the f-string, The synatx is f"{number:,}"

## What is scope of the variable?
- Scope of the variable: It is the region of the code where the variable is accessible. **eg: local, global, nonlocal, etc.**
- Local Scope: It is the scope of the variable that is accessible only within the function. **eg: def add(a, b):, etc.**
- Global Scope: It is the scope of the variable that is accessible throughout the program. **eg: a = 10, etc.**
- Nonlocal Scope: It is the scope of the variable that is accessible within the nested function. **eg: def outer():, def inner():, etc.**
- In python, we can use the global keyword to define the global variable inside the function.

## What is the structure to create folder and file while working on project?
- Project Structure:
- Project_Name/
  - .git/
  - .gitignore
  - README.md
  - requirements.txt
  - setup.py
  - LICENSE
  - Project_Name/
    - __init__.py
    - module1.py
    - module2.py
    - module3.py
    - tests/
      - __init__.py
      - test_module1.py
      - test_module2.py
      - test_module3.py
  - docs/
    - requirements.txt
    - conf.py
    - index.rst
    - module1.rst
    - module2.rst
    - module3.rst
  - data/
    - input/
      - input1.csv
      - input2.csv
      - input3.csv
    - output/
      - output1.csv
      - output2.csv
      - output3.csv
  - notebooks/
    - notebook1.ipynb
    - notebook2.ipynb
    - notebook3.ipynb
  - scripts/
    - script1.py
    - script2.py
    - script3.py
  - etc.

## What is side effect?
- Side Effect: It is the effect of the function that is not related to the return value. **eg: print(), etc.**
- In python, the print() function is used to print the output on the screen it takes the input as a string and prints it on the screen.
- Here, the print() function has the side effect of printing the output on the screen.

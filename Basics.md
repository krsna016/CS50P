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

### Note : Parenthesis is not mandatory while using if, elif, else, for, while, etc. but it is recommended to use the parenthesis when required to make the code more readable.

## What is flowchart?
- Flowchart: It is the diagram that represents the flow of the program. **eg: start, input, process, decision, loop, output, end, etc.**
- We use : 
- Oval to represent the start and end of the program. 
- Parallelogram to represent the input and output of the program.
- Rectangle to represent the process of the program.
- Diamond to represent the decision of the program.
- etc.

### Note: The code is pythonic means the code is written in the pythonic way.

## What is match-case statement?
- Match-Case Statement: It is the statement that is used to match the value with the case and execute the block of code. **eg: match value: case 1: print("One") case 2: print("Two") case 3: print("Three") etc.**
- In python, the match-case statement is used to match the value with the case and execute the block of code.
- Here, the match-case statement is used to match the value with the case and execute the block of code.
- In python, the match-case statement is used to replace the switch-case statement.

## What is Magic Number?
- Magic Number: It is the number that is used in the code without any explanation. **eg: 10, 20, 30, etc.**
- In python, the magic number is used in the code without any explanation.

## What is Infinite Loop?
- Infinite Loop: It is the loop that runs indefinitely. **eg: while True: print("Hello")**

### Note : It's a convention to start counting from 0 in programming.
### Note : Python does not have a++ and a-- operators.
### Note : For - loop is used to iterate over the sequence of the elements.i.e list, tuple, set, dictionary, etc.
### Note : range() function is used to generate the sequence of the numbers.

## What is String concatenation and String replication?
- String Concatenation: It is the process of combining the strings. **eg: "Hello" + "World"**
- String Replication: It is the process of repeating the strings. **eg: "Hello" * 3**

## What is try-except block?
- Try-Except Block: It is the block that is used to handle the exceptions. **eg: try: except:**

### Note : It's the bad practice to use the except block catching all type of errors without the exception name, we should know the error the user might face and handle it accordingly.
### Note : It's a good practice that only a one or very few line should be in the try-block, that can actually raise the exception.

## What is syntactic sugar?
- Syntactic Sugar: It is the syntax that makes the code easier to read and write. **eg: list comprehension, dictionary comprehension, etc.**

## Explain try,except,else and finally block?
- Try Block: It is the block that is used to execute the block of code that can raise the exception. **eg: try:**
- Except Block: It is the block that is used to execute the block of code when the try block raises the exception. **eg: except:**
- Else Block: It is the block that is used to execute the block of code when the try block does not raise any exception. **eg: else:**
- Finally Block: It is the block that is used to execute the block of code whether the try block raises the exception or not. **eg: finally:**

## Scope in Different Programming Languages
### C and C++
- Block-scoped: Variables declared inside a block (within curly braces `{}`) have scope limited to that block.
### Java
- Block-scoped: Similar to C and C++, variables declared inside a block have scope limited to that block.
- Class-level scope: Variables declared at the class level (outside any method) are accessible throughout the class.
### Python
- Function-scoped: Variables declared inside a function have scope limited to that function.
- Module-level scope: Variables declared at the top level of a module are accessible throughout the module.
- Class-scoped: Variables inside a class are generally accessible within methods and class bodies.
### JavaScript
- Function-scoped: Variables declared inside a function have scope limited to that function.
- Block-scoped (with `let` and `const` in modern JavaScript): Variables declared using `let` and `const` have block-level scope.
### C# and .NET Languages
- Block-scoped: Similar to C and C++, variables declared inside a block have scope limited to that block.
- Class-level scope: Variables declared at the class level are accessible throughout the class.


## What is module and package?
- Module: It is the file that contains the python code. **eg: module.py**
- Package: It is the directory that contains the python code. **eg: package/**

## What is Library and Framework?
- Library: It is the collection of the modules and packages. **eg: numpy, pandas, matplotlib, etc.**
- Framework: It is the collection of the libraries and packages. **eg: Django, Flask, etc.**

## What is iterable and iterator?
- Iterable: It is the object that can be iterated. **eg: list, tuple, set, dictionary, etc.**
- Iterator: It is the object that can be iterated using the next() method. **eg: iter(), next(), etc.**

## what is Sequence and Collection?
- Sequence: It is the ordered collection of the elements. **eg: list, tuple, string, etc.**
- Collection: It is the unordered collection of the elements. **eg: set, dictionary, etc.**

### Note: All about import statement -
- Import Statement: It is the statement that is used to import the module or package. **eg: import module, import package, from module import function, from package import module, etc.**
- Different ways to import the module or package:
  - import module
  - import module as alias
  - from module import function
  - from module import function as alias
  - from module import *
  - from module import function1, function2, function3, etc.
  - from package import module
  - from package import module as alias
  - from package import module1, module2, module3, etc.
  - from package import *
  - etc.

### Note: Alias- It is the alternative name of the module or package.

## What is command line argument?
- Command Line Argument: It is the argument that is passed to the program when it is executed. **eg: python3 <file_name.py> arg1 arg2 arg3**
- In python, sys.argv is used to get the command line arguments using the "sys" module.

### Note: Python Style Guide - PEP 8:
- PEP 8: It is the style guide for the python code. **eg: indentation, line length, blank lines, comments, naming conventions, etc.**
- Link: https://www.python.org/dev/peps/pep-0008/
- According to PEP 8:
- The maximum line length should be 79 characters.
- The indentation should be 4 spaces.
- The blank lines should be used to separate the blocks of code.
- The comments should be used to explain the code.
- The naming conventions should be used to define the variable, function, class, etc.
   - snake_case for variable and function names.
   - PascalCase for class names.
   - UPPERCASE for constants.
   - etc.

## What is slicing?
- Slicing: It is the process of extracting the elements from the sequence. **eg: list[1:3], tuple[1:3], string[1:3], etc.**
- The slicing is inclusive of the start index and exclusive of the end index.

### PyPI - The Python Package Index: 
- PyPI: It is the repository of the software for the Python programming language. **eg: pip, etc.**
- Link: https://pypi.org/
- We can use the pip command to install the package from the PyPI.

## What is API?
- API: It is the application programming interface that is used to interact with the software. **eg: REST API, etc.**

## What is request Library?
- Request Library: It is the library that is used to send the HTTP requests. **eg: get(), post(), put(), delete(), etc.**
- Link: https://PyPI.org/project/requests/

### Note: The Zen of Python: (means, the principles of python)
- Readability counts.
- There should be one-- and preferably only one --obvious way to do it.
- Explicit is better than implicit.
- Simple is better than complex.
- Complex is better than complicated.
- Flat is better than nested.
- Sparse is better than dense.
- Now is better than never.
- Although never is often better than *right* now.
- If the implementation is hard to explain, it's a bad idea.
- If the implementation is easy to explain, it may be a good idea.
- Namespaces are one honking great idea -- let's do more of those!
- More about python slogans: https://www.python.org/dev/peps/pep-0020/

## What is pylint?
- Pylint: It is the tool that is used to check the quality of the python code. **eg: pylint <file_name.py>**
- Link: https://PyPI.org/project/pylint/

## What is pycodestyle?
- Pycodestyle: It is the tool that is used to check the style of the python code. **eg: pycodestyle <file_name.py>**
- Link: https://PyPI.org/project/pycodestyle/

## What is black?
- Black: It is the tool that is used to format the python code. **eg: black <file_name.py>**
- Link: https://PyPI.org/project/black/

## What is mypy?
- Mypy: It is the tool that is used to check the type of the python code. **eg: mypy <file_name.py>**
- Link: https://PyPI.org/project/mypy/

### Note : Trailing comma is used to define the single element tuple, list, set, dictionary, etc also it is used to define the multiple elements in the tuple, list, set, dictionary, etc.
- eg: (10,), [10,], {10,}, {10: 20,}, etc.
- eg: (10, 20, 30,), [10, 20, 30,], {10, 20, 30,}, {10: 20, 30: 40,}, etc.

## What is boylerplate code?
- Boilerplate Code: It is the code that is used in many places with little or no alteration. **eg: import os, import sys, etc.**
- In python, the import statement is used to import the module or package.

## What is "Assert" keyword?
- Assert Keyword: It is the keyword that is used to check the condition. **eg: assert condition, etc.**
- eg: assert a > 10, "a should be greater than 10" means if a is not greater than 10 then it will raise the AssertionError with the message "a should be greater than 10".

## What is unit testing?
- Unit Testing: It is the process of testing the individual unit of the code. **eg: unittest, pytest, etc.**
- In python, the unittest module is used to perform the unit testing.
- In python, the pytest module is used to perform the unit testing.
- Link: https://docs.python.org/3/library/unittest.html
- Link: https://docs.pytest.org/en/stable/


### Note : We use __init__.py file to define the package in python.

### Note: File I/0 in python:
- File I/O: It is the process of reading and writing the data from and to the file.
- In python, we can use the open() function to open the file. eg: open("file_name.txt", "r")
- In python, we can use the close() method to close the file. eg: file.close()
- In python, we can use the read() method to read the data from the file. eg: file.read()
- In python, we can use the write() method to write the data to the file. eg: file.write("Hello")
- In python, we can use the readline() method to read the line from the file. eg: file.readline()
- In python, we can use the readlines() method to read the lines from the file. eg: file.readlines()
- In python, we can use the seek() method to change the position of the file. eg: file.seek(0)
- In python, we can use the tell() method to get the position of the file. eg: file.tell()
- In python, we can use the with statement to open the file. eg: with open("file_name.txt", "r") as file:
- In python, we can use the read mode to read the file. eg: "r"
- In python, we can use the write mode to write the file. eg: "w"
- In python, we can use the append mode to append the file. eg: "a"
- In python, we can use the binary mode to read and write the binary file. eg: "rb", "wb", etc.
- In python, we can use the text mode to read and write the text file. eg: "rt", "wt", etc.
- In python, we can use the read and write mode to read and write the file. eg: "r+", "w+", etc.
- In python, we can use the binary and text mode to read and write the binary and text file. eg: "rb+", "wb+", "rt+", "wt+", etc.
- In python, we can use the os module to perform the file I/O operations. eg: os.open(), os.close(), os.read(), os.write(), etc.
- In python, we can use the shutil module to perform the file I/O operations. eg: shutil.copy(), shutil.move(), etc.
- In python, we can use the pathlib module to perform the file I/O operations. eg: Path.open(), Path.read_text(), Path.write_text(), etc.
- In python, we can use the pickle module to perform the file I/O operations. eg: pickle.dump(), pickle.load(), etc.
- In python, we can use the json module to perform the file I/O operations. eg: json.dump(), json.load(), etc.
- In python, we can use the csv module to perform the file I/O operations. eg: csv.reader(), csv.writer(), etc.
- etc.

### Note: Types of files:
- Text Files: It is the files that are used to store the text data. **eg: .txt, etc.**
- Binary Files: It is the files that are used to store the binary data. **eg: .jpg, .png, .pdf, etc.**
- csv Files: It is the files that are used to store the comma separated values. **eg: .csv, etc.**
- json Files: It is the files that are used to store the json data. **eg: .json, etc.**
- etc.

### Note: If we use double quotes inside the single quotes and single quotes inside the double quotes then we don't need to use the escape sequences.
- we should use the escape sequences when we use the same quotes inside the same quotes.
- eg: "Hello 'World'", 'Hello "World"'
- eg: 'Hello \'World\'', "Hello \"World\""


## What is regex?
- Regex: It is the sequence of characters that define the search pattern. **eg: re, etc.**
- It is also known as regular expression.
- In python, the re module is used to perform the regex operations.
- Link: https://docs.python.org/3/library/re.html


### Note: Regex using re module:
- "re" module is used to perform the regex operations.
- Here are some of the methods of the "re" module:
  - re.match(): It is used to match the pattern at the beginning of the string.
  - re.fullmatch(): It is used to match the pattern with the whole string.
  - re.search(): It is used to search the pattern in the string.
  - re.findall(): It is used to find all the occurrences of the pattern in the string.
  - re.finditer(): It is used to find all the occurrences of the pattern in the string and return the iterator.
  - re.sub(): It is used to substitute the pattern in the string.
  - re.split(): It is used to split the string based on the pattern.
  - Some PlaceHolders includes : 
    - "$" - Matches the end of the line.
    - "^" - Matches the start of the line.
    - "." - Matches any character except the newline character.
    - "*" - Matches the zero or more occurrences of the pattern.
    - "+" - Matches the one or more occurrences of the pattern.
    - "?" - Matches the zero or one occurrences of the pattern.
    - "|" - Matches the either or pattern.
    - "[]" - Matches the set of characters.
    - "()" - Matches the group of characters.
    - "{n}" - Matches the exactly n occurrences of the pattern.
    - "{n,}" - Matches the n or more occurrences of the pattern.
    - "{n,m}" - Matches the n to m occurrences of the pattern.
    - "\d" - Matches the digit character.
    - "\D" - Matches the non-digit character.
    - "\s" - Matches the whitespace character.
    - "\S" - Matches the non-whitespace character.
    - "\w" - Matches the word character.
    - "\W" - Matches the non-word character.
    - "\b" - Matches the empty string at the beginning or end of the word.
    - "\B" - Matches the empty string not at the beginning or end of the word.
    - Link: https://docs.python.org/3/library/re.html - More about re module.

### Note :
- 1) .+@.+   : Read as "Any character one or more times followed by @ symbol followed by any character one or more times"

- 2) ..* @.. * : Read as "Any character followed by any character zero or more times followed by @ symbol followed by any 
             character followed by any character zero or more times"

- 3) r".+@.+\.edu"  : Read as "Any character one or more times followed by @ symbol followed by any character one or more
                    times followed by a dot followed by edu"
                    
- 4) r"^.+@.+\.edu$" : Read as "Start of the string followed by any character one or more times followed by @ symbol 
                     followed by any character one or more times followed by a dot followed by edu followed by 
                     end of the string"

- 5) r"^[abcd]+@.+\.edu$" : Read as "Start of the string followed by a, b, c or d one or more times followed by @ symbol
                          followed by any character one or more times followed by a dot followed by edu followed by
                          end of the string"
                          
- 6) r"^[^@]+.+\.edu$" : Read as "Start of the string followed by any character except @ one or more times followed by
                       any character one or more times followed by a dot followed by edu followed by end of the string"

- 7) r"^[a-z]+@[a-z]+\.edu$" : Read as "Start of the string followed by a to z one or more times followed by @ symbol
                             followed by a to z one or more times followed by a dot followed by edu followed by  
                             end of the string"
                             
- 8) r"^[a-zA-Z]+@[a-zA-Z]+\.edu$" : Read as "Start of the string followed by a to z or A to Z one or more times followed
                                   by @ symbol followed by a to z or A to Z one or more times followed by a dot   
                                   followed by edu followed by end of the string"
                                   
- 9) r"^[a-zA-Z0-9_]+@[a-zA-Z0-9_]+\.edu$" : Read as "Start of the string followed by a to z or A to Z or 0 to 9 or _
                                           one or more times followed by @ symbol followed by a to z or A to Z or 0 to 9 
                                           or _ one or more times followed by a dot followed by edu followed by end of 
                                           the string"
                                        
- 10) r"^\w+@\w+\.edu$" : Read as "Start of the string followed by a to z or A to Z or 0 to 9 or _ one or more times
                        followed by @ symbol followed by a to z or A to Z or 0 to 9 or _ one or more times followed
                        by a dot followed by edu followed by end of the string"

- 11) r"^\w+@\w+\.(com|edu|in)$" : Read as "Start of the string followed by a to z or A to Z or 0 to 9 or _ one or more
                                 times followed by @ symbol followed by a to z or A to Z or 0 to 9 or _ one or more
                                 times followed by a dot followed by com or edu or in followed by end of the string"
                   
**---- If we want space---------------------**                                 
- 12) r"^[a-zA-Z0-9_ ]+@[a-zA-Z0-9_ ]+\.edu$ : Read as "Start of the string followed by a to z or A to Z or 0 to 9 or _
                                             or space one or more times followed by @ symbol followed by a to z or A to 
                                             Z or 0 to 9 or _ or space one or more times followed by a dot followed by
                                             edu followed by end of the string"
                                        
- 13) r"^(\w|\s)+@(\w|\s)+\.edu$" : Read as "Start of the string followed by a to z or A to Z or 0 to 9 or _ or space one
                                 or more times followed by @ symbol followed by a to z or A to Z or 0 to 9 or _ or 
                                 space one or more times followed by a dot followed by edu followed by end of the 
                                 string"

**-------------------------------------------**
                                 
- 14) r"^\w+@\w+\.\w+\.edu$" : Read as "Start of the string followed by a to z or A to Z or 0 to 9 or _ one or more
                             times followed by @ symbol followed by a to z or A to Z or 0 to 9 or _ one or more times
                             followed by a dot followed by a to z or A to Z or 0 to 9 or _ one or more times followed
                             by a dot followed by edu followed by end of the string"
                             
- 15) r"^\w+@(\w+\.)?\w+\.edu$" : Read as "Start of the string followed by a to z or A to Z or 0 to 9 or _ one or more 
                                times followed by @ symbol followed by (a to z or A to Z or 0 to 9 or _ one or more times
                                followed by a dot) - zero or one time followed by a to z or A to Z or 0 to 9 or _ one or
                                more times followed by a dot followed by edu followed by end of the string"    
                                
- 16) r"^(\w|\.)+@(\w+\.)?\w+\.edu$" : Read as "Start of the string followed by a to z or A to Z or 0 to 9 or _ or . one
                                    or more times followed by @ symbol followed by (a to z or A to Z or 0 to 9 or _ one
                                    or more times followed by a dot) - zero or one time followed by a to z or A to Z or 0
                                    to 9 or _ one or more times followed by a dot followed by edu followed by end of the
                                    string"

**also,**

- 16) r"^[a-zA-Z0-9_\.]+@(\w+\.)?\w+\.edu$" : Read as "Start of the string followed by a to z or A to Z or 0 to 9 or _ or . 
                                            one or more times followed by @ symbol followed by (a to z or A to Z or 0 to
                                            9 or _ one or more times followed by a dot) - zero or one time followed by a
                                            to z or A to Z or 0 to 9 or _ one or more times followed by a dot followed by
                                            edu followed by end of the string"  

### Note : \w is a shorthand character class and is equivalent to [a-zA-Z0-9_]
### Note : \d is a shorthand character class and is equivalent to [0-9]
### Note : \s is a shorthand character class and is equivalent to [\t\n\r\f\v]
### Note : \W is a shorthand character class and is equivalent to [^a-zA-Z0-9_]
### Note : \D is a shorthand character class and is equivalent to [^0-9]
### Note : \S is a shorthand character class and is equivalent to [^\t\n\r\f\v]

## What are FLAGS in regex?
- Flags: It is the special options that are used to modify the regex pattern. **eg: re.IGNORECASE, re.MULTILINE, re.DOTALL, etc.**
- re.IGNORECASE: It is used to ignore the case of the pattern.
- re.MULTILINE: It is used to match the pattern at the beginning of the line.
- re.DOTALL: It is used to match the pattern with the newline character.


### Note :
- Grouping:
    - (abc) : Matches the string "abc"
    - (a|b) : Matches either "a" or "b"
    - (?:abc) : Non-capturing group
    - (?P<name>abc) : Named capturing group
    - \1 : Matches the same text as most recently matched by the 1st capturing group
    - \2 : Matches the same text as most recently matched by the 2nd capturing group
    - \3 : Matches the same text as most recently matched by the 3rd capturing group
    - \A : Matches the start of the string
    - \Z : Matches the end of the string
    - \b : Matches the empty string at the beginning or end of a word
    - \B : Matches the empty string not at the beginning or end of a word
    - \d : Matches any decimal digit
    - \D : Matches any non-digit character
    - \s : Matches any whitespace character
    - \S : Matches any non-whitespace character
    - \w : Matches any alphanumeric character
    - \W : Matches any non-alphanumeric character
    - \t : Matches the tab character
    - \n : Matches the newline character
    - \r : Matches the carriage return character
    - \f : Matches the form feed character
    - \v : Matches the vertical tab character
    - (...) : Matches whatever regular expression is inside the parentheses, and indicates the start and end of a group
    - (?:...) : A non-capturing version of regular parentheses

### Note: Walrus Operator :=  - It is used to assign the value to the variable as well as return the value.

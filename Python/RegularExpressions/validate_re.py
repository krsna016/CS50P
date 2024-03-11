import re

# This regex : .+@.+ is used to validate that the email has atleast one character before and after the @ symbol
# ".+@.+" <==> "..*@..*" where . is any character and * is 0 or more times


r"""
1) .+@.+   : Read as "Any character one or more times followed by @ symbol followed by any character one or more times"

2) ..*@..* : Read as "Any character followed by any character zero or more times followed by @ symbol followed by any 
             character followed by any character zero or more times"

3) r".+@.+\.edu"  : Read as "Any character one or more times followed by @ symbol followed by any character one or more
                    times followed by a dot followed by edu"
                    
4) r"^.+@.+\.edu$" : Read as "Start of the string followed by any character one or more times followed by @ symbol 
                     followed by any character one or more times followed by a dot followed by edu followed by 
                     end of the string"

5) r"^[abcd]+@.+\.edu$" : Read as "Start of the string followed by a, b, c or d one or more times followed by @ symbol
                          followed by any character one or more times followed by a dot followed by edu followed by
                          end of the string"
                          
6) r"^[^@]+.+\.edu$" : Read as "Start of the string followed by any character except @ one or more times followed by
                       any character one or more times followed by a dot followed by edu followed by end of the string"

7) r"^[a-z]+@[a-z]+\.edu$" : Read as "Start of the string followed by a to z one or more times followed by @ symbol
                             followed by a to z one or more times followed by a dot followed by edu followed by  
                             end of the string"
                             
8) r"^[a-zA-Z]+@[a-zA-Z]+\.edu$" : Read as "Start of the string followed by a to z or A to Z one or more times followed
                                   by @ symbol followed by a to z or A to Z one or more times followed by a dot   
                                   followed by edu followed by end of the string"
                                   
9) r"^[a-zA-Z0-9_]+@[a-zA-Z0-9_]+\.edu$" : Read as "Start of the string followed by a to z or A to Z or 0 to 9 or _
                                           one or more times followed by @ symbol followed by a to z or A to Z or 0 to 9 
                                           or _ one or more times followed by a dot followed by edu followed by end of 
                                           the string"
                                        
10) r"^\w+@\w+\.edu$" : Read as "Start of the string followed by a to z or A to Z or 0 to 9 or _ one or more times
                        followed by @ symbol followed by a to z or A to Z or 0 to 9 or _ one or more times followed
                        by a dot followed by edu followed by end of the string"
                        
11) r"^\w+@\w+\.(com|edu|in)$" : Read as "Start of the string followed by a to z or A to Z or 0 to 9 or _ one or more
                                 times followed by @ symbol followed by a to z or A to Z or 0 to 9 or _ one or more
                                 times followed by a dot followed by com or edu or in followed by end of the string"
                   
---- If we want space---------------------                                 
12) r"^[a-zA-Z0-9_ ]+@[a-zA-Z0-9_ ]+\.edu$ : Read as "Start of the string followed by a to z or A to Z or 0 to 9 or _
                                             or space one or more times followed by @ symbol followed by a to z or A to 
                                             Z or 0 to 9 or _ or space one or more times followed by a dot followed by
                                             edu followed by end of the string"
                                        
13) r"^(\w|\s)+@(\w|\s)+\.edu$" : Read as "Start of the string followed by a to z or A to Z or 0 to 9 or _ or space one
                                 or more times followed by @ symbol followed by a to z or A to Z or 0 to 9 or _ or 
                                 space one or more times followed by a dot followed by edu followed by end of the 
                                 string"
-------------------------------------------
                                 
14) r"^\w+@\w+\.\w+\.edu$" : Read as "Start of the string followed by a to z or A to Z or 0 to 9 or _ one or more
                             times followed by @ symbol followed by a to z or A to Z or 0 to 9 or _ one or more times
                             followed by a dot followed by a to z or A to Z or 0 to 9 or _ one or more times followed
                             by a dot followed by edu followed by end of the string"
                             
15) r"^\w+@(\w+\.)?\w+\.edu$" : Read as "Start of the string followed by a to z or A to Z or 0 to 9 or _ one or more 
                                times followed by @ symbol followed by (a to z or A to Z or 0 to 9 or _ one or more times
                                followed by a dot) - zero or one time followed by a to z or A to Z or 0 to 9 or _ one or
                                more times followed by a dot followed by edu followed by end of the string"    
                                
16) r"^(\w|\.)+@(\w+\.)?\w+\.edu$" : Read as "Start of the string followed by a to z or A to Z or 0 to 9 or _ or . one
                                    or more times followed by @ symbol followed by (a to z or A to Z or 0 to 9 or _ one
                                    or more times followed by a dot) - zero or one time followed by a to z or A to Z or 0
                                    to 9 or _ one or more times followed by a dot followed by edu followed by end of the
                                    string"                               
also,

16) r"^[a-zA-Z0-9_\.]+@(\w+\.)?\w+\.edu$" : Read as "Start of the string followed by a to z or A to Z or 0 to 9 or _ or . 
                                            one or more times followed by @ symbol followed by (a to z or A to Z or 0 to
                                            9 or _ one or more times followed by a dot) - zero or one time followed by a
                                            to z or A to Z or 0 to 9 or _ one or more times followed by a dot followed by
                                            edu followed by end of the string"                      
"""

email = input("Enter the E-mail : ").strip()
if re.search(r"^(\w|\.)+@(\w+\.)?\w+\.edu$", email, re.IGNORECASE):
    print("Valid")
else:
    print("Invalid")
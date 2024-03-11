"""
r"^.+, .+$" : Read as "Starts with any character, one or more times, followed by a comma, a space, followed by
              any character one or more times followed by the end of the string"

r"^(.+)(, |,)(.+)$" : Read as "Starts with any character, one or more times, followed by (a comma, a space) or a comma,
                      followed by any character one or more times followed by the end of the string"

r"^(.+), ?(.+)$" : Read as "Starts with any character, one or more times, followed by a comma, followed by an optional
                   space, followed by any character one or more times followed by the end of the string"

r"^(.+), *(.+)$" : Read as "Starts with any character, one or more times, followed by a comma, followed by a space
                   zero or more times, followed by any character one or more times followed by the end of the string"
"""

import re

name = input("What's your name? : ").strip()

# We can surround the pattern with () to capture the groups, infect this is also used for grouping so don't be confused
# i.e (.+), (.+) are the groups which are captured by the pattern
# and (, |,) is the non-capturing group which is used to match the comma and space or just a comma

# Here we are first assigning the return value of the re.search() method to the matches variable and then
# using the walrus operator (:=) which is checking the boolean value of the matches variable is True or False:

if matches := re.search(r"^(.+)(?:, |,)(.+)$", name):
    # Here we are using the groups() method to get the groups which are captured by the pattern i.e (.+), (.+)

    # last, first = matches.groups()
    # name = f"{first} {last}"
    # Also,

    # last = matches.group(1)
    # first = matches.group(2)
    # name = f"{first} {last}"
    # Also,

    name = matches.group(2) + " " + matches.group(1)

print("Your name is :", name)

r"""

r"^https://twitter.com/"  ==> There's a typo in the regex. It should be r"^https?://twitter\.com/".

r"^(https|http)://twitter\.com/"   ==> Read as "Starts with either https://twitter.com/ or http://twitter.com/".

r"^https?://twitter\.com/"  ==> Read as "Starts with either http://twitter.com/ or https://twitter.com/".

r"^https?://(www\.)?twitter\.com/"  ==> Read as "Starts with either http://twitter.com/ or https://twitter.com/ and may
                                      or may not have www.".

r"^https?://(www\.|)twitter\.com/"  ==> Read as "Starts with either http://twitter.com/ or https://twitter.com/ and may
                                      or may not have www.".

"""

import re

url = input("Input url of you Twitter : ").strip()
# username = url.replace("https://twitter.com/", "")

"""
Approach 1:
Here we are searching for the pattern/regex in the input() and if it's there will be
replacing it with empty string.
"""

# username = re.sub(r"(^https?://)?(www\.)?twitter\.com/","",url)
# print(f"Username is : {username}")

"""
Approach 2:
Here we are searching for the pattern/regex in the input() and if it's there will be
capturing the username.
"""

matches = re.search(r"^https?://(?:www\.)?twitter\.com/([a-z0-9_]+)$", url, re.IGNORECASE)
if matches:
    # matches.group(1) is www. or None
    # We not use matches.group(1) because we don't need it.
    # So we can make it un-capturing group by using (?:)
    username = matches.group(1)
    print(f"Username is : {username}")
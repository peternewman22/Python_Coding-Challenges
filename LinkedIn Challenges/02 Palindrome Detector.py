def is_palindrome(w: str) -> bool:
    """Takes a string and returns true if that string (ignoring case, spacing and punctuation) is the same forwards and backwards"""
    punctuation = [".",",",";","'",'"',"!","?"," "]
    # remove whitespaces and make all lowercase 
    w_clean = "".join(filter(lambda x: x not in punctuation, list(w.lower())))
    w_mirror = "".join(reversed(w_clean))
    return w_clean == w_mirror

# print(is_palindrome("Eva, can I see bees in a cave?"))

# now using regular expressions to just pull all the lower case letters out...
import re

def is_palindrome_regular_expressions(w: str) -> bool:
    forwards = "".join(re.findall('[a-z]+',w.lower()))
    backwards = forwards[::-1]
    return forwards == backwards

print(is_palindrome_regular_expressions("Eva, can I see bees in a cave?"))
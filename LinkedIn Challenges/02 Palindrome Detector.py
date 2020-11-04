def is_palindrome(w: str) -> bool:
    """Takes a string and returns true if that string (ignoring case, spacing and punctuation) is the same forwards and backwards"""
    punctuation = [".",",",";","'",'"',"!","?"," "]
    # remove whitespaces and make all lowercase 
    w_clean = "".join(filter(lambda x: x not in punctuation, list(w.lower())))
    w_mirror = "".join(reversed(w_clean))
    return w_clean == w_mirror

print(is_palindrome("Eva, can I see bees in a cave?"))
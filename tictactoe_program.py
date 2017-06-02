def add_underscores(s):
    """ (str) -> str
    
    >>> add_underscores("cat")
    "c_a_t"
    
    """
    result = ""
    for char in s:
        result = result + char + "_"
    return result[:-1]

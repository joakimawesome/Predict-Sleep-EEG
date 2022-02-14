"""Create appropriate format for search terms."""

def format_terms(words: list[str], tool: str):
    """
    Parameters
    ----------
    words : list of str
    tool : {'urllib', 'lisc'}
        Package name that performs the search.
        
    Returns
    -------
    str : containing the terms as substrings in double quotes joined by "OR" as per urllib format.
    list : containing the terms in double quotes as per lisc format.
    """
    
    if tool == 'urllib':
        return ' OR '.join([f'"{word}"' for word in words])
    elif tool == 'lisc':
        return [f'"{word}"' for word in words]
    else:
        raise Exception("Argument 'tool' missing. Must be 'urllib' or 'lisc'.")

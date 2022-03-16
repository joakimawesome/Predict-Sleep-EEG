""" """

def format_terms(words: list[str], tool: str) -> str:
    if tool == 'urllib':
        return ' OR '.join([f'"{word}"' for word in words])
    elif tool == 'lisc':
        return [f'"{word}"' for word in words]
    else:
        raise Exception("Argument 'tool' missing. Must be 'urllib' or 'lisc'.")
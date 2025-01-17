

def join(separator: str, separated: list[str]) -> str:

    
    for word_or_phrase in separated:
        
        if not isinstance(word_or_phrase, str):
            raise Exception("join() accepts only strings")

    joined: str = ""
    last_index: int = len(separated) - 1
    for word_or_phrase in separated[:last_index]:
        
        joined += word_or_phrase + separator

    
    if separated != []:
        joined += separated[last_index]

    
    return joined


if __name__ == "__main__":
    from doctest import testmod

    testmod()

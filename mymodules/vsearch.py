def search4vowels(phrase: str) -> set:
    """return any vowels found in a supplied phrase."""
    vowels = set('aeiou')
    return vowels.intersection(set(phrase))


def search4letters(phrase: str, letters: str = 'aeiou') -> set:
    """return a set of the letters found in 'phrase'."""
    return set(letters).intersection(set(phrase))

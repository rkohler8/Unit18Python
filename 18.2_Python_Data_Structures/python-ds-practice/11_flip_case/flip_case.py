def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    newPhrase = []
    for letter in phrase:
        if letter.lower() == to_swap.lower():
            if letter.isupper():
                newPhrase.extend(letter.lower())
            elif letter.islower():
                newPhrase.extend(letter.upper())
        else:
            newPhrase.extend(letter)
    return ''.join(newPhrase)

# DONE
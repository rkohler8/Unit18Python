def capitalize(phrase):
    """Capitalize first letter of first word of phrase.

        >>> capitalize('python')
        'Python'

        >>> capitalize('only first word')
        'Only first word'
    """

    retPhrase = phrase.split(" ")
    retPhrase[0] = retPhrase[0].capitalize()

    return ' '.join(retPhrase)

# DONE
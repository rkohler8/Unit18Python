def reverse_string(phrase):
    """Reverse string,

        >>> reverse_string('awesome')
        'emosewa'

        >>> reverse_string('sauce')
        'ecuas'
    """

    wordBack = ""
    for i in range(1, len(phrase)+1):
        wordBack += phrase[-i]
    return wordBack

# DONE
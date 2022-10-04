def titleize(phrase):
    """Return phrase in title case (each word capitalized).

        >>> titleize('this is awesome')
        'This Is Awesome'

        >>> titleize('oNLy cAPITALIZe fIRSt')
        'Only Capitalize First'
    """
    sep = phrase.lower().split(" ")
    return " ".join([word.capitalize() for word in sep])

# DONE

# return phrase.title()
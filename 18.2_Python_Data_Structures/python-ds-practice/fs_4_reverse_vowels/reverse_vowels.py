def reverse_vowels(s):
    """Reverse vowels in a string.

    Characters which re not vowels do not change position in string, but all
    vowels (y is not a vowel), should reverse their order.

    >>> reverse_vowels("Hello!")
    'Holle!'

    >>> reverse_vowels("Tomatoes")
    'Temotaos'

    >>> reverse_vowels("Reverse Vowels In A String")
    'RivArsI Vewols en e Streng'

    reverse_vowels("aeiou")
    'uoiea'

    reverse_vowels("why try, shy fly?")
    'why try, shy fly?''
    """

    # vowels = ['a', 'e', 'i', 'o', 'u']
    vowels = set('aeiouAEIOU')
    vows = []
    indexes = []
    ret_list = list(s)

    for i in range(len(s)):
        if s[i] in vowels:
            vows.append(s[i])
            indexes.append(i)
    
    for x in range(len(vows)):
        ret_list[indexes[-x - 1]] = vows[x]

    return "".join(ret_list)

# DONE
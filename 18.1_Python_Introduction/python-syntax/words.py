def print_upper_words(letters, words):
    """ print all words in words uppercased on separate lines

    """

    for word in words:
        for letter in letters:
            if word[0].lower() == letter:
                print(word.upper())


print("w, b, g; word, words, world, event, grass, brown, green")
print_upper_words(["w", "b", "g"], ["word", "words", "world", "event", "grass", "brown", "green"])
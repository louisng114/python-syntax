def print_upper_words(words, must_start_with={"e"}):
    """For a list of words, print out each word on a separate line, but in all uppercase."""
    
    for word in words:
        for letter in must_start_with:
            if word.startswith(letter):
                print(word.upper())


print_upper_words(["hello", "hey", "goodbye", "yo", "yes"],
                   must_start_with={"h", "y"})
def print_upper_words(words,must_start_with):

    for word in words:
        if word[0].upper() in must_start_with or word[0].lower() in must_start_with:
            print(word.upper())


        
print_upper_words(["hello", "hey", "goodbye", "yo", "yes"], {'h', 'y'})

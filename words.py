def print_upper_words(words, matching_letters):
    # print each word on a seperate line in uppercase
    upper_letters = [letter.upper() for letter in matching_letters]
    e_words = [word for word in words if word[0].upper() in upper_letters]
    for e_word in e_words:
        print (e_word.upper())

print_upper_words(['apple', 'banana','peanuts', 'eggs', 'Eagle'], {'e', 'b'})
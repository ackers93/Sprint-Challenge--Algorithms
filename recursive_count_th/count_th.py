'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''


def count_th(word):
    # define the searched for term
    sub_string = 'th'
    # define the length of the 'word' argument
    word_length = len(word)
    # sets the length the searched for term for iteration purposes
    count = len(sub_string)
    # if the word is to small be be tested, if will return 0
    if word_length == 0 or word_length < count:
        return 0
    # this checks if the word is contained in the selected letter until
    # the end of the length of the 'count' varaible.
    # if it is, 1 is added to a the call stack.
    elif word[0: count] == sub_string:
        return count_th(word[count - 1:]) + 1
    # if it wasn't contianed in the previous selection,
    # we will continue onto the next letter .
    else:
        return count_th(word[count - 1:])


# Once it has run through each letter, it will piece by piece dismantle the call stack
# as it goes it will count and return the amount of times that "sub_string" appears.

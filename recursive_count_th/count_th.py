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
    # TBC

    if word_length == 0 or word_length < count:
        return 0
    elif word[0: count] == sub_string:
        return count_th(word[count - 1:]) + 1
    else:
        return count_th(word[count - 1:])

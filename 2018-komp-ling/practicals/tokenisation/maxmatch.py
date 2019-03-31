def max_match(sentence, dictionary):
"""
sentence - a sentence for tokenisation
dictionary - a list of unique words

"""
    for i in range(len(sentence)-1, -1, -1):
        first_word = (sentence[0:i+1])
        keeper = sentence[i+1:len(sentence)]
        if first_word in dictionary:
            return [first_word] + max_match(keeper, dictionary)

    first_word = sentence[0]
    keeper = sentence[1:len(sentence)]

    return [first_word] + max_match(keeper, dictionary)
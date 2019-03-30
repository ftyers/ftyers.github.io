def maxmatch(sentence, dictionary):
    if len(sentence) == 0:
        return []

    for i in range(len(sentence), -1, -1):
        word = sentence[:i]
        remainder = sentence[i:]

        if word in dictionary or i == 1:
            return [word] + maxmatch(remainder, dictionary)




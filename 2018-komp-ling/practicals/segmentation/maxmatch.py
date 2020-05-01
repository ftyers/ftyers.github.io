# max_match
# sentence – предложение, которое предстоит токенизировать
# wordlist - список уникальных словоформ, по которым происходит поиск токенов
def max_match(sentence, wordlist):
    if not sentence:
        return []
    for i in range(len(sentence)-1, -1, -1):
        first_word = (sentence[0:i+1])
        remainder = sentence[i+1:len(sentence)]
        if first_word in wordlist:
            return [first_word] + max_match(remainder, wordlist)

    # если слово не найдено, то создаем новое односимвольное слово
    first_word = sentence[0]
    remainder = sentence[1:len(sentence)]

    return [first_word] + max_match(remainder, wordlist)
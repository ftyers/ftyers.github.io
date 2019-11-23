import re
sentence = []


def max_match(text, dictionary):
    inword = ""
    outword = ""
    global sentence
    for letter in text:
        inword += letter
        if inword in dictionary:
            outword = inword
    # start lines added to block segmentation of digits and english words
    if re.search("^「([ -~]+)」", inword):
        match = re.search("^「([ -~]+)」", inword)
        sentence.append("「")
        sentence.append(match.group(1))
        sentence.append("」")
        replacement = "「" + match.group(1) + "」"
        text = text.replace(replacement, "", 1)
        return text
    elif re.search("^([ -~]+)[^ -~]", inword):
        match = re.search("^([ -~]+)[^ -~]", inword)
        sentence.append(match.group(1))
        text = text.replace(match.group(1), "", 1)
        return text
    # end lines added to block segmentation of digits and english words
    elif outword in dictionary:
        sentence.append(outword)
        text = text.replace(outword, "", 1)
        return text
    else:
        sentence.append(text[0])
        text = text.replace(text[0], "", 1)
        return text


if __name__ == '__main__':
    sent = input("Input sentence file here: ")
    dic = input("Input dictionary name here: ")
    final = ""
    with open(dic, "r", encoding="utf-8") as f:
        diction = f.readlines()
        for index, entry in enumerate(diction):
            diction[index] = entry.replace("\n", "")
        with open("maxmatchtokens.txt", "w+", encoding="utf-8") as r:
            with open(sent, "r", encoding="utf-8") as m:
                senten = m.readlines()
                for inp in senten:
                    while True:
                        if len(inp) > 0:
                            inp = max_match(inp, diction)
                        else:
                            break
                final = " ".join(sentence)
                final = re.sub("\s\\n\s", r"\n", final)
                r.write(final)

import re


def sentence_extract(filename):
    with open(filename, "r", encoding="utf-8") as f:
        l = f.readlines()
        sentlist = []
        for line in l:
            if re.search("^# text = (.+)", line):
                s = re.search("^# text = (.+)", line).group(1)
                sentlist.append(s)
        sentlist = "\n".join(sentlist)
        return sentlist


if __name__ == "__main__":
    with open("sentencelist.txt", "w+", encoding="utf-8") as r:
        filename = input("Enter filename here: ")
        test = sentence_extract(filename)
        r.write(test)

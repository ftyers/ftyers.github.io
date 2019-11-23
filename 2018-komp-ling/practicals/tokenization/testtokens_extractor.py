import re


def sent_extract(filename):
    with open(filename, "r", encoding="utf-8") as f:
        l = f.readlines()
        dict = []
        for line in l:
            if line[0].isdigit():
                if line[0] == "1" and line[1].isspace():
                    s = line.split("\t")
                    dict.append("\n" + s[1])
                else:
                    s = line.split("\t")
                    dict.append(s[1])
        dict = " ".join(dict)
        dict = re.sub("\s\\n", "\n", dict)
        dict = dict.lstrip("\s\n")
        return dict


if __name__ == "__main__":
    with open("testtokens.txt", "w+", encoding="utf-8") as r:
        filename = input("Enter filename here: ")
        r.write(sent_extract(filename))

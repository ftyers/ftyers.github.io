def dict_extract(filename):
    with open(filename, "r", encoding="utf-8") as f:
        l = f.readlines()
        dict = []
        for line in l:
            if line[0].isdigit():
                s = line.split("\t")
                dict.append(s[1])
        dict = set(dict)
        return dict


if __name__ == "__main__":
    with open("dictionary.txt", "w+", encoding="utf-8") as r:
        filename = input("Enter filename here: ")
        r.write("\n".join(dict_extract(filename)))

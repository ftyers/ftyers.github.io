def create_dictionary (dictionary_source):
    wordforms = set()
    openfile = open(dictionary_source,"r",encoding="utf-8") 
    for line in openfile:
        splitline = line.split('\t')
        if len(splitline) > 4:
            wordform = splitline[1]
            wordforms.add(wordform)
    return wordforms
    openfile.close()

if __name__ == '__main__':
    with open("dictionary.txt", "w+", encoding="utf-8") as f:
        dictionary_source = input("Enter name of the train file: ")
        f.write("\n".join(create_dictionary(dictionary_source)))
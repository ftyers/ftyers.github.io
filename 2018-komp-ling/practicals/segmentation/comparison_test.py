with open("D:\loren\OneDrive\Documenti\Program\OOBOONTOO\Practical_1_Wiki\wikicomparetest.txt", "r", encoding="utf-8") as r:
    with open("D:\loren\OneDrive\Documenti\Program\OOBOONTOO\Practical_1_Wiki\wikicomparenltk.txt", "r", encoding="utf-8") as f:
        filetest = r.readlines()
        filecomp = f.readlines()
        mistake = []
        counter = 0
        check = False
        for index2, line2 in enumerate(filetest):
            filetest[index2] = line2.rstrip(" \n")
        for index1, line1 in enumerate(filecomp):
            filecomp[index1] = line1.rstrip(" \n")
        for line1 in filecomp:
            if line1 in filetest:
                counter += 1
            else:
                mistake.append(line1)
        print(counter, "\n", "\n".join(mistake))

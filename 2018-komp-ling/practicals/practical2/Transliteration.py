Transliteration


text = open("filename", 'r')
def transliteration(text):
    cyrillic = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    latin = 'a|b|v|g|d|e|yo|zh|z|i|i|k|l|m|n|o|p|r|s|t|u|f|kh|tc|ch|sh|shch||y||y|yu|ya'.split('|')
    trantab = {k:v for k,v in zip(cyrillic,latin)}
    newtext = ''
    for ch in text:
        casefunc =  str.capitalize if ch.isupper() else str.lower
        newtext += casefunc(trantab.get(ch.lower(),ch))
    return newtext
if __name__ == "__main__": 


Пример :
    s = 'Литва́ (), официальное название — Лито́вская Респу́блика () — государство, расположенное в Северной Европе (одна из стран Балтии). Столица страны — Вильнюс.'
    print(transliteration(s))

Litvá (), ofitcialnoe nazvanie — Litóvskaya Respúblika () — gosudarstvo, raspolozhennoe v Severnoi Evrope (odna iz stran Baltii). Stolitca strany — Vilnyus.

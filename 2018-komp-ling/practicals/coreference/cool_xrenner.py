import xrenner


cool_xrenner = xrenner.Xrenner(model = './eng')
# eng text
with open('coref.html', 'w+', encoding='utf-8') as f:
    f.write(cool_xrenner.analyze('eng.conllu', 'html'))
    f.close()

rusxrenner = xrenner.Xrenner(model = './rus')
# cool pushkin
with open('coref_pushkin.html', 'w+', encoding='utf-8') as c:
    c.write(rusxrenner.analyze('pushkin.conllu', 'html'))
    c.close()

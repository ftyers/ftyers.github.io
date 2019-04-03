import os


script_dir = os.path.dirname(__file__)
rel_path_text = "text"
abs_path_text = os.path.join(script_dir,rel_path_text)


dict = {'А': 'A', 'а': 'a','Б':'B','б':'b','В':'V','в':'v','Г':'G','г':'g','Д':'D','д':'d','Е':'Ye','е':'ye','Ё':'Yo','ё':'yo','Ж':'Zh','ж':'zh','З':'Z','з':'z','И':'I','и':'i','Й':'Y','й':'y','К':'K','к':'k','Л':'L','л':'l','М':'M','м':'m','Н':'N','н':'n','О':'O','о':'o','П':'P','п':'p','Р':'R','р':'r','С':'S','с':'s','Т':'T','т':'t','У':'U','у':'u','Ф':'F','ф':'f','Х':'H','х':'h','Ц':'Ts','ц':'ts','Ч':'Ch','ч':'ch','Ш':'Sh','ш':'sh','Щ':'Sh','щ':'sh','Ъ':'Y','ъ':'y','Ы':'Ei','ы':'ei','Ь':'','ь':'','Э':'E','э':'e','Ю':'Yu','ю':'yu','Я':'Ya','я':'ya'}

trans = []

with open(abs_path_text,'r') as text:
    text = text.read()
    for i in text:
        if i in dict:
            trans.append(dict[i])
        else:
            trans.append(i)
    trans = ''.join(trans)


while ' yeye' in trans:
    trans = trans.replace(' yeye', ' yeyo')

while 'ogo ' in trans:
    trans = trans.replace('ogo ', 'ovo ')

while 'ego ' in trans:
    trans = trans.replace('ego ', 'evo ')

print(trans)

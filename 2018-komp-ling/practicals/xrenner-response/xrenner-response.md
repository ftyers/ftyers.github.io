# Practice with xrenner

I tried to modify the standard Udx Xrenner model to make a coreference resolution for _azazel.conllu_ file (a summary of Boris Akunin's "Azazel" novel, _azazel.txt_). 

I added some entities in _entities.tab_:
```

общественный парк	place	place	1
Эраст Фандорин	person	person/male	1
молодой человек	person	person/male	1
Москва	place	place	1
Петр Кокорин	person	person/male	1
Амалия Бежецкая	person	person/female	1
Ипполит Зуров	person	person/male	1
студент Ахтырцев	person	person/male	1
леди Эстер	person person/female	1
англичанка Маргарета Эстер	person	person/female 	1
Иван Францевич Бриллинг	person	person/male	1
Петербург	place	place	1
Лондон	place	place	1
портфель	object	object	1
Россия	place	place	1

```
And also in _entity_heads.tab_:

```
Эраст	person	person/male	1
Фандорин	person	person/male	1
Амалия	person	person/female	1
Бежецкая	person	person/female	1
Эстер	person	person/female	1
англичанка	person	person/female	1
Маргарета	person	person/female	1
Ахтырцев	person	person/male	1
студент	person	person/male	1
следователь	person	person/male	1
Бриллинг	person	person/male	1
красавица	person	person/female	1
дама	person	person/female	1
Бриллинг	person	person/male	1
сыщик	person	person/male	1
директор	person	person/male	1

```

And also in _names.tab_:
```
Эраст Фандорин	male
Петр Кокорин	male
Амалия Бежецкая	female
Ипполит Зуров	male
Ахтырцев	male
Маргарета Эстер	female
Иван Францевич Бриллинг	male
Каннингем	male
```
I also added Russian pronouns in _pronouns.tab_ and tried to improve coreference detection by adding 
```
Фандорин|Эраст|Эраст Фандорин	coref
```
into the _coref.tab_ (that did not work though - "Эраст Фандорин" and "Эраст" did not match). 

The result of my experiments can be seen in _azazel.html_.

I tried to make some changes in the _coref_rules.tab_, but that did not make any impact into the _azazel.html_ file.

In conclusion, it was very difficult to understand how to build my own working Russian model without understandable examples. I hope that someone will explain to me in the future how Xrenner actually works or that someone will make a user-friendly interface for it.  

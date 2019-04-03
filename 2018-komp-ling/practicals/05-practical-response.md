 # Anaphora & co-reference resolution

## Model
I used preprocessed text file `pushkin.conllu`

## Xrenner

I made folder structure for Russian (based on default config of xrenner) and added couple of rules to catch surnames (the files are in `xrenner` subfolder). Then I run:

`xrenner.py -m rus -o html pushkin.conllu > pushkin.html`

Personal names where successfully detected. Result is in `pushkin.html`.
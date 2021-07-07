wget -q -O fear.html  "http://ru.wiktionary.org/wiki/страх"
wget -q -O tree.html  "http://ru.wiktionary.org/wiki/дерево"
cat fear.html | python3 wiktionary.py
cat tree.html | python3 wiktionary.py
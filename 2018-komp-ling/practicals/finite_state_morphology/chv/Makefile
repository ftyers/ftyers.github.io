all:
	hfst-lexc chv.lexc -o chv.lexc.hfst
	hfst-lexc chv.mor -o chv.mor.hfst
	hfst-twolc chv.twol -o chv.twol.hfst
	hfst-compose-intersect -1 chv.lexc.hfst -2 chv.twol.hfst -o chv.gen.hfst

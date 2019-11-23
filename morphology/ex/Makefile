all:
	hfst-lexc grn.lexc -o grn.lexc.hfst
	hfst-twolc grn.twol -o grn.twol.hfst
	hfst-compose-intersect -1 grn.lexc.hfst -2 grn.twol.hfst -o grn.gen.hfst


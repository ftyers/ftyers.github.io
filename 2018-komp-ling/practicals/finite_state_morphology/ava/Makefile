all:
	hfst-lexc ava.lexc -o ava.lexc.hfst
	hfst-twolc ava.twoc -o ava.twoc.hfst
	hfst-invert ava.lexc.hfst | hfst-compose-intersect -1 - -2 ava.twoc.hfst | hfst-invert -o ava.gen.hfst

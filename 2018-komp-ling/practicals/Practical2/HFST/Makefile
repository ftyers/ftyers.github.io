all:
	hfst-lexc d_lexc.lexc -o d_lexc.lexc.hfst
	hfst-twolc rule_n.twol -o rule_n.twol.hfst
	hfst-compose-intersect -1 d_lexc.lexc.hfst -2 rule_n.twol.hfst -o d_res.hfst

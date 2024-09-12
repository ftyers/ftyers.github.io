#!/usr/bin/python
# -*- coding: utf-8-*-

import hfst, sys

ifs = hfst.HfstInputStream('chv.gen.hfst') # set up an input stream
transducer = ifs.read()                    # read the first transducer
transducer.invert()                        # invert the transducer
transducer.lookup(sys.stdin)                  # analyse a token

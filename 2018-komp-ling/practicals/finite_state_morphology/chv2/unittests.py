import hfst

ifs = hfst.HfstInputStream('chv.gen.hfst')
transducer = ifs.read()
errors_analysis = 0
errors_synthesis = 0
with open("unittests.tsv") as f:
   for num, s in enumerate(f):
      action, analytic, synthetic = s.strip().split("\t")
      if action not in ["<", ">", "_"]:
         raise ValueError("action, must be <, > or -, but it's {act} "
                          "at {num}".format(
         act = action
         ))
         
      if action in ["<", "_"]:
         system_analysis = transducer.lookup(synthetic)[0][0].replace("@_EPSILON_SYMBOL_@", "")
         if analytic != system_analysis:
            errors_analysis += 1
            print("Analitic error at line {num} where word {synthetic} "\
                  "must be interpreted as {analytic} "
                  "but is interpreted as {system_analytic}".format(
                  num = num, synthetic = synthetic, analytic = analytic,
                  system_analytic = system_analytic
))

      if action in [">", "_"]:
         system_synthesis = transducer.lookup(analytic)[0][0].replace("@_EPSILON_SYMBOL_@", "")
         if synthetic != system_synthesis:
            errors_analysis += 1
            print("Synthetic error at line {num} where word {analytic} "\
                  "must be interpreted as {synthetic} "
                  "but is interpreted as {system_synthesis}".format(
                  num = num, synthetic = synthetic, analytic = analytic,
                  system_synthesis = system_synthesis
))

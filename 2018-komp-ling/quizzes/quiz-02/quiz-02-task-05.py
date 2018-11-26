import sys

softs = ["ch", "sh", "tz", "s", "x"]
for line in sys.stdin:
   for soft in softs:
      line = line.replace(soft + "<PL>", soft + "es")
   
   line = line.replace("<pl>", "s")
   print(line)

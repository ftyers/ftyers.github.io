soft = ["ch", "sh", "tz", "s", "x"]
word = input()
if any(word.endswith(s) for s in soft):
    print(word + "es")
else:
    print(word + "s")

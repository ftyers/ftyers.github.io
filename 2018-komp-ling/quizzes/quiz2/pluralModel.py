import sys
import re

dictionary = {'ch<PL>':'ches', 'sh<PL>':'shes', 'tz<PL>':'tzes', 's<PL>':'ses', 'x<PL>':'xes'}

def main():
    global dictionary
    text = sys.stdin.read()
    for i, j in dictionary.items():
        text = text.replace(i, j)
    text = re.sub('<PL>', 's', text)
    print(text)

if __name__ == "__main__":
    main()

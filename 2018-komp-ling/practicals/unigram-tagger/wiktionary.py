import re
import requests
from bs4 import BeautifulSoup as bs


def wiki(cool_word):
    
    article = bs(requests.get('http://ru.wiktionary.org/wiki/' + cool_word).text, 'html5lib')
    stem = str([s for s in article.select('p') if 'Корень' in str(s)][0].text).strip('. \n')
    if 'окончание' in stem:
        stem = stem.split('окончание')[0].strip('; ')
    pronunciation = re.findall('МФА:\s.+', str(article.get_text()))[0].replace('\xa0', ' ').replace('(файл)', '').split('[')[1].split(']')[0]
    declension = str([d for d in article.find_all('p') if 'склонение' in str(d)][0].text).replace('\xa0', ' ').split('тип склонения')[1].split()[0].strip()
        
    return print(stem, 'IPA: {}'.format(pronunciation), 'Зализняк: {}'.format(declension), sep='\n')


def main():
    cool_word = str(input())
    wiki(cool_word)

if __name__ == '__main__':
    main()

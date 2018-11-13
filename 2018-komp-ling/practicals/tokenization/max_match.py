#with open('words_new.txt') as f:
#    all_words = f.read().split('\n')

import sys

#Let's import our untokenized sentences
#with open('sentences.txt') as f:
#    sentences = f.read().split('\n')

# Let's import our Japanese dictionary
#with open('Japanese_dic.txt') as f:
#    the_dictionary = f.read().split('\n')

# all_words = ['a', 'ab', 'b', 'c', 'brb']

def MaxMatch(sentence, dictionary):
    sentence = sentence.lower()
    if len (sentence) == 0:
        return '\n' #the_list

    for i in range(len(sentence), 0, -1):

        if i == 1:

            word = sentence[0]
            rest = sentence [1:]

            return (word + ' ' + MaxMatch (rest,dictionary))

        if sentence[:i] in dictionary:

            word = sentence[:i]
            rest = sentence[i:] #+ rest
            #i = len(sentence)
            return (word +' '+ MaxMatch (rest,dictionary))


#strng = 'And Lily would tell me no, and make up the most ridiculous ex- cuses, like the world would end if she were nice to her sister, or a centaur told her not to—the most ridiculous things, and I hated her for it. And when I had just graduated, I was going out with this boy, Vernon Durs- ley, he was fat and he was the only boy who would talk to me in college. And he said he wanted children, and that his first son would be named Dudley. And I thought to myself, what kind of parent names their child Dudley Dursley? It was like I saw my whole future life stretching out in front of me, and I couldn’t stand it. And I wrote to my sister and told her that if she didn’t help me I’d rather just'.split()
#for i in strng:
#    print (i, end = '')

#s = 'AndLilywouldtellmenoandmakeupthemostridiculousexcusesliketheworldwouldendifshewerenicetohersisteroracentaurtoldhernottothemostridiculousthingsandIhatedherforitAndwhenIhadjustgraduatedIwasgoingoutwiththisboyVernonDursleyhewasfatandhewastheonlyboywhowouldtalktomeincollege.AndhesaidhewantedchildrenandthathisfirstsonwouldbenamedDudleyAndIthoughttomyselfwhatkindofparentnamestheirchildDudleyDursley?ItwaslikeIsawmywholefuturelifestretchingoutinfrontofmeandIcouldntstanditAndIwrotetomysisterandtoldherthatifshedidnthelpmeIdratherjust'

#print (MaxMatch(s, all_words))
'''with open('tokenized_japanese.txt', 'w', encoding='utf-8') as f:
    for i in sentences:
        f.write(MaxMatch(i, the_dictionary) +  '\n')'''
            #MaxMatch(sentence, dictionary)


        #elif sentence[:i] not in dictionary:
         #   rest = sentence[i:] + rest

        #    sentence = sentence[:i]
        #word = sentence[0]

        #print ('Слово не в словаре, sent = ', sentence, ', rest = ', rest, 'i = ', i)

        #else:
         #   print ('Wow')


        #print('MaxMatch:', sentence, file=sys.stderr)

    #return the_list


# new_string = ''.join([i.strip() for i in string])
#new_string = 'abcbca'


#print (MaxMatch(new_string, all_words))
# print (' '.join([i for i in a]))

'''
with open('forms.txt') as f:
    jap_dictionary = f.read().split()

japanese_dic = []

for i in jap_dictionary:
    if i not in japanese_dic:
        japanese_dic.append(i)

with open('Japanese_dic.txt', 'w', encoding='utf-8') as f:
    f.write(''.join(i + '\n' for i in japanese_dic))

for i in range(10):
    print (japanese_dic[i])'''





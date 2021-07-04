import pyphen
import statistics
import os
import numpy as np
from sklearn.model_selection import train_test_split

from collections import OrderedDict

import pandas as pd
from sklearn.preprocessing import MultiLabelBinarizer

import nltk

from operator import add

from ordered_set import OrderedSet

import collections

pos_keys = ['ADJ', 'ADP', 'ADV', 'AUX', 'CCONJ', 'INTJ', 'NOUN', 'NUM', 'PRON', 'PROPN', 'PUNCT', 'SCONJ', 'SYM', 'VERB', 'X']

one_hot_encoded_pos_features_for_dict = {
    'ADJ': ['Abbr_0', 'Abbr_Yes', 'Case_0', 'Case_Abl', 'Case_Ade', 'Case_All', 'Case_Com', 'Case_Ela', 'Case_Ess', 'Case_Gen', 
         'Case_Ill', 'Case_Ine', 'Case_Ins', 'Case_Nom', 'Case_Par', 'Case_Tra', 'Clitic_0', 'Clitic_Kaan', 'Clitic_Kin', 
         'Clitic_Ko', 'Degree_0', 'Degree_Cmp', 'Degree_Pos', 'Degree_Sup', 'Derivation_0', 'Derivation_Inen', 
         'Derivation_Lainen', 'Derivation_Llinen', 'Derivation_Ton', 'NumType_0', 'NumType_Ord', 'Number_0', 
         'Number_Plur', 'Number_Sing', 'Number[psor]_0', 'Number[psor]_Sing', 'Person[psor]_0', 'Person[psor]_1', 
         'Person[psor]_2', 'Person[psor]_3', 'Style_0', 'Style_Coll', 'Typo_0', 'Typo_Yes'], 
 'ADP': ['AdpType_0', 'AdpType_Post', 'AdpType_Prep', 'Clitic_0', 'Clitic_Kaan', 'Clitic_Kin', 'Number[psor]_0', 
         'Number[psor]_Plur', 'Number[psor]_Sing', 'Person[psor]_0', 'Person[psor]_1', 'Person[psor]_2', 'Person[psor]_3', 
         'Style_0', 'Style_Coll', 'Typo_0', 'Typo_Yes'], 
 'ADV': ['Abbr_0', 'Abbr_Yes', 'Clitic_0', 'Clitic_Han', 'Clitic_Han,Ko', 'Clitic_Kaan', 'Clitic_Kin', 'Clitic_Ko', 
         'Clitic_Ko,S', 'Clitic_Pa', 'Clitic_Pa,S', 'Clitic_S', 'Degree_0', 'Degree_Cmp', 'Degree_Sup', 'Derivation_0', 
         'Derivation_Sti', 'Derivation_Ttain', 'Number[psor]_0', 'Number[psor]_Plur', 'Number[psor]_Sing', 'Person[psor]_0', 
         'Person[psor]_1', 'Person[psor]_2', 'Person[psor]_3', 'Style_0', 'Style_Coll', 'Typo_0', 'Typo_Yes'], 
 'AUX': ['Case_0', 'Case_Abe', 'Case_Ade', 'Case_Ela', 'Case_Ess', 'Case_Gen', 'Case_Ill', 'Case_Ine', 'Case_Ins', 'Case_Nom', 
         'Case_Par', 'Case_Tra', 'Clitic_0', 'Clitic_Han', 'Clitic_Han,Ko', 'Clitic_Han,Pa', 'Clitic_Ka', 'Clitic_Kaan', 
         'Clitic_Kin', 'Clitic_Ko', 'Clitic_Ko,S', 'Clitic_Pa', 'Clitic_Pa,S', 'Connegative_0', 'Connegative_Yes', 'Degree_0', 
         'Degree_Pos', 'InfForm_0', 'InfForm_1', 'InfForm_2', 'InfForm_3', 'Mood_0', 'Mood_Cnd', 'Mood_Imp', 'Mood_Ind', 
         'Mood_Pot', 'Number_0', 'Number_Plur', 'Number_Sing', 'Number[psor]_0', 'Number[psor]_Plur', 'Number[psor]_Sing', 
         'PartForm_0', 'PartForm_Agt', 'PartForm_Past', 'PartForm_Pres', 'Person_0', 'Person_1', 'Person_2', 'Person_3', 
         'Person[psor]_0', 'Person[psor]_1', 'Person[psor]_2', 'Person[psor]_3', 'Polarity_0', 'Polarity_Neg', 'Style_0', 
         'Style_Coll', 'Tense_0', 'Tense_Past', 'Tense_Pres', 'Typo_0', 'Typo_Yes', 'VerbForm_0', 'VerbForm_Fin', 
         'VerbForm_Inf', 'VerbForm_Part', 'Voice_0', 'Voice_Act', 'Voice_Pass'], 'CCONJ': ['Clitic_0', 'Clitic_Ko', 
                                                                                           'Style_0', 'Style_Coll'],
 'INTJ': ['Style_0', 'Style_Coll'], 'NOUN': ['Abbr_0', 'Abbr_Yes', 'Case_0', 'Case_Abe', 'Case_Abl', 'Case_Ade', 'Case_All', 
                                             'Case_Com', 'Case_Ela', 'Case_Ess', 'Case_Gen', 'Case_Ill', 'Case_Ine', 'Case_Ins',
                                             'Case_Nom', 'Case_Par', 'Case_Tra', 'Clitic_0', 'Clitic_Han', 'Clitic_Kaan', 
                                             'Clitic_Kin', 'Degree_0', 'Degree_Pos', 'Derivation_0', 'Derivation_Inen,Vs', 
                                             'Derivation_Ja', 'Derivation_Ja,Tar', 'Derivation_Lainen', 'Derivation_Lainen,Vs',
                                             'Derivation_Llinen,Vs', 'Derivation_Minen', 'Derivation_Tar', 'Derivation_Ton', 
                                             'Derivation_Ton,Vs', 'Derivation_U', 'Derivation_Vs', 'Number_0', 'Number_Plur', 'Number_Sing', 'Number[psor]_0', 'Number[psor]_Plur', 'Number[psor]_Sing', 'Person[psor]_0', 'Person[psor]_1', 'Person[psor]_2', 'Person[psor]_3', 'Style_0', 'Style_Arch', 'Style_Coll', 'Typo_0', 'Typo_Yes'], 'NUM': ['Case_0', 'Case_Abl', 'Case_Ade', 'Case_All', 'Case_Ela', 'Case_Ess', 'Case_Gen', 'Case_Ill', 'Case_Ine', 'Case_Ins', 'Case_Nom', 'Case_Par', 'Case_Tra', 'Clitic_0', 'Clitic_Kaan', 'Clitic_Kin', 'NumType_0', 'NumType_Card', 'Number_0', 'Number_Plur', 'Number_Sing', 'Style_0', 'Style_Coll'], 'PRON': ['Case_0', 'Case_Abl', 'Case_Acc', 'Case_Ade', 'Case_All', 'Case_Com', 'Case_Ela', 'Case_Ess', 'Case_Gen', 'Case_Ill', 'Case_Ine', 'Case_Ins', 'Case_Nom', 'Case_Par', 'Case_Tra', 'Clitic_0', 'Clitic_Han', 'Clitic_Han,Ko', 'Clitic_Kaan', 'Clitic_Kin', 'Clitic_Ko', 'Clitic_Pa', 'Clitic_S', 'Degree_0', 'Degree_Pos', 'Number_0', 'Number_Plur', 'Number_Sing', 'Number[psor]_0', 'Number[psor]_Plur', 'Number[psor]_Sing', 'Person_0', 'Person_1', 'Person_2', 'Person_3', 'Person[psor]_0', 'Person[psor]_1', 'Person[psor]_2', 'Person[psor]_3', 'PronType_0', 'PronType_Dem', 'PronType_Ind', 'PronType_Int', 'PronType_Prs', 'PronType_Rcp', 'PronType_Rel', 'Reflex_0', 'Reflex_Yes', 'Style_0', 'Style_Coll', 'Typo_0', 'Typo_Yes'], 'PROPN': ['Abbr_0', 'Abbr_Yes', 'Case_0', 'Case_Abl', 'Case_Ade', 'Case_All', 'Case_Ela', 'Case_Ess', 'Case_Gen', 'Case_Ill', 'Case_Ine', 'Case_Ins', 'Case_Nom', 'Case_Par', 'Case_Tra', 'Clitic_0', 'Clitic_Kaan', 'Clitic_Kin', 'Clitic_Ko', 'Derivation_0', 'Derivation_Lainen', 'Number_0', 'Number_Plur', 'Number_Sing', 'Number[psor]_0', 'Number[psor]_Sing', 'Person[psor]_0', 'Person[psor]_2', 'Style_0', 'Style_Coll', 'Typo_0', 'Typo_Yes'], 'PUNCT': ['Typo_0', 'Typo_Yes'], 'SCONJ': ['Clitic_0', 'Clitic_Kin', 'Clitic_Ko', 'Style_0', 'Style_Coll'], 'SYM': ['Case_0', 'Case_Par'], 'VERB': ['Abbr_0', 'Abbr_Yes', 'Case_0', 'Case_Abe', 'Case_Abl', 'Case_Ade', 'Case_All', 'Case_Ela', 'Case_Ess', 'Case_Gen', 'Case_Ill', 'Case_Ine', 'Case_Ins', 'Case_Nom', 'Case_Par', 'Case_Tra', 'Clitic_0', 'Clitic_Han', 'Clitic_Han,Ko', 'Clitic_Ka', 'Clitic_Kaan', 'Clitic_Kin', 'Clitic_Ko', 'Clitic_Ko,S', 'Clitic_Pa', 'Clitic_Pa,S', 'Clitic_S', 'Connegative_0', 'Connegative_Yes', 'Degree_0', 'Degree_Pos', 'Degree_Sup', 'Derivation_0', 'Derivation_Ton', 'InfForm_0', 'InfForm_1', 'InfForm_2', 'InfForm_3', 'Mood_0', 'Mood_Cnd', 'Mood_Imp', 'Mood_Ind', 'Mood_Pot', 'Number_0', 'Number_Plur', 'Number_Sing', 'Number[psor]_0', 'Number[psor]_Plur', 'Number[psor]_Sing', 'PartForm_0', 'PartForm_Agt', 'PartForm_Neg', 'PartForm_Past', 'PartForm_Pres', 'Person_0', 'Person_1', 'Person_2', 'Person_3', 'Person[psor]_0', 'Person[psor]_1', 'Person[psor]_2', 'Person[psor]_3', 'Polarity_0', 'Polarity_Neg', 'Style_0', 'Style_Arch', 'Style_Coll', 'Tense_0', 'Tense_Past', 'Tense_Pres', 'Typo_0', 'Typo_Yes', 'VerbForm_0', 'VerbForm_Fin', 'VerbForm_Inf', 'VerbForm_Part', 'Voice_0', 'Voice_Act', 'Voice_Pass'], 'X': ['Foreign_0', 'Foreign_Yes']}
											 
def average_dict_transf_to_list(dct,averaging_element):
    values_list = list(dct.values())
    ind = 0
    for el in values_list:
        try:
            el /= averaging_element
        except:
            pass
        values_list[ind] = round(el,5)
        ind += 1
    return values_list				 
							
file = '0_a.txt.parsed'				

def get_features(file, target_var, pos_keys, ohe_dict, predict = False):
    with open(file, "r", encoding = 'utf-8') as data:
        dict_of_ordered_pos_properties_dicts = {}
        pos_count = dict.fromkeys(pos_keys,0)
        for pos in pos_keys:
            ohe_feat = ohe_dict[pos]
            pos_keys_dict = dict.fromkeys(ohe_feat,0)
            pos_keys_ordered_dict = OrderedDict(pos_keys_dict)
            dict_of_ordered_pos_properties_dicts[pos] = pos_keys_ordered_dict
        #print(dict_of_ordered_pos_properties_dicts)
        
        pos_count_dict = dict.fromkeys(pos_keys,0)
        pos_count_dict_ordered = OrderedDict(pos_count_dict)
        
        word_count = []#каждый эл-т - количество слов в предложении. сумма даст количество слов в юните,длина-кол-во предложений
        word_len_list = []
        word_len_syll_list = []
        inside_sentence = False
        
        syntax_markers_list = []
        
        edit_distance_list = []

        punctuation_count = 0
        
        syllables_counter = pyphen.Pyphen(lang='es_ES')
        more_than_three_syll_words_list = []
        more_than_three_syll_words_count = 0
        one_syll_words_count_per_unit = 0
        
        try:
                
            for line in data:
                    row = line.split('\t')
                    #handle last units
                    if((row[0][:8] == "# text =")):
                        #print(row[0][9:])
                        if (inside_sentence == True):
                            word_count.append(last_sentence_word_count)
                            more_than_three_syll_words_list.append(more_than_three_syll_words_count)
                            more_than_three_syll_words_count = 0
                        inside_sentence = True



                    if(str(row[0]).isdigit()):
                        syntax_markers_list.append(int(row[6]))

                        real_word = row[1].lower()
                        initial_form = row[2]
                        edit_distance_list.append(nltk.edit_distance(real_word,initial_form))

                        last_sentence_word_count = int(row[0])

                        if(row[3] != "PUNCT"):
                            current_pos = row[3]
                            word_len_list.append(len(row[1]))

                            pos_count_dict_ordered[current_pos] += 1

                            syll = syllables_counter.inserted(row[1])
                            syll_list = syll.split("-")
                            syll_count = len(syll_list)
                            word_len_syll_list.append(syll_count)
                            if (syll_count > 3):
                                more_than_three_syll_words_count += 1
                            elif(syll_count == 1):
                                one_syll_words_count_per_unit +=1


                            for prop in row[5].split('|'):
                                prop_list = prop.split("=")
                                if(len(prop_list) > 1):
                                    ohe_dict_key_val = prop_list[0] + '_' + prop_list[1]
                                    if(ohe_dict_key_val not in dict_of_ordered_pos_properties_dicts[current_pos].keys()):
                                        print ("net youba")
                                    dict_of_ordered_pos_properties_dicts[current_pos][ohe_dict_key_val] += 1
                        elif(row[1]!= "." and row[3] == "PUNCT"):
                            punctuation_count += 1
        except:
            print("get_features did not work")    
            return             
                        
        #print(syntax_markers_list)
        #append last items
        word_count.append(last_sentence_word_count)
        more_than_three_syll_words_list.append(more_than_three_syll_words_count)
        #word_count
        med_word_count = round(statistics.median(word_count),3)
        #av_word_len_syll
        med_word_len_syll = round(statistics.median(word_len_syll_list),3)
        #av_word_len_letters
        med_word_len_letters = round(statistics.median(word_len_list),3)
        
        #syllable
        med_more_th_three = round(statistics.median(more_than_three_syll_words_list),3)
        
        one_syll_words_percent = round(one_syll_words_count_per_unit / sum(word_count),3)
        
        #word_distance
        med_edit_distance = round(statistics.median(edit_distance_list),3)
        
        #av_punctuation_per_sentence
        av_punctuation_per_sentence = round(punctuation_count / len(word_count),2)
        
        #syntax_median = round(statistics.median(syntax_markers_list),3)

        
    
        
    ret_list = [med_word_count,med_word_len_syll,med_word_len_letters,
         med_more_th_three, one_syll_words_percent, med_edit_distance, av_punctuation_per_sentence]
    
    #averaged POS amount
    pos_av = average_dict_transf_to_list(pos_keys_ordered_dict, sum(pos_keys_ordered_dict.values()))
    ret_list += pos_av
    
    pos_count_dict_ordered_values = list(pos_count_dict_ordered.values())
    pos_per_word_count = [round(x / sum(word_count),3) for x in pos_count_dict_ordered_values]
    
    ret_list += pos_per_word_count
    
    #handle_pos_properties
    for pos in dict_of_ordered_pos_properties_dicts.keys():
        pos_properties_values_list = list(dict_of_ordered_pos_properties_dicts[pos].values())
        current_pos_count = pos_count[pos]
        try:
            pos_properties_per_pos_count = [round(x / current_pos_count,3) for x in pos_properties_values_list]
        except:
            pos_properties_per_pos_count = pos_properties_values_list
        #print(pos, list(dict_of_ordered_pos_properties_dicts[pos].values()),'\n')
        #print(pos, pos_properties_per_pos_count,current_pos_count,'\n')   
        pos_properties_per_word_count = [round(x / sum(word_count),3) for x in pos_properties_values_list]
        ret_list += pos_properties_per_pos_count
        ret_list += pos_properties_per_word_count
    if(predict == False):
        ret_list.append(target_var)
    #print(ret_list)
    return ret_list
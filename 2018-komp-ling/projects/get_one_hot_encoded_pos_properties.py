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



def get_pos_pareameters_list(file, POS):
    pos_properties_list = []
    with open(file, "r", encoding = 'utf-8') as data:
        try:
            for line in data:
                row = line.split('\t')
                if(str(row[0]).isdigit()):
                    if(row[3] == POS):
                        for prop in row[5].split('|'):
                            prop_list = prop.split("=")
                            pos_properties_list.append(prop_list[0])
        except:
            print("get_pos_pareameters_list error raised")
                    
    return pos_properties_list
	
def get_pos_properties_values (file, POS, POS_properties_list):
    properties_dict = dict.fromkeys(POS_properties_list,0)
    properties_ordered_dict = OrderedDict(properties_dict)
    properties_ordered_dict_list = []
    with open(file, "r", encoding = 'utf-8') as data:
        try:
            for line in data:
                row = line.split('\t')
                if(str(row[0]).isdigit()):
                    if(row[3] == POS):
                        for prop in row[5].split('|'):
                            #print(row[1],row[5])
                            prop_list = prop.split("=")
                            try:
                                if(prop_list[0] not in POS_properties_list):
                                   print(prop_list[0],"property is not predefined")
                                properties_ordered_dict[prop_list[0]] = prop_list[1]
                            except:
                                pass
                        properties_ordered_dict_list.append(list(properties_ordered_dict.values()))
        except:
            print("get_pos_properties_values raised error")
    return properties_ordered_dict_list


def get_pos_ohe_properties_list(root, subfolders_list, POS):

    output_data_prep = []
    for folder in subfolders_list:
        for file in os.listdir(os.path.join(root, folder)):
            #print(os.path.join(root, folder, file ))
            if ("parsed" in file):
                unit_data = get_pos_pareameters_list(os.path.join(root, folder, file ),POS)
                output_data_prep.append(unit_data)
                
    pd_data_prep = pd.Series(output_data_prep)
    mlb = MultiLabelBinarizer()
    res = pd.DataFrame(mlb.fit_transform(pd_data_prep),
                       columns=mlb.classes_,
                       index=pd_data_prep.index)
    pos_properties = list(res.columns.values)
    
    #print(res.head(30))
    
    all_pos_properties = []
    for folder in subfolders_list:
        for file in os.listdir(os.path.join(root, folder)):
            #print(os.path.join(root, folder, file ))
            if ("parsed" in file):
                unit_data = get_pos_properties_values(os.path.join(root, folder, file ),POS ,pos_properties)
                all_pos_properties.append(unit_data)
                
    all_pos_properties_by_unit = []
    #fistr_unit = all_pos_properties[0][0]
    for unit in all_pos_properties:
        for verb in unit:
            all_pos_properties_by_unit.append(verb)
            #if(len(fistr_unit) != len(verb)):
                #print(fistr_unit, verb)
            #assert len(fistr_unit) == len(verb)
            
    #print(len(all_pos_properties_by_unit[0]), len(pos_properties))    
    pos_df = pd.DataFrame(all_pos_properties_by_unit, columns=pos_properties)
    drop_column_name_list = []
    print("show unique elements (one value properties will be ignored in final dictionary)")
    for ind in range(len(pos_properties)):
        column_unique_values = pos_df.iloc[:,ind].unique()
        print(pos_properties[ind], column_unique_values)
        if(len(column_unique_values) == 1):
            drop_column_name_list.append(pos_properties[ind])
            
            
    #for drop_column_name in drop_column_name_list:
    pos_df = pos_df.drop(columns = drop_column_name_list)
    
    pos_df_ohe = pd.get_dummies(pos_df)
    pos_df_ohe_features = list(pos_df_ohe.columns.values)
    pos_df_ohe_features_set = OrderedSet(pos_df_ohe_features)
    
    """	
    print("show unique elements")
    for ind in range(len(pos_properties)):
        print(pos_properties[ind], pos_df.iloc[:,ind].unique())"""	
          
    return pos_df_ohe_features_set.items
"""	
def get_pos_ohe_properties_list(root, subfolders_list, POS):

    output_data_prep = []
    for folder in folders:
        for file in os.listdir(os.path.join(root, folder)):
            #print(os.path.join(root, folder, file ))
            if ("parsed" in file):
                unit_data = get_pos_pareameters_list(os.path.join(root, folder, file ),POS)
                output_data_prep.append(unit_data)
                
    pd_data_prep = pd.Series(output_data_prep)
    mlb = MultiLabelBinarizer()
    res = pd.DataFrame(mlb.fit_transform(pd_data_prep),
                       columns=mlb.classes_,
                       index=pd_data_prep.index)
    pos_properties = list(res.columns.values)
    
    #print(res.head(30))
    
    all_pos_properties = []
	
    for folder in folders:
        for file in os.listdir(os.path.join(root, folder)):
            #print(os.path.join(root, folder, file ))
            if ("parsed" in file):
                unit_data = get_pos_properties_values(os.path.join(root, folder, file ),POS ,pos_properties)
                all_pos_properties.append(unit_data)
				
    leng = set()            
    all_pos_properties_by_unit = []
    for unit in all_pos_properties:
        for verb in unit:
            all_pos_properties_by_unit.append(verb)
            leng.add(len(verb))
			
    print("List of unique elements of this Part Of Speech (one value parameters will be ignored in final dict)")
    for ind in range(len(pos_properties)):
        print(pos_properties[ind], pos_df.iloc[:,ind].unique())
		
    pos_df = pd.DataFrame(all_pos_properties_by_unit, columns=pos_properties)
    pos_df_ohe = pd.get_dummies(pos_df)
    pos_df_ohe_features = list(pos_df_ohe.columns.values)
    pos_df_ohe_features_set = OrderedSet(pos_df_ohe_features)

    return pos_df_ohe_features_set.items"""	

pos_keys = ['ADJ', 'ADP', 'ADV', 'AUX', 'CCONJ', 'INTJ', 'NOUN', 'NUM', 'PRON', 'PROPN', 'PUNCT', 'SCONJ', 'SYM', 'VERB', 'X']	
dirname = os.path.dirname(__file__)
root = os.path.join(dirname,"data","parsed_data")
folders =['a','b','c']
pos_keys_dict = dict.fromkeys(pos_keys,[])
for pos in pos_keys:
    print("NOW HANDLING ", pos)
    ohe_features = get_pos_ohe_properties_list(root, folders, pos)
    #print(pos, " features are \n", ohe_features)
    pos_keys_dict[pos] = ohe_features
print("one hot encoded features are", pos_keys_dict)
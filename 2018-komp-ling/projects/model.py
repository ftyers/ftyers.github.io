import os
from sklearn import svm
from sklearn.model_selection import train_test_split
import numpy as np
import pickle
from get_features import pos_keys, one_hot_encoded_pos_features_for_dict, get_features
  
dirname = os.path.dirname(__file__)
root = os.path.join(dirname,"data","parsed_data")
folders =['a','b','c']
data = []
target = 0
stop_cond = 0
for folder in folders:
    target += 1
    print("Wordking on folder", folder)
    for file in os.listdir(os.path.join(root, folder)):
        #print(os.path.join(root, folder, file ))
        if ("parsed" in file):
            unit_data = get_features(os.path.join(root, folder, file), target, pos_keys, one_hot_encoded_pos_features_for_dict) 
            #if(len(unit_data) != 307):
                #print(os.path.join(root, folder, file))
            if(unit_data):
                data.append(unit_data)
        stop_cond += 1

#print(data[0])

np_data = np.array(data)
#print(np_data .shape)#should be 2 dimensional (xx,xx))
X_data = np_data[:,0:-1]
Y_data = np_data[:,-1]

X_train, X_test, y_train, y_test = train_test_split(X_data, Y_data, test_size=0.3, random_state=0)
#print(X_train.shape, X_test.shape)
clf = svm.SVC(kernel='linear', C=1).fit(X_train, y_train)
print("SVM accuracy is", clf.score(X_test, y_test))
print(X_test.shape, y_test.shape)

#https://machinelearningmastery.com/save-load-machine-learning-models-python-scikit-learn/
filename = 'finalized_model.sav'
pickle.dump(clf, open(filename, 'wb'))
    
                                             
import pickle
import argparse
import numpy as np
from get_features import pos_keys, one_hot_encoded_pos_features_for_dict, get_features

parser = argparse.ArgumentParser(add_help=True)
parser.add_argument('file_for_analyzing', type=str, help='file_for_analyzing')
args = parser.parse_args()

loaded_model = pickle.load(open('finalized_model.sav', 'rb'))   
test_file = args.file_for_analyzing
print("predict with trained model")
object_features = get_features(test_file, None , pos_keys, one_hot_encoded_pos_features_for_dict, predict = True)

object_features_array = np.asarray(object_features)
object_features_array = object_features_array.reshape(1, -1)
#print(object_features)
print(loaded_model.predict(object_features_array))
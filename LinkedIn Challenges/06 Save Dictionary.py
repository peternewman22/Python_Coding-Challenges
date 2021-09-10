import json
from os import path, getcwd


def save_dict(file_path: str, dict_to_save: dict):
    with open(file_path,"w") as fh:
        json.dump(dict_to_save, fh)

def load_dict(file_path: str) -> dict:
    with open(file_path, "r") as fh:
        return json.load(fh)

test_path = path.join(getcwd(),"test_dict.json")
test_dict = {'one' : 1, 'two' : 2, 'three' : 3}

save_dict(test_path, test_dict)
print("dict save successful")
retrieved_dict = load_dict(test_path)
print(retrieved_dict)


"""
Note: alternative is pickling = python-specific, slower, less secure and not human-readable, but it can handle nearly any python data structure 
"""
import pickle

def save_dict_pickle(file_path: str, dict_to_save: dict):
    with open(file_path, "wb") as fh:
        pickle.dump(dict_to_save, fh)

def load_dict_pickle(file_path: str) -> dict:
    with open(file_path, "rb") as fh:
        return pickle.load(fh)
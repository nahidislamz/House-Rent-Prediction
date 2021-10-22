from joblib import load
import json
import numpy as np
import os

module_dir = os.path.dirname(__file__)  # get current directory
columns_path = os.path.join(module_dir, 'columns.json')
model_path = os.path.join(module_dir, 'model.joblib')

__locations = None
__data_columns = None
__model = None

def get_estimated_price(location,sqft,bhk,bath):
    try:
        loc_index = __data_columns.index(location.lower())
    except:
        loc_index = -1

    x = np.zeros(len(__data_columns))
    x[0] = sqft
    x[1] = bath
    x[2] = bhk
    if loc_index>=0:
        x[loc_index] = 1

    return round(__model.predict([x])[0],2)


def load_saved_artifacts():
    global  __data_columns
    global __locations

    with open(columns_path, "r") as f:
        __data_columns = json.load(f)['data_columns']
        __locations = __data_columns[3:]  # first 3 columns are sqft, bath, bhk

    global __model
    if __model is None:
        with open(model_path, 'rb') as f:
            __model = load(f)


def get_location_names():
    return __locations

def get_data_columns():
    return __data_columns


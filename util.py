import json
import pickle
import numpy as np

# Creating 3 global variables
__locations = None
__data_columns = None
__model = None

def get_estimated_price(location,sqft,bhk):
    try:
        loc_index = __data_columns.index(location.lower())
    except:
        loc_index = -1

    x = np.zeros(len(__data_columns))

    x[0] = bhk
    x[1] = sqft
    if loc_index >= 0:
        x[loc_index] = 1
    return round(__model.predict([x])[0], 2)

def get_location_names():
    return __locations

def load_saved_artifacts():
    print("loading saved artifacts...start")
    global __data_columns
    global __locations

    with open("C:/Users/vijay/Mumbai_House_Price_Prediction/server/artifacts/columns.json", 'r') as f:
        __data_columns = json.load(f)['data_columns']
        __locations = __data_columns[2:-4]

    global __model
    with open("C:/Users/vijay/Mumbai_House_Price_Prediction/server/artifacts/Mumbai_house_prices_model.pickle", 'rb') as f:
        __model = pickle.load(f)
        print("loading saved artifacts...done")


if __name__ == '__main__':
    load_saved_artifacts()
    #print(get_location_names())
    print(get_estimated_price('Agripada',600, 2))
    print(get_estimated_price('Andheri West',600, 2))
    print(get_estimated_price('Airoli',1233, 4))

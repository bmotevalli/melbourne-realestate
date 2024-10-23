import pickle
import os
from app.models.house import House

dirname = os.path.dirname(os.path.abspath(__file__))

def load_trained_model():
    with open(os.path.join(dirname, 'rf_trained_model.pkl'), 'rb') as model_file:
        return pickle.load(model_file)
    

def predict_price(house: House):
    feats = house.get_features()
    model = load_trained_model()
    return model.predict(feats)[0]
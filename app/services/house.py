import pickle
import os
import pandas as pd
from pygwalker.api.streamlit import StreamlitRenderer
import streamlit as st
from app.models.house import House

dirname = os.path.dirname(os.path.abspath(__file__))

def load_trained_model():
    with open(os.path.join(dirname, 'rf_trained_model.pkl'), 'rb') as model_file:
        return pickle.load(model_file)
    

def predict_price(house: House):
    feats = house.get_features()
    model = load_trained_model()
    return model.predict(feats)[0]


@st.cache_resource
def get_pyg_renderer() -> "StreamlitRenderer":
    df = pd.read_csv(os.path.join(dirname,"..", "..", "data", "melb_data.csv"))
    # If you want to use feature of saving chart config, set `spec_io_mode="rw"`
    return StreamlitRenderer(df, spec="./gw_config.json", spec_io_mode="rw")

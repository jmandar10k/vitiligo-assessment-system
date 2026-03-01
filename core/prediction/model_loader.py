import os
import pickle
from functools import lru_cache

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
MODEL_PATH = os.path.join(BASE_DIR, "models", "best.pkl")

@lru_cache()
def load_svc_model():
    with open(MODEL_PATH, "rb") as file:
        model = pickle.load(file)
    return model
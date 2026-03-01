import os
from functools import lru_cache
from tensorflow.keras.models import load_model

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
MODEL_PATH = os.path.join(BASE_DIR, "models", "vitiligo-resnet-finetuned-01.h5")


@lru_cache()
def load_resnet_model():
    return load_model(MODEL_PATH)
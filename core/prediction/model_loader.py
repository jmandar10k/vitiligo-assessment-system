import os
import pickle
from functools import lru_cache

from huggingface_hub import hf_hub_download


@lru_cache()
def load_svc_model():

    model_path = hf_hub_download(
        repo_id="mandar10/vitiligo-models",
        filename="best.pkl"
    )

    with open(model_path, "rb") as f:
        model = pickle.load(f)

    return model
import os
from functools import lru_cache

from tensorflow.keras.models import load_model
from huggingface_hub import hf_hub_download


@lru_cache()
def load_resnet_model():

    # Download .h5 model from Hugging Face
    model_path = hf_hub_download(
        repo_id="mandar10/vitiligo-models",
        filename="vitiligo-resnet-finetuned-01.h5"
    )

    return load_model(model_path)
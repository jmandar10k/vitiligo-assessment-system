import numpy as np
from core.prediction.model_loader import load_svc_model


def predict_vitiligo_risk(
    diet_score,
    environmental_score,
    lifestyle_score,
    psychological_score,
    family_score,
    combined_score
):

    model = load_svc_model()

    scores_input = np.array([[
        diet_score,
        environmental_score,
        lifestyle_score,
        psychological_score,
        family_score,
        combined_score
    ]])

    prediction = model.predict(scores_input)[0]

    return prediction